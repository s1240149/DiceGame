import random

name=input("What is your name? ")
print("Hello, "+name+"!")

random.seed()

print("Rolling the dice...")
a=random.randint(1,6)
b=random.randint(1,6)

print("Die 1: "+str(a))
print("Die 2: "+str(b))
print("Total value: "+str(a+b))
