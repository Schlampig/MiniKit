from jieba import posseg as jbp


def pos_simplizer(s):
    """
    Simplize the current part-of-speech (only focus on noun, verb, adjective, and adverb)
    :param s: string, the current part-of-speech
    :return: string, the updated (or not) part-of-speech
    """
    if s in ["an", "Ng", "n", "nr", "ns", "nt", "nz", "s", "vn", "j"]:
        s = "n"
    if s in ["v", "vd", "vg"]:
        s = "v"
    if s in ["a"]:
        s = "adj"
    if s in ["d", "ad", "dg"]:
        s = "adv"
    return s


def str2lst(s):
    """
    Split sentence into words corresponding to part-of-speech of each word
    :param s: string, input sentence
    :return: list, lst = [piece, piece, ...], where one piece might contain more than one word
    """
    lst = list()
    lst_tempor = list()
    for word, pos in jbp.lcut(s):
        pos = pos_simplizer(pos)
        if len(lst_tempor) > 0:
            if pos == "n":
                if lst_tempor[-1][1] in ["adj", "n"]:
                    lst_tempor.append([word, pos])
                else:
                    lst.append("".join(w for w, _ in lst_tempor))
                    lst_tempor = [[word, pos]]
            elif pos == "v":
                if lst_tempor[-1][1] in ["adv", "v"]:
                    lst_tempor.append([word, pos])
                else:
                    lst.append("".join(w for w, _ in lst_tempor))
                    lst_tempor = [[word, pos]]
            elif pos == "adj":
                if lst_tempor[-1][1] in ["adv", "adj"]:
                    lst_tempor.append([word, pos])
                else:
                    lst.append("".join(w for w, _ in lst_tempor))
                    lst_tempor = [[word, pos]]
            elif pos == "q":
                if lst_tempor[-1][1] in ["m"]:
                    lst_tempor.append([word, pos])
                else:
                    lst.append("".join(w for w, _ in lst_tempor))
                    lst_tempor = [[word, pos]]
            else:
                lst.append("".join(w for w, _ in lst_tempor))
                lst_tempor = [[word, pos]]
        else:
            lst_tempor = [[word, pos]]
    if len(lst_tempor) > 0:
        lst.append("".join(w for w, _ in lst_tempor))
    return lst


if __name__ == "__main__":
    res = str2lst("我特别喜欢吃红苹果，当然还有黑巧克力")
    print(res)
