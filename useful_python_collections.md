### Collections库
- **Counter()**: 用于计数，以一个迭代器（数组，字符串，列表等）作为参数，返回对该迭代器中各项出现次数的统计结果。
  - 基础用法，统计结果：
    ```bash
    >>> from collections import Counter
    >>> Counter("this is a demo, just a demo")
    Counter({' ': 6, 's': 3, 't': 2, 'i': 2, 'a': 2, 'd': 2, 'e': 2, 'm': 2, 'o': 2, 'h': 1, ',': 1, 'j': 1, 'u': 1})
    ```
    或是，
    ```bash
    >>> from collections import Counter
    >>> Counter(['t', 'h', 'i', 's', 'i', 's', 'a', 'd', 'e', 'm', 'o', ',', 'j', 'u', 's', 't', 'a', 'd', 'e', 'm', 'o'])
    Counter({'s': 3, 't': 2, 'i': 2, 'a': 2, 'd': 2, 'e': 2, 'm': 2, 'o': 2, 'h': 1, ',': 1, 'j': 1, 'u': 1})
    ```
    也可以将Counter类型转为字典输出，
    ```bash
    >>> from collections import Counter
    >>> dict(Counter("this is a demo, just a demo"))
    {'t': 2, 'h': 1, 'i': 2, 's': 3, ' ': 6, 'a': 2, 'd': 2, 'e': 2, 'm': 2, 'o': 2, ',': 1, 'j': 1, 'u': 1}
    ```
  - 排序返回前K个高频字符：
    ```bash
    >>> cnt = Counter("this is a demo, just a demo")
    >>> cnt.most_common(3)  # 查看前3个高频字符
    [(' ', 6), ('s', 3), ('t', 2)]
    ```
  - 获取元素（注意两种方式区别）：
    ```bash
    >>> list(cnt)
    ['t', 'h', 'i', 's', ' ', 'a', 'd', 'e', 'm', 'o', ',', 'j', 'u']
    >>> list(cnt.elements())
    ['t', 't', 'h', 'i', 'i', 's', 's', 's', ' ', ' ', ' ', ' ', ' ', ' ', 'a', 'a', 'd', 'd', 'e', 'e', 'm', 'm', 'o', 'o', ',', 'j', 'u']
    ```
  - 查找元素：
    ```bash
    >>> cnt["z"]
    0
    >>> cnt["a"]
    2
    ```
  - :notebook: 自定义Counter对象及相关运算：
    ```bash
    >>> cnt_a = Counter(a=3, b=2, c=1);print(cnt_a)
    Counter({'a': 3, 'b': 2, 'c': 1})
    >>> cnt_b = Counter(a=1, b=2, c=3);print(cnt_b)
    Counter({'c': 3, 'b': 2, 'a': 1})
    >>> cnt_a + cnt_b
    Counter({'a': 4, 'b': 4, 'c': 4})
    >>> cnt_a - cnt_b
    Counter({'a': 2})
    >>> cnt_a & cnt_b
    Counter({'b': 2, 'a': 1, 'c': 1})
    >>> cnt_a | cnt_b
    Counter({'a': 3, 'c': 3, 'b': 2})
    ```
