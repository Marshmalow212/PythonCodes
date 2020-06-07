#split the line into a list of words using the split() method. 
#check to see if the word is already in the list and if not append it
#Open the file romeo.txt

f = open("romeo.txt",'r')
word = list()

for l in f:
	li = l.split()
	for w in li:
		if w not in word:
			word.append(w)

word.sort()
print(word)
			
		