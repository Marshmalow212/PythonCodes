#Open the file mbox-short.txt
#find a line that starts with 'From '
#You will parse the From line using split() and print out the second word 

f = open("mbox-short.txt",'r')

mail=list()

for l in f:
	if l.startswith('From'):
		ln = l.split()
		if 'From:' not in ln:
			mail.append(ln[1])
for i in mail:
	print(i)
print("There were", len(mail), "lines in the file with From as the first word")				
