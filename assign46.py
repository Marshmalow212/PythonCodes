def computepay(a,b):
	if h<=40: return a*b

	else:
		return ((a - 40)*(b*1.5))+(40 * b)


h = input('Enter hour: ')
r = input('Enter rate per hour: ')

h = float(h) 
r = float(r)

print("Pay",computepay(h,r))



