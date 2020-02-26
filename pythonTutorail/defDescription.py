def echo(anything):
    'echo return its input argument'
    return anything

def print_if_check(thing, check):
    '''
    print the first argument if a second argument is true.
    The operation is:
        1.Check whether the *second* argument is true.
        2.If it is, print the *first* argument
    '''
    if check:
        print(thing)


print_if_check('HI hello world',True)
echo('HiHiHi')

help(print_if_check)
print(print_if_check.__doc__)