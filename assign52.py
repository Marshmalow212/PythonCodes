#5.2 Write a program that repeatedly prompts a user for integer numbers 
#until the user enters 'done'. Once 'done' is entered, print out the 
#largest and smallest of the numbers. If the user enters anything other 
#than a valid number catch it with a try/except and put out an appropriate 
#message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

def store(n,a,b):
	if a is None:
		a = n
		b = n
	elif n<a:
		a=n
	elif n>b:
		b=n
	return a,b

lg = -1
sl = None


while True:
	data = input('Enter value: ')
	
	if data == 'done': break

	else:
		try:
			data = int(data)
			sl,lg = store(data,sl,lg)
		except:
			print('Invalid input')
		
print('Maximum is',lg)
print('Minimum is',sl)
