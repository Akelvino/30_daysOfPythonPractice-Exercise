#1
import random
char = 'abcdefghijklmnopqrstuvwxyz1234567890'
char_list =[]
char_list[:0] = char

def random_user_id():
    identity = ''
    for _ in range(6):
        identity+=random.choice(char_list)
    return identity

print(random_user_id())

#2
def user_id_gen_by_user():
    ident = ''
    charsize = int(input("Enter character size: "))
    charlimit= int(input("Enter how many user ids to generate: "))
    for _ in range(charlimit):
        ident = ''.join([random.choice(char_list) for _ in range(charsize)])
        print(ident)

print(user_id_gen_by_user())


#3
def rgb_color_gen():
    r = str(random.randint(0, 255))
    g = str(random.randint(0, 255))
    b = str(random.randint(0, 255))

    return f'{r},{g},{b}'
print(rgb_color_gen())


#4
def seven_random():
    arr = []
    length = -1

    while length <=7:
        num = random.randint(0,9)
        if num not in arr:
            arr.append(num)
            length = len(arr)
    return arr

print(seven_random())
