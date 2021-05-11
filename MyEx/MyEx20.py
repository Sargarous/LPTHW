#write 3 like of text and read first 12 lines from txt file
from os.path import exists

#wrighter
def file_writer(file_name, text):
    open(file_name, 'a').write(f"\n{text}")
#reader line-by-line 12 times
def line_reader(file):
    x = 0
    current_file = open(file)
    while(x != 12):
        line_number = x
        print(line_number, current_file.readline())
        x += 1

print("Enter name of file for wrighting:")
file_name = input('> ')
#verify file name
while(not exists(file_name)):
    print("Incorrect file name, please try again.")
    file_name = input('> ')
#add 3 string line at the end of file from new line
else:
    print("Wright your text below: ")
    x = 0
    while(x != 3):
        text = input('> ')
        file_writer(file_name, text)
        x += 1
    print("Done!")

#just call reader method
print("Type file to read: ")
file_to_read = input('> ')
line_reader(file_to_read)
