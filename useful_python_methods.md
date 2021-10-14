### ASCII到UNICODE: 编码转换操作
- **ord()**: ord()函数是chr()函数（对于8位的ASCII字符串）或unichr()函数（对于Unicode对象）的配对函数，其以一个字符作为参数，返回对应的ASCII或Unicode数值，若所给Unicode字符超出Python定义范围，则会引发一个TypeError异常。
- **chr()**: chr()函数以一个10进制或16进制的整数作为参数，返回该数对应的ASCII字符。
- **unichr()**: unichr()函数和chr()函数功能基本一样，只不过是返回Unicode字符。Python3不支持unichr()函数，改用chr()函数。
  ```bash
  >>> ord('熊')
  29066
  >>> chr(29066)
  '熊'
  >>> chr(0x42)
  'B'
  ```
- :notebook: 可使用ord()来限定某类符号的范围，例如汉语注音符号的范围是0x3100至0x312F。也可用ord()与chr()搭配用在需要互相转换的场合。
<br>

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
<br>

### Dictionary: 字典操作
- 合并字典
  - :notebook: 使用update，会修改dict_a的结构，如果不想更新dict_a，可以"d = dict(dict_a);d.update(dict_b);print(d)"：
    ```bash
    >>> dict_a = {"a": 1, "b": 2, "e":5}
    >>> dict_b = {"c": 3, "d": 4, "e":7}
    >>> dict_a.update(dict_b);dict_a
    {'a': 1, 'b': 2, 'e': 7, 'c': 3, 'd': 4}
    ```
  - 使用\*\*号：
    ```bash
    >>> dict_a = {"a": 1, "b": 2, "e":5}
    >>> dict_b = {"c": 3, "d": 4, "e":7}
    >>> {**dict_a, **dict_b}
    {'a': 1, 'b': 2, 'e': 7, 'c': 3, 'd': 4}
    ```
  - 使用dict(a,\*\*b)：
    ```bash
    >>> dict_a = {"a": 1, "b": 2, "e":5}
    >>> dict_b = {"c": 3, "d": 4, "e":7}
    >>> dict(dict_a, **dict_b)
    {'a': 1, 'b': 2, 'e': 7, 'c': 3, 'd': 4}
    ```
- 有序字典（OrderedDict）
  - 使用不同方式定义有序字典，例如依次插入key与value:
    ```bash
    >>> import collections
    >>> order_dict = collections.OrderedDict()
    >>> order_dict["a"] = 1
    >>> order_dict["b"] = 2
    >>> order_dict["c"] = 3
    >>> order_dict["d"] = 4
    >>> order_dict["e"] = 5
    ```
    或是以下形式：
    ```bash
    >>> order_dict = collections.OrderedDict({"e":5, "d":4, "c":3, "b":2, "a":1})
    >>> order_dict = collections.OrderedDict(e=5, d=4, c=3, b=2, a=1)
    >>> order_dict = collections.OrderedDict({k:v for k, v in [["e", 5], ["d", 4], ["c", 3], ["b", 2], ["a", 1]]})
    ```
    输出都一样：
    ```bash
    >>> for k, v in order_dict.items():
    ...     print(k, ": ", v)
    ... 
    e :  5
    d :  4
    c :  3
    b :  2
    a :  1
    ```
    :notebook: 由于改写了内部算法，Python3.6及之后版本的字典是有序的。
    
- itemgetter，attrgetter

### IsX操作
- isdigit()
- isalpha()
- isalnum()
- isupper(), islower(), upper(), lower()

### Itertools库

### List Comprehension: 链表解析
- 链表解析
- 含if...else...的链表解析
- 用生成器提速
- 字典链表解析

### Operator库

### Radix: 进制转换操作
- bin()
- oct()
- int()
- hex()

### Random库
- choice()
- shuffle()
- sample()
- seed()
- random()
- randint()
- uniform()
- randrange()

### Re库与正则表达式
- 环视
- ?: 贪婪与非贪婪搜索
- 跨行匹配
- finditer
- 分组

### Set: 集合操作
- 去重
- 交集
- 并集
- 差集

### Sort: 排序操作
- sort出现位置
- sort简单排序
- sort多键按优先级排序

### Time库与Timeit库
- time库
- timeit库

### 验证库
- voluptuous库
