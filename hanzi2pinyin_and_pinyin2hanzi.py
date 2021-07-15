from Pinyin2Hanzi import DefaultHmmParams, DefaultDagParams
from Pinyin2Hanzi import viterbi, dag
from Pinyin2Hanzi import simplify_pinyin, all_pinyin
from pypinyin import pinyin, lazy_pinyin
from random import choice

# reference
# Pinyin2Hanzi (by 乐天): https://github.com/letiantian/Pinyin2Hanzi
# pypinyin (by Huang Huang): https://github.com/mozillazg/python-pinyin

# initialization
DICT_PINYIN = {k: True for k in all_pinyin()}


def pinyin2hanzi(lst_s, method="viterbi", num_candi=3, log_score=False):
    """
    Transfer Chinece pinyin to Chinece word.
    :param lst_s: [pinyin_1, pinyin_2, ...] where pinyin_i is a string like "wo"(我)
    :param method: viterbi or dag
    :param num_candi: number of generated hanzi candidates.
    :param log_score: using log score to calculate or not.
    :return: best hanzi group, best hanzi's score, beast result, dictionary storing special char location
    """
    global DICT_PINYIN
    if isinstance(lst_s, list):
        if len(lst_s) > 0:
            # check pinyin
            lst_s_new = list()
            dict_s_empty = dict()
            for i_s, s in enumerate(lst_s):
                s = simplify_pinyin(s)
                if s in DICT_PINYIN.keys():
                    lst_s_new.append(s)
                else:
                    lst_s_new.append("a")  # record index of illegal pinyin
                    dict_s_empty.update({i_s: s})
            # settings
            if method == "dag":
                params = DefaultDagParams()
                func = dag
            else:
                params = DefaultHmmParams()
                func = viterbi
            # pinyin-to-hanzi
            res = func(params, lst_s_new, path_num=num_candi, log=log_score)
            res_best = ["" if i_w in dict_s_empty.keys() else w for i_w, w in enumerate(res[0].path)]  # 补回特殊符号的位置
            return res_best, res[0].score, res, dict_s_empty
        else:
            raise ValueError("[ERROR] Input is empty.")
    else:
        raise ValueError("[ERROR] Input is not a list.")


def hanzi2pinyin(s, method="pinyin"):
    """
    Transfer Chinece word to Chinece pinyin.
    :param s: string like "苟利国家生死以，岂因祸福避趋之"
    :param method: string, pinyin or lazy_pinyin
    :return: list = [pinyin_1, pinyin_2, ...] where special character would keep its original form
    """
    if isinstance(s, str):
        if len(s) > 0:
            if "lazy" in method:
                res = [p for p in lazy_pinyin(s)]
            else:
                res = [p[0] for p in pinyin(s)]
            return res
        else:
            raise ValueError("[ERROR] Input is empty.")
    else:
        raise ValueError("[ERROR] Input is not a string.")


def word_turbulance(s):
    """
    Input a word and return another word with same pronunciation.
    :param s: string, a word
    :return: string, a turbulent word
    """
    lst_s = hanzi2pinyin(s, method="lazy")
    _, _, candidates, d_empty = pinyin2hanzi(lst_s, method="viterbi", num_candi=5)
    lst_candidate = list()
    for candidate in candidates:
        lst_candi = [d_empty.get(i_w) if i_w in d_empty.keys() else w for i_w, w in enumerate(candidate.path)]
        candi = "".join(lst_candi)
        lst_candidate.append(candi)
    s_new = choice(lst_candidate)
    return s_new, lst_candidate


if __name__ == "__main__":
    # example 1
    res_p2h = pinyin2hanzi(['shui', 'neng', 'zai', 'zhou', '☆，', 'yi', 'ke', '♂', 'sai', 'ting', '。'])
    print("Best Result: {}\nBest Result Score: {}\nAll Candidates: {}\n\n".format(res_p2h[0], res_p2h[1], res_p2h[2]))

    # example 2
    res_h2p = hanzi2pinyin("水能载舟☆，亦可♂赛艇。")
    print("Result: {}\n".format(res_h2p))

    # example 3
    input = "水能载舟☆，亦可♂赛艇。"
    res_turb = word_turbulance(input)
    print("Old Word: {}\nNew Word: {}\nALL Candidates: {}\n".format(input, res_turb[0], res_turb[1]))
