import re
mstart = re.match('^You','Young Aaron')
m = re.match('You','Young Aaron')
Aaron = re.match('Aaron','Young Aaron')
if m:
    print(m.group())
if mstart:
    print(mstart.group())

# match 只會在模式位於來源開頭時才生效

if Aaron:
    print(Aaron.group())

#解決 .是所有字元包含空白，*代表任何數量,.*代表模式會匹配模式前任和數量與字元的來源
Aaron = re.match('.*Aaron','Young Aaron')
if Aaron:
    print(Aaron.group())