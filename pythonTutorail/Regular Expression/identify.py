# 模式          匹配
# abc           找出abc
# (abc)         找出abc
# ab|cd         找出ab或cd
# .             找出除了\n以為的任何字元(\n是換行)
# ^abc          找出abc開頭的字
# abc$          找出abc結尾的字
# abc?          找出0個或多個abc
# abc*          找出0個或多個abc(越多越好)
# abc*?         找出0個或多個abc(越少越好)
# abc+          找出1個或多個abc(越多越好) 
# abc-          找出1個或多個abc(越少越好)
# abc{m}        找出m個連續的abc
# abc{m, n}     找出m~n個連續的abc(越多越好)
# abc{m, n}?    找出m~n個連續的abc(越少越好) 
# [abc]         等於a|b|c
# [^abc]        不含abc字串
# abc(?= next)  找出abc且他後面有next
# abc(?! next)  找出abc且他後面沒有next
# (?<= abc)next 找出next且他前面匹配abc
# (?<! abc)next 找出next且他前面不是abc

import re
source = """III I wish I may, I wish I might...Have a dish of fish tonight. I I I""" 

m = re.findall('wish',source)
print(m)

m = re.findall('(wish)',source)
print(m)

m = re.findall('wish|I',source)
print(m)

m = re.findall('.',source)
print(m)

m = re.findall('^I',source)
print(m)

m = re.findall('to.*$',source)
print(m)

m = re.findall('I ?',source)
print(m)

m = re.findall('I *',source)
print(m)

m = re.findall('wish.*?',source)
print(m)

m = re.findall('wish+',source)
print(m)

m = re.findall('wish+?',source)
print(m)

m = re.findall('I{3}',source)
print(m)

m =re.findall('I{2,4}',source)
print(m)

m =re.findall('I{2,3}?',source)
print(m)

m = re.findall('[wish I]',source)
print(m)

m = re.findall('[^ wish I]',source)
print(m)

m = re.findall('I (?=wish)',source)
print(m)

m = re.findall('I(!=wish)',source)
print(m)

m = re.findall('(?<=I) wish',source)
print(m)

m = re.findall('(?<! I) wish',source)
print(m)