def edit_story(words,func):
    for word in words:
        print(func(word))

stair = ['thun','meow','thud','hiss']
def enliven(word):
    return word.capitalize() +'!'

edit_story(stair,enliven)

# 匿名函式
edit_story(stair,lambda word: word.capitalize() + '!')