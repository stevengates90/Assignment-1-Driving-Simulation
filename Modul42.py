a = 0
b = 0
c = []

for x in range(10):
    a=int(input())
    c.append(a%42)

d = set(c)
e = len(d)
print(e)
