regions = {}
cities = {}

regions['Gomelskaya'] = 'Gomel'
regions['Brestskaya'] = 'Brest'
regions['Vitebskaya'] = 'Vitebsk'
regions['Grodnenskaya'] = 'Grodna'

cities['Gomelskaya'] = 'Shklov'
cities['Brestskaya'] = 'Borisov'
cities['Vitebskaya'] = 'Kerch'
cities['Grodnenskaya'] = 'Bobrujsk'

print('-' * 10)

for citie, region in list(cities.items()):
     print(f"{cities} in {region}")

print('-' * 10)
for state, sitie in list(cities.items()):
    print(f"{sitie}===>{regions[state]}")


reg2 = regions.copy()
print(reg2)
#get value by key
print(regions.get('Grodnenskaya'))
#list of key-val
print(reg2.items())
#list of keys
print(reg2.keys())
#delete keys and return val
print(reg2.pop('Vitebskaya'))
print(regions)
#delete and return key-val
print(reg2.popitem())
#add new or rewrite key-val/key/val (add one dict to another)
reg2.update(Gomelskaya = 'Gnom')
reg2.update(Gnom = 'Gnom')
print("update Gnom", reg2)
reg2.update(cities)
print("update citie", reg2)
#ckear
reg2.clear()
print("clear", reg2)
