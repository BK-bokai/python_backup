import re

source = 'Young Aaron'

# ---結果一樣
print(source.replace('n','?'))

m = re.sub('n','?',source)
print(m)
# ----------
# 但re可以用正規表示法
m = re.sub('n.','?',source)
print(m)