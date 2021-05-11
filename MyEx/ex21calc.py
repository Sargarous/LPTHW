import ast
#method for evaluation string (2+2 etx)
def calc(f):
    return ast.literal_eval(f)

print("Follow the instructions: ")
print("Print evaluation (for example 2+2)): ")
string = input('> ')

# print("Print math sign: ")
# math_sign = input('> ')
#
# print("Print second value: ")
# second = float(input('> '))

print(calc(string))
