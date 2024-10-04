# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1
print(len(it_companies))
#2
it_companies.add("Twitter")
print(it_companies)

#3
it_companies2=set(("NAYA","POA"))
it_companies.update(it_companies2)
print(it_companies)
#4
it_companies.remove("NAYA")
print(it_companies)

#exercise level 2
#1
A.union(B)
print(A)
#2
print(A.intersection(B))
#3
print(A.issubset(B))
#4
print(A.isdisjoint(B))
#5
print(A.difference(B))
#6
del A

#exercise level 3
agest = set(age)
print("the len of of age list is: ",len(age))
print("the len of age set is: ",len(agest))


string = 'I am a teacher and I love to inspire and teach people.'
print(len(set(string.split())))