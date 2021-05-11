#There we call func
formatter = "{} {} {} {}"
#set values for our fumc, more values than declared in func dont do anything
print(formatter.format(1, 2, 3, 4, 5))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter,  formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
