### Dictionary & Tuple: 字典与元组操作
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
  - 使用不同方式定义**OrderedDict**，例如依次插入key与value:
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
    
- **itemgetter()**: 
  - 搭配排序相关方法（如**sorted()**）的入参**key**使用，指定列表中**字典**的排序逻辑。**key=itemgetter("key_name")** 功能等价于 **key=lambda x: x\["key_name"]**:
    ```bash
    >>> lst_people = [{"name": "Alice", "job": "Computer Science", "age": "32"},
                      {"name": "Bob", "job": "Software Engineer", "age": "27"}, 
                      {"name": "Chris", "job": "System Administrator", "age": "30"}, 
                      {"name": "David", "job": "Project Manager", "age": "33"}]
                      
    >>> from operator import itemgetter
    
    >>> sorted(lst_people, key=itemgetter("job"))
        [{'name': 'Alice', 'job': 'Computer Science', 'age': '32'}, 
         {'name': 'David', 'job': 'Project Manager', 'age': '33'}, 
         {'name': 'Bob', 'job': 'Software Engineer', 'age': '27'}, 
         {'name': 'Chris', 'job': 'System Administrator', 'age': '30'}]
         
    >>> sorted(lst_people, key=itemgetter("age"))
        [{'name': 'Bob', 'job': 'Software Engineer', 'age': '27'}, 
         {'name': 'Chris', 'job': 'System Administrator', 'age': '30'}, 
         {'name': 'Alice', 'job': 'Computer Science', 'age': '32'}, 
         {'name': 'David', 'job': 'Project Manager', 'age': '33'}]
         
    >>> sorted(lst_people, key=lambda x: x["age"])
        [{'name': 'Bob', 'job': 'Software Engineer', 'age': '27'}, 
         {'name': 'Chris', 'job': 'System Administrator', 'age': '30'}, 
         {'name': 'Alice', 'job': 'Computer Science', 'age': '32'}, 
         {'name': 'David', 'job': 'Project Manager', 'age': '33'}]
    ```
  - 搭配排序相关方法（如**sorted()**）的入参**key**使用，指定列表中**元组**的排序逻辑。**key=itemgetter(index)** 功能等价于 **key=lambda x: x\[index]**:
    ```bash
    >>> lst_people = [('Alice', 'Computer Science', '32'), 
                      ('Bob', 'Software Engineer', '27'), 
                      ('Chris', 'System Administrator', '30'), 
                      ('David', 'Project Manager', '33')]
                      
    >>> from operator import itemgetter
         
    >>> sorted(lst_people, key=itemgetter(1))
        [('Alice', 'Computer Science', '32'), 
         ('David', 'Project Manager', '33'), 
         ('Bob', 'Software Engineer', '27'), 
         ('Chris', 'System Administrator', '30')]
         
    >>> sorted(lst_people, key=itemgetter(2))
        [('Bob', 'Software Engineer', '27'), 
         ('Chris', 'System Administrator', '30'), 
         ('Alice', 'Computer Science', '32'), 
         ('David', 'Project Manager', '33')]

    >>> sorted(lst_people, key=lambda x: x[2])
        [('Bob', 'Software Engineer', '27'), 
         ('Chris', 'System Administrator', '30'), 
         ('Alice', 'Computer Science', '32'), 
         ('David', 'Project Manager', '33')]
    ```
  - 在排序方法中，指定多个index的排序优先级（多级排序）。**key=itemgetter(index_1, index_2, index_3)** 功能等价于 **key=lambda x: (x\[index_1], x\[index_2], x\[index_3])**：
    ```bash
    >>> lst_people = [('Alice', 'Computer Science', '27'), 
                      ('Bob', 'Software Engineer', '27'), 
                      ('Chris', 'System Administrator', '30'), 
                      ('David', 'Project Manager', '30'), 
                      ('David', 'Algorithm Engineer', '30')]
                      
    >>> from operator import itemgetter
             
    >>> sorted(lst_people, key=itemgetter(2,0,1))
        [('Alice', 'Computer Science', '27'), 
         ('Bob', 'Software Engineer', '27'), 
         ('Chris', 'System Administrator', '30'), 
         ('David', 'Algorithm Engineer', '30'), 
         ('David', 'Project Manager', '30')]
    
    >>> sorted(lst_people, key=lambda x: (x[2], x[0], x[1]))
        [('Alice', 'Computer Science', '27'), 
        ('Bob', 'Software Engineer', '27'), 
        ('Chris', 'System Administrator', '30'), 
        ('David', 'Algorithm Engineer', '30'), 
        ('David', 'Project Manager', '30')]
    ```
    
