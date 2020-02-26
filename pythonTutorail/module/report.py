def get_description():
    """ Return random weather, just like the pros """
    from random import choice
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who know']
    return choice(possibilities)