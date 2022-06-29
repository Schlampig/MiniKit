def lst_strip(lst):
    """
    去掉列表头尾冗余的0，注：也可以把0换成别的元素
    例：[0, 0, 0, 1, 2, 0, 3, 4, 0, 2, 2, 0, 5, 0, 0, 0] -> [ 1, 2, 0, 3, 4, 0, 2, 2, 0, 5]
    :param lst: list
    :return: list, strip 0 at head and tail
    """
    idx_b, idx_e = 0, 0
    for i, w in enumerate(lst):
        if w > 0:
            if lst[idx_b] == 0:
                idx_b = i
                idx_e = i
            else:
                idx_e = i
        else:
            if idx_b == idx_e:
                idx_b = i
                idx_e = i
    lst_new = lst[idx_b:idx_e+1] if idx_e < len(lst) else lst[idx_b:]
    return lst_new
  
  
  if __name__ == "__main__":
    print(lst_strip([0, 0, 0, 1, 2, 0, 3, 4, 0, 2, 2, 0, 5, 0, 0, 0]))
