import re

source = 'Young Aaron'
m = re.search('Aaron',source)
if m:
    print(m.group())

