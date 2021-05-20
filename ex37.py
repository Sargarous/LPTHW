#python keywords examples
#and
print(True and False)
#with as(work with files, always close after)
with open("ex16_test.txt", 'r') as file:
    print(file.read())
    flag = False
#True or error
# assert flag, "False!"
#while
i = 0
while not flag:
    i += 1
    if i == 3:
        print(i)
        break
#class
class Dog(object):

    def __init__(self, breed, color, weight):
        self.breed = breed
        self.color = color
        self.weight = weight

    def bark(self):
        return "Barking"
    def sleep(self):
        return "Sleeping"

if __name__ == "__main__":
    dog_hound = Dog("Dog hound", "brown", 15)
    wolf_hound = Dog("Wolf hound", "gray", 53)
    print(dog_hound.breed, dog_hound.color, dog_hound.weight, dog_hound.bark())
    print(wolf_hound.breed, wolf_hound.color, wolf_hound.weight, wolf_hound.sleep())

#def and continue
def cont(i):
    for x in range(1, 10):
        i += 2
        if x%2 == 0:
            continue
        print(f"  {x-1} skipped")
        print(x)
cont(0)
#del
lst = [1, 2, 4, 5]
del lst[2]
print(lst)
#except and finally
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Emergency alert!")
    finally:
        print(1 + 1)
#exec
i = 3
exec('i = 10')
print(i)
#
