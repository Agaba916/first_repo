#print("Hello GitHub! This is my first Python file.")
#print("Real it is !")
#o=3
#z=str(2)
#y=complex(o)
a="""Lorem ipsum dolor sit amet,
consectatetur adipiscing elit,
sed do eiusmod tempor incididunt 
ut labore et dolore magna aliqua."""#3 single quotes can also be used.
print(type(y))
print(y)
import random
print(random.randrange(1,10))
print(z)
print(a)
r='name'
b='AHJE'
for x in b:
  print(x)
print(b[1])
print(len(b))

print('Lorem' in a)
print('amare' not in a)

if 'Lorem' in a:
  print('yeah it is present')

if 'amare' not in a:
  print('exactly not present')
else:
  print('it is present')    
print(r[0:2])
print(r[:3])
print(r[2:])
print(r[-3:-1])
print(a.upper())
print(b.lower())
c=" abantu bose "
print(c.strip())
print(c)
print(c.replace("abantu bose","abanyeshuri nabo rwose "))
print(c)
p="me and me"
print(p.replace ("me","I"))
q= c+p
print(q)
print(p.split("and"))
print(f"My name is {b} and i have {o}")
print(f"This is really funny {o:.2f}")
print(f"This is somehow enough for now {4*8} got it right")