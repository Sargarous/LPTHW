people = 100
cars = 40
trucks = 50

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't secide.")

if people > trucks:
    print("Alright, let's just  take the trucks.")
else:
    print("Fine, let's stay home then.")

if people > trucks and cars < people:
    print("Anyway, people more than rest of both")
