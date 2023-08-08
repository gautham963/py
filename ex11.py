import random
print("This program takes name and prints a random name")

names = []

while len(names) < 8:  #for x in range(0,8)
    name = input("Enter any eight names: ")
    names.append(name)

nos = random.randint(1,7)

print("Picking a random person:",names[nos])


