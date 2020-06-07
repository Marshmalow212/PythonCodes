h = input('Enter hour: ')
r = input('Enter rate per hour: ')

h = float(h) 
r = float(r)
if h<=40:
	p = h * r
	print(p)
else:
	p = ((h - 40)*(r*1.5))+(40 * r)
	print(p)

