st =set()
dt = {"animal","humans"}

print(type(st))
print(type(dt))

counties =set(("Nairobi","Mombasa","Nandi","Vihiga"))
print(counties)

print(len(counties))

for county in counties:
    print(county)

print("Vihiga" in counties)

counties.add("Kisumu")
print(counties)

counties2 = set(("Kisii","Busia"))

counties.update(counties2)
print(counties)

counties.remove("Nandi")
print(counties)

print(counties.pop())

counties.clear()
print(counties)

del counties

st1 = set(('item1','item2','item3'))
st2 = set(('item4','item5','item6'))

print(st1.union(st2))
st1.update(st2)
print(st1)

