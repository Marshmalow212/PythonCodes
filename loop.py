def whileloop(a):
	print('starting while loop')
	while a>=0:
		print(a)
		a-=1
	print('end while loop\n')

def forloop(a):
	print('starting for loop')
	for i in range(0,a):
		print(i)
	print('end for loop\n')


n = input("Enter a number for starting loops: ")
whileloop(int(n))
forloop(int(n))

a = [1,2,3,4,5]
print('Printing from int array')
for i in a:
	print(i)

