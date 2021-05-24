import re
import jieba
ADD_NAME = ["市", "区", "号", "省", "路", "县", "镇", "楼", "道", "村", "室", "街", "层", "幢", "园",
            "城", "州", "栋", "组", "场", "疆", "乡", "房", "苑", "家", "段", "口", "江", "河", "里",
            "门", "座", "巷", "弄", "庄", "湾", "院", "港", "塘", "站", "所", "坪", "津", "盟", "关",
            "坝", "屋", "馆", "部", "台", "屯", "坊", "户", "居", "寨", "堡", "滨", "庙", "滩", "岗",
            "坡", "侧"]


def find_split_idx(s, see=False):
    """
    反馈输入字符串的jieba切分下标信息。
    :param s: string, 地址字符串
    :param see: boolean, True打印输入输出，否则False
    :return: list, jieba判断应切分的词的下标信息
    """
    idx = 0
    lst_split = list()
    lst_jieba = jieba.lcut(s)
    for word in lst_jieba:
        idx += len(word)
        lst_split.append(idx)
    lst_split = lst_split[:-1]
    if see:
        print(s)
        print(lst_jieba)
        print([s[idx] for idx in lst_split])
    return lst_split


def address_seg(s, see=False):
    """
    切分单个长地址为更小的地址单元。
    :param s: string, 地址字符串
    :param see: boolean, True打印输入输出，否则False
    :return: string,切分后的地址列表
    """
    global ADD_NAME
    s = re.sub("\(.+\)", "", s)
    split_idx = find_split_idx(s)
    lst_s = list()
    stack_s = ""
    for i_c, c in enumerate(s):
        if c in ADD_NAME:  # 当前字是切分关键字
            if i_c + 1 < len(s):  # 当前字不在句末
                if s[i_c+1] in ADD_NAME:  # 下一个字是切分关键字
                    stack_s += c
                else:  # 下一个字不是切分关键字
                    stack_s += c
                    if stack_s not in lst_s:  # 当前地址单元未在之前出现，出现情况如：【X县】X区【X县政府办公楼】X号
                        if i_c+1 in split_idx:  # 切分点前后两字不构成词，出现情况如：X【省际】工作单位
                            lst_s.append(stack_s)
                            stack_s = ""
            else:  # 当前字在句末
                stack_s += c
                lst_s.append(stack_s)
        else:  # 当前字不是切分关键字
            stack_s += c
    if len(stack_s) > 0:
        if stack_s not in lst_s:
            lst_s.append(stack_s)
    if see:
        print(s)
        print(lst_s)
    return lst_s


if __name__ == "__main__":
    address_seg("南京市玄武区和燕路168号南京红山动物园", see=True)