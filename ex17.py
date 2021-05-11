from sys import argv
import math
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

indata = open(from_file).read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output fiLe exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to aboart.")
input()

out_file = open(to_file, 'w').write(indata)


print("Alright, all done.")
print(math.e)
