import re

source = 'Young Aaron'
# 會回傳一個list，顯示n出現過幾次
m = re.findall('n',source)
print(m)
if m :
    print('Found', len(m), 'matches')

# 會回傳一個list，顯示n出現過幾次，並顯示n後面的字元
# 但由於最後一個n後面沒字元所以只匹配到1個n
m = re.findall('n.',source)
print(m)
if m :
    print('Found', len(m), 'matches')

# 在.c後面加?代表後面字元部必要
m = re.findall('n.?',source)
print(m)
if m :
    print('Found', len(m), 'matches')