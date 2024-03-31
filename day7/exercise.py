# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add("Twitter")
print(it_companies)

it_companies.update(['Safaricom','Amazon','NAYA'])
print(it_companies)

it_companies.remove("Facebook")
print(it_companies)

print(A.issubset(B))

it_companies.discard
("awo")

print(A.union(B))
print(A.intersection(B))

print('------------------------------------------------')
print(age)
age1 = set(age)
print(age1)

print(len(age) > len(age1) )

string = 'I am a teacher and I love to inspire and teach people'
print(len(set(string.split())))