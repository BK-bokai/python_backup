class person():
    def __init__(self,input_name):
        self.hidden_name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter
    def name(self,input_name):
        print('inside the setter')
        self.hidden_name = input_name

        
Aaron = person('Aaron')
# set 
Aaron.hidden_name = 'perla'#你可以直接存取物件內部的屬性
Aaron.name = 'perla'#你也可以使用你賦與name屬性的特性

# get
print(Aaron.hidden_name)#你可以直接存取物件內部的屬性
print(Aaron.name)#你也可以使用你賦與name屬性的特性