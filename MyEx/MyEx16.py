# from sys import argv
#
# script = argv

print("Enter filename to rewrite")
filename = input('>>> ')
print(f"Clear {filename} from previous data, ok?")
input("?> ")
target = open(filename, 'w')

print(f"Whath do you want to write in {filename}?")
text = input()

target.write(text)

print(f"{text} is writed to the file")

target.close()

print(f"{filename} saved and closed")

print("Enter name of file to read")
file_reader = input('> ')

file_data = open(file_reader)

print(file_data.read())

file_data.close()
