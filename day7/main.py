country = {'Kenya','Uganda','Tanzania'}

#checking if an element exist in a set
print('kenya' in country)

#Adding an item 
country.add("Somalia",)
print(country)

#we can add multiple line using update() which takes list arguments

country.update(['Burundi','Ethopia','Congo'])
print(country)

#removin item
country.remove("Congo")
print(country)

#pop removes a random item

print(country.pop())

#joining sets
set1 = {'item1','item2','item3'}
set2 = {'item4','item5','item6'}

print(set1.union(set2))

set3 = set1.update(set2)

print(set3)