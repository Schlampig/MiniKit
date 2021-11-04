"""
【Citation】
[1] lcs: https://github.com/flatpickles/Python-LCS
[2] pyltp: https://github.com/HIT-SCIR/pyltp
"""
import os
from random import choice
from jieba import posseg as jbp
from pyltp import Segmentor, Postagger


LTP_PATH = "your/ltp/model/path"
CWS_MODEL = Segmentor()
CWS_MODEL.load(os.path.join(LTP_PATH, "cws.model"))
POS_MODEL = Postagger()
POS_MODEL.load(os.path.join(LTP_PATH, "pos.model"))


class LCS(object):
    
    def __init__(self, l1, l2):
        self.list1 = l1
        self.list2 = l2

    def lcs_mat(self):
        m = len(self.list1)
        n = len(self.list2)
        mat = [[0] * (n + 1) for _ in range(m + 1)]
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if self.list1[row - 1] == self.list2[col - 1]:
                    mat[row][col] = mat[row - 1][col - 1] + 1
                else:
                    mat[row][col] = max(mat[row][col - 1], mat[row - 1][col])
        return mat

    def all_lcs(self, lcs_dict, mat, index1, index2):
        if index1 in lcs_dict.keys() and index2 in lcs_dict.keys():
            return lcs_dict[(index1, index2)]
        if (index1 == 0) or (index2 == 0):
            return [[]]
        elif self.list1[index1 - 1] == self.list2[index2 - 1]:
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


def str2list(s, use_ltp=False):
    """
    Split the input text into "word"s and find the attribute for each word as "attr"
    :param s: string, input text
    :param use_ltp: bool, True to use LTP, False to use jieba
    :return: list lst = [[word, attr], ...]
    """
    global CWS_MODEL, POS_MODEL
    if use_ltp:
        lst_s = list(CWS_MODEL.segment(s))
        lst_pos= list(POS_MODEL.postag(lst_s))
        lst = [[lst_s[i], lst_pos[i]] for i in range(len(lst_s))]
    else:
        lst = [[w, p] for w, p in jbp.lcut(s)]
    return lst


def find_diff(s_a, s_b, find_same=True):
    lst_a = str2list(s_a)
    lst_b = str2list(s_b)
    lst_word_a = [word for word, _ in lst_a]
    lst_word_b = [word for word, _ in lst_b]
    lst_same = LCS(lst_word_a, lst_word_b).get_lists()
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
    # example 1
    lst_all = LCS(['这', '真就', '特', '么', '是', '一个', '测试', '不是', '?'],
                  ['这', '是', '个', '与众不同', '的', '测试', '属于', '是', '了']).get_lists()
    print(lst_all)

    # example 2
    print(str2list("这真就特么是一个测试不是？"), "\n")
    print(str2list("这是个与众不同的测试属于是了"), "\n")

    # example 3
    res_a, res_b = find_diff("这真就特么是一个测试不是？", "这是个与众不同的测试属于是了", find_same=True)
    print(res_a, "\n", res_b)
