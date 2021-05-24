import difflib


def get_diff(source, target):
    """
    比较source字符串和target字符串的差异，基于source字符串输出差异字符串。
    <ADD></ADD>中的字符为source没有而target新增的，<MISS></MISS>中的字符为source有而target删减的。
    :param source: string, 原始文本
    :param target: string, 对比文本
    :return: string, s_diff, 带差异tag的文本
    """
    d = difflib.Differ()
    lst_diff = list()
    tag = None
    for i_c, c in enumerate(list(d.compare(source, target))):
        c_now = c[-1]
        if c[0] == "+":
            c_tag = "<ADD>"
        elif c[0] == "-":
            c_tag = "<MISS>"
        else:
            c_tag = ""
        # add tag or continue
        if tag is not None:
            if c_tag != tag:
                if len(tag) > 0:
                    c_now = "<" + tag.strip("<") + c_tag + c_now
                else:
                    c_now = c_tag + c_now
                tag = c_tag
        else:
            tag = c_tag
            c_now = tag + c_now
        lst_diff.append(c_now)
    s_diff = "".join(lst_diff)
    return s_diff


def translate_html(lst_source, lst_target):
    """
    比较source列表和target列表的差异，生成形如在线文档对比的双栏Html静态网页。
    :param lst_source: list, 原文列表，每项可以是句、段、章等字符串
    :param lst_target: list, 对比文列表，每项可以是句、段、章等字符串
    :return: None, 生成一个Html文本
    """
    d = difflib.HtmlDiff(wrapcolumn=42, charjunk=None)  # wrapcolumn为Html显示栏宽
    diff = d.make_file(lst_source, lst_target)
    with open("compare_result.html", "w") as f:
        f.writelines(diff)
    return None


if __name__ == "__main__":
    s = """月光如流水一般，静静地泻在这一片叶子和花上。薄薄的青雾浮起在荷塘里。叶子和花仿佛在牛乳中洗过一样；
           又像笼着轻纱的梦。虽然是满月，天上却有一层淡淡的云，所以不能朗照；但我以为这恰是到了好处——酣眠固不可少，小睡也别有风味的。
           月光是隔了树照过来的，高处丛生的灌木，落下参差的斑驳的黑影，峭楞楞如鬼一般；弯弯的杨柳的稀疏的倩影，却又像是画在荷叶上。
           塘中的月色并不均匀；但光与影有着和谐的旋律，如梵婀玲上奏着的名曲。"""
    t = """月光如流水，静静泻在这片叶与花。薄雾浮起在荷塘。树影摇曳，叶与花仿佛在牛奶中洗过一般；
           又像笼着轻纱的梦。虽然今天是满月，空中却有一层淡云，而不能朗照；但我以为这恰到好处：酣眠固不可少，小睡也别有风味的。
           月光隔了树照来，高处丛生的灌木丛，落下参差斑驳的树影，如鬼一般；弯弯杨柳稀疏倩影，又像画在荷叶上。
           塘中月色并不均匀；但光与影有着和谐的旋律，如小提琴上奏着的名曲。"""
    res = get_diff(s, t)
    print(res)



