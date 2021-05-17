import random
#ptint animals from list in random order
animals = ['Bear', 'Python', 'Peacock', 'Kangoo', 'Whale']
printed_ind = []
count = len(animals)
while count > 0:
    rand_animal = random.randint(0, 4)
    if not rand_animal in printed_ind:
        print(f"{animals[rand_animal]} under index {rand_animal} in our list")
        printed_ind.append(rand_animal)
        count -= 1
