#1
def add_two_numbers(a,b):
    return a+b
print(add_two_numbers(10,20))

#2
def area_of_circle(r):
    return 3.14*r*r
print(area_of_circle(3))

#3
def sum_of_all_numbers(*number):
    total = 0
    for i in number:
        if isinstance(i, int):
            total+=i
    return total
print(sum_of_all_numbers(1,1,1,1,1))

#4
def convert_celsius_to_fahrenheit(c):
    return f'{(c*9/5)+32}°F'
print(convert_celsius_to_fahrenheit(23))

#5

def check_season(month):
    if month in ["September","October","November"]:
        return "Autumn"
    elif month in ["December", "January", "February"]:
        return "Winter"
    elif month in ["March", "April", "May"]:
        return "Spring"
    else:
        return "Summer"

print(check_season("may"))

#6
def sum_of_numbers(j):
    total=0
    for i in range(j+1):
       total+=i
    print(total)
sum_of_numbers(5)
sum_of_numbers(10)
sum_of_numbers(100)

#7
def evens_and_odds(high):
    odds = 0
    evens = 0
    for i in range(high + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    print(odds, evens)

evens_and_odds(100)

#8
def factorial_number(j):
    fact=1
    for jj in range(j+1):
        fact*=jj
    return fact

print(factorial_number(10))