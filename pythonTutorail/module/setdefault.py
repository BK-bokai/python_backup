myDict = {
    'name':'Aaron',
    'age' :'25',
    'like':'sport'
}

print(myDict)

#如果今天取得的字典裡沒有的鍵可以使用setdefault()，當找不到鍵他會給他一組預設
city = myDict.setdefault('city','Taipei')
print(myDict)

#若已經有資料則不會去更改她
age = myDict.setdefault('age','200')
print(myDict)