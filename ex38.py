ten_things = "Apples Oranges Crows Telephone Light Sugar"
print(ten_things)
print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
            "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff))

lst = []
lst.append("Ex")
lst.extend(ten_things)
lst.insert(3, "Dread")
lst.remove("Apples")
#delete index 0 value and return it, Ex no more
print(lst.pop([0]))
#return 1st "Oranges" in list from ind 0 till len-1 or any other
lst.list.index("Oranges",[0[,(lst.len-1)]])
lst.count(x)
