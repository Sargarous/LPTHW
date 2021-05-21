import copy

ten_things = "Apples Oranges Crows Telephone Light Sugar"
print(ten_things)
print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
            "Corn", "Banana", "Girl", "Boy"]
X = [1 , 3]
# while len(stuff) != 10:
#     next_one = more_stuff.pop()
#     print("Adding: ", next_one)
#     stuff.append(next_one)
#     print(f"There are {len(stuff)} items now.")
#
# print("There we go: ", stuff)
#
# print("Let's do some things with stuff.")
#
# print(stuff[1])
# print(stuff[-1])
# print(stuff.pop())
# print(' '.join(stuff))
# print('#'.join(stuff))

lst = more_stuff[:]
lst.append("Ex")
lst.extend(X)
lst.insert(3, "Dread")
print(f"lst ---> {lst}")

lst.remove("Banana")
#delete index 0 value and return it, Ex no more
print(lst.pop(0))
#return 1st "Oranges" in list from ind 0 till len-1 or any other
lst.index("Girl",0,(len(lst)))
#return quantity of (x) elements in list
lst.count("Light")
#reverce - turn list back to front
lst.reverse()
#deepcopy (acrual, not just ref)
print(f"lst ---> {lst}")
new_lst = lst
new_copied_lst = copy.deepcopy(more_stuff)
print(f"new lst = lst ---> {new_lst}")
print(f"new_lst.copy(lst) ---> {new_copied_lst}\n")
print("pop(0) from lst", lst.pop(0))
print(f"\nnew lst ---> {new_lst}")
print(f"new_lst.copy(lst) ---> {new_copied_lst}")
#clear
new_copied_lst.clear()
print(f"new lst clear() ---> {new_copied_lst}")
