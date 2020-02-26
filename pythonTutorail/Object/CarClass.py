class car():
    def __init__(self,country):
        self.country = country
        print('Im a car') # 建構式

    def exclaim(self):
        print('Im from {}'.format(self.country))
    
GiveMeCar = car('TW')
GiveMeCar.exclaim()

# 繼承
class Yugo(car):
    def __init__(self,country):# 覆蓋父類別的建構式
        super().__init__(country)# 呼叫父類別 self.country = country
        print('Im a Yugo Car')


GiveMeYugo = Yugo('Tw')
GiveMeYugo.exclaim() #繼承了父類別的方法
    
