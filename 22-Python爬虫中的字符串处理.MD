## python 爬虫中的字符串处理 
### 去除字符串中的空白字符 
（1）空白字符位于左右两边 
```python
demo_str = '    Lfuruiyang'
ret1 = demo_str.lstrip()
print(demo_str) 
print(ret1) 
```
(2) 空白字符在中间 
```python
# 空白字符在中间 
import re

demo_str = '  Lfuru   iyang   '
ret1 = re.sub('\s', '', demo_str)
print(demo_str)
print(ret1)
```

### 去除字符串中的指定字符 
- string.strip(s), s 是一个序列，在 string 的两边删除 string 中在序列 s 中的字符
- string.lstrip(s), 在 string 的左边删除 string 中在序列 s 中的字符
- string.rstrip(s), 在 string 的右边删除 string 中在序列 s 中的字符
```python
# 去除在给定序列中的字符 
demo_str = 'Lfuruiyang'
ret1 = demo_str.lstrip("Lfuryy")
print(demo_str)
print(ret1)

# 去除指定字符 
import re

demo_str = """  Lfuru iyang  "hello"  'pig'  """
# ret1 = re.sub(['\"', '\'', '\s'], '', demo_str)     # error
demo_str = re.sub('\"', '', demo_str)
print(demo_str)
demo_str = re.sub('\'', '', demo_str)
print(demo_str)
demo_str = re.sub('\s', '', demo_str)
print(demo_str)
```

### 常见用法 




