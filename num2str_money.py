import re
DICT_NUM2SIM = {"0": "〇", "1": "一", "2": "二", "3": "三", "4": "四", "5": "五", "6": "六",
                "7": "七", "8": "八", "9": "九"}
DICT_SIM2FOR = {"〇": "零", "一": "壹", "二": "贰", "三": "叁", "四": "肆", "五": "伍", "六": "陆",
                "七": "柒", "八": "捌", "九": "玖", "十": "拾", "百": "佰", "千": "仟"}


def parser_local(s):
    """
    千位以内的整数数字转换
    :param s: string, like 1234
    :return: string, like 一千二百三十四
    """
    global DICT_NUM2SIM
    if not s.isdigit():
        raise ValueError("[ERROR] s is not pure digital [require 0-9].")
    if len(s) > 4:
        raise ValueError("[ERROR] s is over-length in parser_local [require len<=4].")
    if len(s) < 1:
        raise ValueError("[ERROR] s is empty in parser_local [require len>0].")
    suffix = ["", "十", "百", "千"]
    s_new = str()
    s = s[::-1]
    for i, c in enumerate(s):
        if c == "0":
            s_new += DICT_NUM2SIM[c]
        else:
            s_new += suffix[i] + DICT_NUM2SIM[c]
    s_new = s_new[::-1]
    if len(s) < 4:
        s_new = DICT_NUM2SIM["0"] + s_new
    return s_new


def parser_global(s):
    """
    亿位以内的整数数字转换
    :param s: string, like 123456789876
    :return: string, like 一千二百三十四亿五千六百七十八万九千八百七十六
    """
    global DICT_NUM2SIM
    if not s.isdigit():
        raise ValueError("[ERROR] s is not pure digital [require 0-9].")
    if len(s) > 12:
        raise ValueError("[ERROR] s is over-length in parser_local [require len<=12].")
    if len(s) < 1:
        raise ValueError("[ERROR] s is empty in parser_local [require len>0].")
    suffix = ["", "万", "亿"]
    s_tempor = str()
    i = 0
    s_new = str()
    s = s[::-1]
    for c in s:
        if len(s_tempor) == 4:
            if i > 2:
                i = 0
            s_tempor = parser_local(s_tempor)
            s_new += suffix[i] + s_tempor[::-1]
            i += 1
            s_tempor = c
        else:
            s_tempor = c + s_tempor
    if i > 2:
        i = 0
    s_tempor = parser_local(s_tempor)
    s_new += suffix[i] + s_tempor[::-1]
    s_new = s_new[::-1]
    s_new = re.sub("〇+", "〇", s_new)
    s_new = s_new.replace("〇万", "万").replace("〇亿", "亿")
    s_new = s_new.strip("〇")
    return s_new


def parser_decimal(s):
    """
    两位小数数字转换
    :param s: string, like 12
    :return: string, like 一角二分
    """
    global DICT_NUM2SIM
    if not s.isdigit():
        raise ValueError("[ERROR] s is not pure digital [require 0-9].")
    if len(s) < 1:
        raise ValueError("[ERROR] s is empty in parser_local [require len>0].")
    if len(s) == 1:
        s_new = DICT_NUM2SIM[s] + "角"
    else:
        s_new = DICT_NUM2SIM[s[0]] + "角" + DICT_NUM2SIM[s[1]] + "分"
    s_new = s_new.replace("〇角", "").replace("〇分", "")
    if len(s_new) == 0:
        s_new = "整"
    return s_new


def number2money(s, is_formal=True):
    """
    数字金额转大写金额表示法
    :param s: string, like 123456789.25
    :param is_formal: boolean, True for formal Chinese expresion, False for simple Chinese expresion
    :return: string, like 壹亿贰仟叁佰肆拾伍万陆仟柒佰捌拾玖元贰角伍分
    """
    global DICT_SIM2FOR
    s = re.sub("[,，]+", "", s)
    s = re.sub("[.。]+", ".", s)
    if s.isdigit():
        s_new = parser_global(s) + "元整"
    else:
        if len(re.findall("\.", s)) == 1:
            s_split = s.split(".")
            s_new = parser_global(s_split[0]) + "元" + parser_decimal(s_split[1])
        else:
            raise ValueError("[ERROR] Not amount of money [require xxxxxx.xx].")
    if is_formal:
        s_new = "".join([DICT_SIM2FOR.get(c, c) for c in s_new])
    return s_new


if __name__ == "__main__":
    print(number2money("123456789.42"))
