f = open("mbox-short.txt",'r')

mail=dict()

for l in f:
	if l.startswith('From'):
		ln = l.split()
		if 'From:' not in ln:
			#mail.append(ln[1])
			mail[ln[1]] = mail.get(ln[1],0) + 1
print("---------Items from dict()\n")			
for k,v in mail.items():
	print(k,'-',v)
print("----------------------")

item = mail.items()#[(k,v) for k,v in mail.items()]
print(item)
print("--------Dictionary to tuples\n")
for k,v in item:
	print(k,'-',v)
print("----------------------")

item = mail.items()#[(k,v) for k,v in mail.items()]
print(item)
print("--------tuples simple sort\n")

item =sorted( item)
print(item)
for k,v in item:
	print(k,'-',v)
print("----------------------")




tup = sorted( [(v,k) for k,v in mail.items()])

print(tup)
print("---------Items sort v,k\n")
for v,k in tup:
	print(v,'-',k)                           
print("----------------------")
tup = sorted(tup,reverse = True)
print(tup)
print("---------Items reverse sort v,k\n")
for v,k in tup:
	print(v,'-',k)
print("----------------------")
tup.sort()
print(tup)
print("----------Items sort()\n")
for v,k in tup:
	print(v,'-',k)
print("----------------------")