#Write a program to read through the mbox-short.txt
#greatest number of mail messages. 
#looks for 'From ' lines and takes the second word
#count of the number of times they appear in the file. 
#find the most prolific committer


f = open("mbox-short.txt",'r')

mail=dict()

for l in f:
	if l.startswith('From'):
		ln = l.split()
		if 'From:' not in ln:
			#mail.append(ln[1])
			mail[ln[1]] = mail.get(ln[1],0) + 1
			
word = None
cnt = None
for k,v in mail.items():	
	if word is None or v>cnt:
		word = k
		cnt = v

print(word,cnt)	 