- 具名元组：
  - **namedtuple()**: 通过构造一个带字段名的元组，方便理解、查找元组内部指定含义的数据。namedtuple(typename, field_names, verbose=False, rename=False)，其中typename为元组名称，field_names为元组中元素的名称，verbose默认，若元素名称中含有Python关键字，则须设置rename=True。构建具名元组有两种方法，常规方法如下：
    ```bash
    >>> from collections import namedtuple
    >>> Person = namedtuple("Person", ["name", "job", "age"])
    >>> one_person = Person(name="Alice", job="Computer Science", age="27")
    >>> one_person
        Person(name='Alice', job='Computer Science', age='27')
    >>> print(one_person.name, " is ", one_person.age)
        Alice  is  27
    ```
  - 构建具名元组的另一种方法，涉及使用._make:
    ```bash
    >>> from collections import namedtuple
    >>> Person = namedtuple("Person", "name job age")
    >>> one_person = Person._make(["Alice", "Computer Science", "27"])
    >>> one_person
        Person(name='Alice', job='Computer Science', age='27')
    >>> print(one_person.name, " is ", one_person.age)
        Alice  is  27
    ```
  - 构建嵌套具名元组：
    ```bash
    >>> from collections import namedtuple
    >>> Birth_info = namedtuple("Birth", "month day")
    >>> Person = namedtuple("Person", "name job age birth")
    >>> birth_info = Birth_info(month="09", day="13")
    >>> one_person = Person(name="Alice", job="Computer Science", age="27", birth=birth_info)
    >>> one_person
        Person(name='Alice', job='Computer Science', age='27', birth=Birth(month='09', day='13'))
    >>> print(one_person.name, "'s birthday is ", one_person.birth.month, "-", one_person.birth.day)
        Alice 's birthday is  09 - 13
    ```  

- **attrgetter()**: 根据元组的某个字段（key）给元组列表排序，支持嵌套。
  ```bash
  >>> lst_people = [('Alice', 'Computer Science', '27', ('09', '13')), 
                    ('Bob', 'Software Engineer', '27',  ('08', '06')), 
                    ('Chris', 'System Administrator', '30', ('03', '16')), 
                    ('David', 'Project Manager', '30', ('04', '15')), 
                    ('David', 'Algorithm Engineer', '30', ('11', '27'))]

  >>> from collections import namedtuple
  >>> Birth_info = namedtuple("Birth", "month day")
  >>> Person = namedtuple("Person", "name job age birth")
  >>> people_info = [Person(name, job, age, Birth_info(month, day)) for name, job, age, (month, day) in lst_people]

  >>> from operator import attrgetter
  >>> check_one = attrgetter("name", "job", "age", "birth.month")
  >>> for person_now in sorted(people_info, key=attrgetter("age")):
  ...     print(check_one(person_now))
  ... 
      ('Alice', 'Computer Science', '27', '09')
      ('Bob', 'Software Engineer', '27', '08')
      ('Chris', 'System Administrator', '30', '03')
      ('David', 'Project Manager', '30', '04')
      ('David', 'Algorithm Engineer', '30', '11')
  ``` 
