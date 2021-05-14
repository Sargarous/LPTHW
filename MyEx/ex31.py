#if-else calc
flag = True

while flag:
    print("Enter first value: ")
    v1 = input("> ")
    print("Enter operator: ")
    operat = input("> ")
    print("Enter second value: ")
    v2 = input("> ")

    val1 = int(v1)
    val2 = int(v2)

    if operat == "+":
        print(val1 + val2)
    elif operat == "-":
        print(val1 - val2)
    elif operat == "*":
        print(val1 * val2)
    elif operat == "/":
        print(val1 / val2)
    else:
        print("Something went wrong! Try again!")

    print("Do you want to continue? Just press enter! Or write something and press enter to EXIT.")
    quiter = input(" ")
    if len(quiter) > 0:
        flag = False
