from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you din't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")
print("Opening the file...")
#open file (w - for wrighting, will be truncated  first)
target = open(filename, 'w')
#clear all data in file
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")
#simple input x3
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
#write each input (\n - form new line)
target.write(f"{line1}\n{line2}\n{line3}")
#close file(save&quit)
print("And finally, we close it.")
target.close()
