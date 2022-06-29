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
