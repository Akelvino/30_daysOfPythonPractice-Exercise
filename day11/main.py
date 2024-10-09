def generete_full_name():
    fname="Kelvin"
    space =" "
    lname = "Adamba"
    return(fname+space+lname)

print(generete_full_name())


def greetings(name="Adamba"):
    return f'Hello, {name}'

print(greetings("Kelvin"))
print(greetings("Elvira"))
print(greetings())

def sum_of_two_numbers(num1,num2):
    return f"The sum of {num1} and {num2} is {num1+num2}"

print(sum_of_two_numbers(100,10))


def is_even(n):
    if n%2==0:
        print("even")
        return True
    return False

print(is_even(7))
print(is_even(6))

def find_even_numbers(numbers):
    even=[]
    for number in range(numbers+1):
        if number % 2==0:
            even.append(number)
    return(even)

print(find_even_numbers(10))


#arbitrary arguments 
def summ_all_numbers(*nums):
    total=0
    for i in nums:
        total+=i
    return i
print(summ_all_numbers(1,3,4,6,2))

#function as aprameter of another function 

def squre_number(j):
    return j*j

def do_something(f,x):
    return f(x)

# print(squre_number(9))

print(do_something(squre_number,3))