#string 

greetings = 'Hello, World!'
print(greetings)
print(len(greetings))

#multy string
my_statement = '''
my name is kelvin adamba 
I have jined PLP to grow my tech skills
I love codding
'''
print(my_statement)

#string concatenation
first_name = 'Kelvin'
last_name = 'Adamba'
full_name = first_name +' '+ last_name
print(full_name)

print('\t'+ full_name)

#string formatting
fName = 'kelvin'
lName = 'adamba'
language = 'Python'
fString = 'My name is {} {}. I love {}'.format(fName, lName, language)
print(fString)

lang = 'python'

a,b,c,d,e,f = lang

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

print(lang[::-1])

chall = 'thirty days of python'
print(chall.count('th'))

challenge = 'thirty days of python'
print(challenge.replace('python','coding'))
print(challenge.split())
print(challenge.swapcase())

#Exercise
print('Thirty '+'Days '+'Of '+'Python ')
print('Coding '+'for '+' all')

name = 'Coding For All'
print(name)
print(len(name))
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(name.swapcase())
print(name[0:6])
print("Coding" in name)
print(name.split())
print(name[0])
print(name[-1])
print(name[10])
print(name.rfind("i"))
print('Name \tAge \tCountry \tCity')
print('Kelvin \t250 \tKenya \tNairobi')

radius = 10
area = 3.14 * radius **2
print('The are of a circle with a radius of {} is {} meters square'.format(radius, area))
 
a=8
b=6

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)