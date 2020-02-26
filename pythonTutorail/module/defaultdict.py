from collections import defaultdict
# 讓mydict的預設為整數0，也可以是list()=[],dict()={},
mydict = defaultdict(int)
mydict['name'] = 1

print(mydict['age'])
print(mydict['name'])
print(mydict)


# 也可以自己訂
def noIdea():
    return 'Huh'

mydict2 = defaultdict(noIdea)
mydict2['name'] = 1
print(mydict2['age'])
print(mydict2['name'])
print(mydict2)

# 訂法2
mydict3 = defaultdict(lambda : 'hahaha')

mydict3['name'] = 1
print(mydict3['age'])
print(mydict3['name'])
print(mydict3)
