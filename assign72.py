#.....X-DSPAM-Confidence:    0.8475
#...when you are testing below enter mbox-short.txt as the file name.

fname = input("Enter the file name: ")

data = open(fname,'r')
d = 0.0
c = 0
for line in data:
	line = line.rstrip()
	if line.startswith("X-DSPAM-Confidence:"):
		s = line
		pos = line.find('0')
		s = line[pos:]
		d += float(s)
		c += 1
print("Average spam confidence:",(d/c))

	