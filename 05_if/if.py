import random

color = ["green", "red", "yellow"]
alien_color = random.choice(color)

if alien_color == 'green':
    print(f"{alien_color.title()} has been shot down")
if alien_color == 'red':
    print(f"{alien_color.title()} has been shot down")
if alien_color == 'yellow':
        print(f"{alien_color.title()} has been shot down")

if alien_color == 'green':
    print('+5pkt')
elif alien_color == 'yellow':
    print('+10pkt')
elif alien_color == 'red':
    print('+15pkt')

print('---------Life stages----------')
age = random.randint(0,100)
print(age)

if age < 2:
    print("baby")
elif age >= 2 and age < 4:
    print("baby but older")
elif age >= 4 and age < 13:
    print("kid")
elif age >= 13 and age < 20:
    print('teenager')
elif age >= 20 and age < 65:
    print("adult")
elif age >= 65:
    print('senior')

print('-------------fruits-------------')
fruits = ['apple', 'banana', 'kiwi']

if 'apple' in fruits:
    print('apple is on the list')
if 'banana' in fruits:
    print('banana is on the list')
if 'kiwi' in fruits:
    print('kiwi is on the list')

