countries = ['Ukraine', 'Belarus', 'France', 'Germany',
             'Estonia', 'Finland', 'Poland', 'Serbia']

name = {'name': 'Sweden',
        'capital': 'Stockholm',
        'largest_cities': ['Stockholm', 'Kherson', 'Malmo']}

name.update({'pop': 1_000_000, 'land': 'fasd'})
print(name)
name['name'] = 'Ihor'
print(name)
del name['name']
print(name)

countries = {'Ukraine': 1, 'Belarus': 2,
             'France': 3, 'Germany': 4,
             'Estonia': 5, 'Finland': 6,
             'Poland': 7, 'Serbia': 8}

countries = ['Ukraine', 'Belarus', 'France', 'Germany',
             'Estonia', 'Finland', 'Poland', 'Serbia']

me_key = ['ukr', 'bel', 'fra', 'ger', 'est', 'finl', 'pol', 'ser']

new_key = {me_key[x]: countries[x] for x in range(len(countries))}
print(new_key)

sevens = [i for i in range(71) if i % 5 == 0]
print(sevens)

d = [i for i in range(1, 11)]
countries = ['Ukraine', 'Belarus', 'France', 'Germany',
             'Estonia', 'Finland', 'Poland', 'Serbia',
             'Russia', 'Italy']
dict1 = [(x, countries[d.index(x)]) for x in d]
dict_main = dict(dict1)
print(dict_main)