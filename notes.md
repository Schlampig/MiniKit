### ASCII—UNICODE: 编码转换操作
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

### Collections库
- Counter

### Dictionary: 字典操作
- 合并两个字典
- 有序字典（OrderedDict）
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
