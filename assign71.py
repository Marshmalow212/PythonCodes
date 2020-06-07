#7.1 Write a program that prompts for a file name, then opens that file and 
#reads through the file, and print the contents of the file in upper case. 
#Use the file words.txt to produce the output below.
fname = input("Enter the file name: ")

data = open(fname,'r')

for line in data:
	line = line.rstrip()
	print(line.upper())