#read through the mbox-short.txt 
#figure out the distribution by hour of the day
#finding the time and then splitting the string a second time using a colon.
#the counts for each hour, print out the counts, sorted by hour  


f = open("mbox-short.txt",'r')

mail=dict()

for l in f:
	if l.startswith('From'):
		le = l.split()
		if 'From:' not in le:
			ln = le[5].split(':')
			mail[ln[0]] = mail.get(ln[0],0) + 1

it = sorted(mail.items())
for k,v in it:
	print(k,v)


