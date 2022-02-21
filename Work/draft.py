

def name_first(species, name, **lines):
	pet = {}
	pet['species'] = species
	pet['name'] = name
	for key, value in lines.items():
		pet[key] = value
	return pet
my_pet = name_first('Huski', 'Koshka', color='White', age=2)
print(my_pet)

def print_tree(n):
	for i in range(n):
		for j in range(n - i):
			print(' ', end='')
		for k in range(2*i + 1):
			print('*',end='')
		print()

print_tree(4)
