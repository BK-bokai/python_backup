import string
import re

# 存取內建ASCII碼，共100個
printable = string.printable
print(len(printable))

# \d、\D數字及非數字
print('----------------數字非數字---------------')
m = re.findall('\d',printable) #數字
print(m)
m = re.findall('\D',printable) #非數字
print(m)

# \w，\W英數字及非英數字
print('----------------英數字及非英數字---------------')
m = re.findall('\w',printable)
print(m)
m = re.findall('\W',printable)
print(m)

# \s，\S空白及非空白
print('----------------空白及非空白---------------')
m = re.findall('\s',printable)
print(m)
m = re.findall('\S',printable)
print(m)

# \b，\B 單字及非單字
print('----------------單字及非單字---------------')
m = re.findall(r'(\b)',printable)
print(m)
m = re.findall('\B',printable)
print(m)