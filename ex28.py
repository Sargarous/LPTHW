def result_or(a, b):
    print(f" >{a} or {b}< ", end = " "),
    return(a or b)

def result_and(a, b):
    print(f" >{a} and {b}< ", end = " "),
    return (a and b)

def result_equals(a, b):
    print(f" >{a} == {b}< ", end = " "),
    return(a == b)

def result_not(a, b):
    print(f" >{a} != {b}< ", end = " ")
    return(a != b)


print(result_and(True, True))
print(result_and(False, True))
print(result_and(result_equals(1, 1), result_not(2, 1)))
print(result_equals("test", "test"))
print(result_or(result_equals(1, 1), result_not(2, 1)))
print(result_and(True, result_equals(1, 1)))
print(result_or(True, result_equals(1, 1)))
print(result_equals("test", "testing"))
print(result_and(result_not(1, 0), result_equals(2, 1)))
print(result_not("test", "tisting"))
print(result_equals("test", 1))

print(not(result_and(True, False)))
print(not(result_and(result_equals(1, 1), result_not(0, 1))))
print(not(result_or(result_equals(10, 1), result_equals(1000, 1000))))
print(not(result_or(result_equals(10, 1), result_equals(3, 4))))
print(not(result_and(result_equals("testing", "testing"), result_equals("Zed", "Cool Guy"))))

print(result_and(result_equals(1, 1), (not(result_or(result_equals("testing", 1), result_equals(1, 0))))))
print(result_and(result_equals("chunky", "bacon"), (not(result_or(result_equals(3, 4), result_equals(3, 3))))))
print(result_and(result_equals(3, 3), (not(result_or(result_equals("testing", "testing"), result_equals("Python", "Fun"))))))


# 1. True and True
# 2. False and True
# 3. 1 == 1 and 2 == 1
# 4. "test" == "test"
# 5. 1 == 1 or 2 != 1
# 6. True and 1 == 1
# 7. False and 0 != 0
# 8. True or 1 == 1
# 9. "test" == "testing"
# 10. 1 != 0 and 2 == 1
# 11. "test" != "testing"
# 12. "test" == 1
#
# 13. not (True and False)
# 14. not (1 == 1 and 0 != 1)
# 15. not (10 == 1 or 1000 == 1000)
# 16. not (1 != 10 or 3 == 4)
# 17. not ("testing" == "testing" and "Zed" == "Cool Guy")
#
# 18. 1 == 1 and (not ("testing" == 1 or 1 == 0))
# 19. "chunky" == "bacon" and (not (3 == 4 or 3 == 3))
# 20. 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))
