# decorator 修改既有的函式，但不想更改原本的程式碼

# decoratorNo1
def document_it(func):
    def new_funciton(*args,**kwargs):
        print('Running function',func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
    return new_funciton
# decoratorNo2
def square_it(func):
    def new_funciton(*args,**kwargs):
        result = func(*args,**kwargs)
        return result * result
    return new_funciton

# 使用方法01
def add_ints(a,b):
    return a+b

cooler_add_ints = document_it(add_ints)
cooler_add_ints(9,10)

# 使用方法02 good
@document_it
def add2_ints(a,b):
    return a+b

add2_ints(11,10)

# 會先執行離自己最接近的decorator
@document_it
@square_it
def add3_ints(a,b):
    return a+b
add3_ints(14,15)

