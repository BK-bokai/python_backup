class person():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
    name = property(get_name,set_name)

Aaron = person('Aaron')


# set 
Aaron.hidden_name = 'perla'#你可以直接存取物件內部的屬性
Aaron.set_name('perla')#你也可以使用你定義的set方法
Aaron.name = 'perla'#你也可以使用你賦與name屬性的特性

# get
print(Aaron.hidden_name)#你可以直接存取物件內部的屬性
print(Aaron.get_name())#你也可以使用你定義的get方法
print(Aaron.name)#你也可以使用你賦與name屬性的特性



