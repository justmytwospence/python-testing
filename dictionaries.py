import doctest
from collections import defaultdict
from pprint import pprint

bad_guys = {
    "daredevil": "kingpin",
    "x-men": "apocalypse",
    "batman": "bane",
}
bad_guys['deadpool'] = 'evil deadpool'
bad_guys['x-men'] = 'juggernaut'

my_profile = {}
my_profile['fname'] = 'Paul'
my_profile['lname'] = 'Mealus'
my_profile['city'] = 'San Diego'
my_profile['past_jobs'] = ['analyst', 'sandwich', 'engineer']
my_profile['transportation'] = {
    'skateboard': 'fun',
    'bike': 'work'
}

d1 = {
    'a': 'robin',
    'b': 'galahad',
}

d2 = {
    'b': 'black knight',
    'c': 'rabbit',
    'd': 'shrubbery',
}

d1.update(d2)

if __name__ == "__main__":
    doctest.testmod()
    bad_guys.update(**{'x-men': 'magneto'})
    pprint(bad_guys)
    pprint(d1)
