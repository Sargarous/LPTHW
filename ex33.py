def list_filler (count, inc):
    i = 0
    increminator = int(inc)
    numbers = []
    count = int(count) + 1
    numbers = range(0, count, increminator)
    # while i < count:
    #     print(f"At the top i is {i}")
    #     numbers.append(i)
    #
    #     i += increminator
    #     print("Numbers now: " , numbers)
    #     print(f"At the bottom i is {i} \n")
    #
    print("The numbers: ")

    for num in numbers:
        print(num)

print("Input last number in list: ")
hi_number = input()
print("Input increment: ")
list_filler(hi_number, input())
