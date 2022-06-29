### IsX操作
- **isdigit()**: 检测字符串是否只由数字组成，返回True或False。
    ```bash
    >>> "1234567890".isdigit()
    True
    >>> "12345-67890".isdigit()
    False
    >>> "1234五六7890".isdigit()
    False
    ```
- **isalpha()**: 检测字符串是否只由字母组成，返回True或False。
    ```bash
    >>> "abcdefg".isalpha()
    True
    >>> "aBcDeFg".isalpha()
    True
    >>> "abc0efg".isalpha()
    False
    >>> "abcd efg".isalpha()
    False
    ```
- **isalnum()**: 检测字符串是否只由字母和数字组成，返回True或False。
    ```bash
    >>> "abcdefg".isalnum()
    True
    >>> "1234567".isalnum()
    True
    >>> "1a3b5c7".isalnum()
    True
    >>> "1a3b 5c7".isalnum()
    False
    >>> "1a3b-5c7".isalnum()
    False
    ```  
- **isupper()**: 检测字符串中所有字母是否都为大写，返回True或False。 
- **islower()**: 检测字符串中所有字母是否都为大写，返回True或False。 
- **upper()**: 将字符串中的小写字母转为大写字母。
- **lower()**: 将字符串中的大写字母转为小写字母。
