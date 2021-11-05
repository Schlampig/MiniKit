"""
【Citation】
[1] lcs: https://github.com/flatpickles/Python-LCS
[2] pyltp: https://github.com/HIT-SCIR/pyltp
"""
from random import choice
from jieba import posseg as jbp
from fuzzywuzzy import fuzz


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


class LCS(object):
    
    def __init__(self, l1, l2):
        self.list1 = l1
        self.list2 = l2

    def fuzz_compare(self, source, target):
        # note: two fuzz.ratio threshold could be manually set.
        flag = False
        if source == target:
            flag = True
        if ((source in target) or (target in source)) and fuzz.ratio(source, target) > 60:
            flag = True
        if fuzz.ratio(source, target) > 85:
            flag = True
        return flag

    def lcs_mat(self):
        m = len(self.list1)
        n = len(self.list2)
        mat = [[0] * (n + 1) for _ in range(m + 1)]
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if self.fuzz_compare(self.list1[row - 1], self.list2[col - 1]):
                    mat[row][col] = mat[row - 1][col - 1] + 1
                else:
                    mat[row][col] = max(mat[row][col - 1], mat[row - 1][col])
        return mat

    def all_lcs(self, lcs_dict, mat, index1, index2):
        if index1 in lcs_dict.keys() and index2 in lcs_dict.keys():
            return lcs_dict[(index1, index2)]
        if (index1 == 0) or (index2 == 0):
            return [[]]
        elif self.fuzz_compare(self.list1[index1 - 1], self.list2[index2 - 1]):
            lcs_dict[(index1, index2)] = [prevs + [[self.list1[index1 - 1], index1-1, index2-1]] for prevs in
                                          self.all_lcs(lcs_dict, mat, index1 - 1, index2 - 1)]
            return lcs_dict[(index1, index2)]
        else:
            lcs_list = []
            if mat[index1][index2 - 1] >= mat[index1 - 1][index2]:
                before = self.all_lcs(lcs_dict, mat, index1, index2 - 1)
                for series in before:
                    if not series in lcs_list:
                        lcs_list.append(series)
            if mat[index1 - 1][index2] >= mat[index1][index2 - 1]:
                before = self.all_lcs(lcs_dict, mat, index1 - 1, index2)
                for series in before:
                    if not series in lcs_list:
                        lcs_list.append(series)
            lcs_dict[(index1, index2)] = lcs_list
            return lcs_list

    # return a set of the sets of longest common subsequences in self.list1 and self.list2
    def get_lists(self):
        # mapping of indices to list of LCSs, so we can cut down recursive calls enormously
        mapping = dict()
        # start the process...
        return self.all_lcs(mapping, self.lcs_mat(), len(self.list1), len(self.list2))


def split_by_diff_fuzz(s_a, s_b, find_same=True):
    if isinstance(s_a, str) and isinstance(s_b, str):
        lst_a = str2lst(s_a)
        lst_b = str2lst(s_b)
    elif isinstance(s_a, list) and isinstance(s_b, list):
        lst_a = s_a
        lst_b = s_b
    else:
        raise KeyError("Source and Target are in wrong format [should be string or list].")
    lst_same = LCS(lst_a, lst_b).get_lists()
    if len(lst_same) == 1:
        lst_same = lst_same[0]
    else:
        lst_same = choice(lst_same)
    if find_same:
        lst_new_a, lst_new_b = list(), list()
        for same_unit in lst_same:
            _, i_a, i_b = same_unit
            lst_new_a.append(lst_a[i_a])
            lst_new_b.append(lst_b[i_b])
    else:
        same_idx_a, same_idx_b = list(), list()
        for _, i_a, i_b in lst_same:
            same_idx_a.append(i_a)
            same_idx_b.append(i_b)
        lst_new_a = [lst_a[i] for i in range(len(lst_a)) if i not in same_idx_a]
        lst_new_b = [lst_b[i] for i in range(len(lst_b)) if i not in same_idx_b]
    return lst_new_a, lst_new_b


if __name__ == "__main__":

    print(str2lst("这真就特么是一个测试不是？"))
    print(str2lst("这是个与众不同的测试属于是了"), "\n")

    res_a, res_b = split_by_diff_fuzz("这真就特么是一个测试不是？", "这是个与众不同的测试属于是了", find_same=True)
    print(res_a, "\n", res_b)
