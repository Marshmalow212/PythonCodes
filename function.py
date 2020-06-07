def s1(a1):
	print("This is from s1",a1)
def s2(a):
	b = a * 2
	c = b + 1
	return c + 100000

x = input('Number? ')
x = int(x)
s1(x)

ans = s2(x)

print("Ans",ans)
