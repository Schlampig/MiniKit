import difflib


def brute_search(lst, key):
    """
    顺序搜索key在lst中的index
    :param lst: list
    :param key: int
    :return: int, key在lst的第几个位置
    """
    assert key >= 0
    for i_idx, idx in enumerate(lst):
        if key == idx:
            return i_idx
        if key < idx:
            if i_idx == 0:
                return i_idx
            else:
                return i_idx - 1
    return len(lst) - 1


def fuzz_search(s, s_all, max_length=13):
    """
    求检索的字段在原文的起止点坐标
    :param s: string, 检索的字段
    :param s_all: string, 原文（经列表拼接而成，该列表可能来自前置任务输出，例如来自OCR或ASR）
    :param max_length: 判断两个候选识别字段断开的最大间隔，例如该值为3时，"abc def"→["abc def"]，"abc   def"→["abc", "def"]
    :return: int, int, idx_begin和idx_end分别为识别到的字段在原文的起止点坐标
    """
    d = difflib.Differ()
    difference = list(d.compare(s_all, s))
    lst_candi = list()
    candi = [None, None]
    length = 0
    for i_w, w in enumerate(difference):
        if "-" in w or i_w == len(difference) - 1:
            if candi[0] is not None:
                if candi[1] is not None:
                    if length > max_length:
                        lst_candi.append(candi)
                        candi = [None, None]
                        length = 0
                    else:
                        length += 1
                else:  # 一个字符的情形
                    candi[1] = candi[0]
                    lst_candi.append(candi)
                    candi = [None, None]
                    length = 0
            else:
                continue
        else:
            if candi[0] is not None:
                candi[1] = i_w
            else:
                candi[0] = i_w
    if candi[0] is not None and candi[1] is not None:
        lst_candi.append(candi)

    lst_candi.sort(key=lambda x: x[1] - x[0], reverse=True)
    idx_begin, idx_end = lst_candi[0][0], lst_candi[0][1]
    return idx_begin, idx_end


def block_search(idx_begin, idx_end, lst_idx):
    """
    根据检索的字段在原文的起止坐标，映射回列表项（列表可能来自前置任务输出，例如来自OCR或ASR）
    :param idx_begin: int， 识别字段在原文（s_all）的起点坐标
    :param idx_end: int， 识别字段在原文（s_all）的终点坐标
    :param lst_idx: list[int], 列表项(lst_all)在原文(s_all)的起点坐标
    :return: int, int, 第block_begin至第block_end个列表项（例，在OCR输出中即为第block_begin至第block_end个OCR的block）
    """
    block_begin = brute_search(lst_idx, idx_begin)
    block_end = brute_search(lst_idx, idx_end)
    if block_begin > block_end:
        block_begin = 0
        block_end = len(lst_idx) - 1
        print("[ERROR] block_begin > block_end, reset.")
    return block_begin, block_end


def see(lst_test, lst_all):
    """
    测试用脚本
    :param lst_test: list, 假设预测到的片段列表
    :param lst_all: list, 原文列表，首先会被拼接为原文s_all
    :return: None
    """
    # build raw text
    s_all = ""
    idx_now = 0
    lst_block = [0]
    for piece in lst_all:
        s_all += piece
        idx_now += len(piece)
        lst_block.append(idx_now)

    print("原始文本：\n {}".format(lst_all))
    print()
    print("原始Block下标：\n {}".format(lst_block))
    print()
    # test
    for i_s, s in enumerate(lst_test):
        print("测试例{}---------------------------------------".format(i_s+1))
        b, e = fuzz_search(s, s_all)
        print("预测句: {}\n".format(s))
        print("原句(起点({})，终点({})): {}\n".format(b, e, s_all[b:e]))
        b_new, e_new = block_search(b, e, lst_block)
        if b_new == e_new:
            print("对应的列表项{}：{}\n".format(b_new, lst_all[b_new]))
        else:
            print("对应的列表项{}至项{}：{}\n".format(b_new, e_new, lst_all[b_new:e_new+1]))
    return None


if __name__ == "__main__":

    raw = ["中国人民解放军总医院门诊病历\n",
           "患者ID：F F60673211	姓名：了不起的盖茨比	\t",
           "性别：男	年龄：40  岁	婚姻状况：\n",
           "费 别：出 地方医保 	就诊时间：2	2019-04-25",
           "下午		就诊科室：		肾病科门诊",
           "【主		诉】\n",
           "【简要病史1\n",
           "【 体		检】\n",
           "【辅助检查\n",
           "【诊		断】肾病综合征;高血压;膜性肾病; 水肿; 肾性骨病; 慢性静脉闭塞; 慢性病长期用药\n",
           "【处		置】\n",
           "1. 蚓激酶肠溶片	用法：60wu		口服		3/日\n",
           "   黄葵胶囊	用法：2.5g	口服	3/日",
           "托拉塞米片	用法：20mg	口服	1/日",
           "          他克莫司胶囊（杭州中美）	用法：2mg	口服	2/月",
           " 医生：王涌（签字）"]

    pred = ["断】肾病 综合征;高 病; 水肿; 肾性骨病; 慢 :) 脉",
            "2019年4月25日",
            "中国人民解放军总医院\t  患者ID：F F606",
            "托拉塞米片	用法：20mg	口服	1/日\n他克莫司胶囊（杭州中美）	用法：2mg	口服	2/月\n医生：王涌（签字）",
            "医"]

    see(lst_test=pred, lst_all=raw)
