class num():
    def __init__(self,num):
        self.num = num
    
    def __eq__(self,num):
        return self.num == num.num

Anum = num(15)
Bnum = num(16)
Cnum = num(15)

print(Anum == Bnum)
print(Anum == Cnum)