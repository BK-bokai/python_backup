animal = 'Dog'

# 他為往上一層去找animal
def print_global():
    print('inside print_global:',animal)

print_global()
print('at top level:', animal)

# 若想在函式中取得環境變數並更改她，會產生錯誤
def change_and_print_global():
    # print('inside change_and_print_global:',animal) #所以你不能取得globe變數在改變他，只能創造依樣名稱的變數，但行動範圍僅限函式內
    animal = 'Cat'
    print('After the change:',animal)
change_and_print_global()

def change_local():
    animal = 'Cat'
    print('inside change_local:',animal,id(animal)) #每個變數都有獨一無二的id
change_local()
print('at top level:', animal,id(animal))

#*************************************************************************************

#global
print(animal)
def change_and_print_global():
    global animal
    animal = 'lion'
    print('inside change and print global:', animal)
change_and_print_global()
print(animal)

#globals 與 locals會返回字典形式全域及Local的變數
def print_locals():
    animal = 'lion'
    print('locals:', locals())
print_locals()
print('globals:',globals())
