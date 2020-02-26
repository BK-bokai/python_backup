def knights(saying):
    def inner():
        return "We are the Knights who says : '%s' " % saying
    return inner

a = knights('HiHiHi')

print(type(a))#此時a的type是function 我們稱為閉包，而不是str
print(a())