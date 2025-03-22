import math
import functools
print(round(2.9))
print()
math.comb(2,1)



#fabs: absolute value of x. 
print(f"{math.floor(4.5)}") 
#math.fmod: remainder 
print(f"{math.floor(4.5)}") 

numbers = [1,23,45]
print(f"{math.fsum(numbers)}")

numbers2 =[12,45,36]

print(f"{(functools.reduce(math.gcd, numbers2))}")

print(f"{math.gcd(*numbers2)}")

#diiinput("X:")

def greet(name):
    return print(f"hello,{name}")

#user_name = input("what is your name")
#rprint(f"{greet(user_name)}")

prime_numbers = []

Integerfind_1 = (range(2,101))

for numbers in Integerfind_1:
    is_prime = True
    for x in range(2,int(numbers)):
        if x == numbers:
             break
        elif math.fmod(numbers, x) ==0:
            is_prime = False

    if is_prime:
        prime_numbers.append(numbers)
 

print(prime_numbers)



fruits = ['apple','bannana','pinnaple']
for index, fruit in enumerate(fruits, start = 1):
        print(index,fruit)



    