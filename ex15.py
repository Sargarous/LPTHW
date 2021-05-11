#this line import argument value, arguments of command line we transger so script
from sys import argv
#there wo define two arg of argv, scriptname is one of them
script, filename = argv
#create txt variable and add text from file as value
# txt = open(filename)
# #just print filename and read string from our txt var
# print(f"Here's your file {filename}:")
# print(txt.read())
#input my filemane again
print("Type the filename again:")
file_again = input('> ')
#create another var for text form file
txt_again = open(file_again)
#print text through read command
print(txt_again.read())
