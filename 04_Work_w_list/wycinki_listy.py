values = []
for value in range(1,11):
        values.append(value)
print(values)
print("\nPierwsze trzy wartosci to:")
print(values[0:3])

mid = int(len(values)/2)
print(mid)
print(values[mid-1:mid+1])

print("\nOstatnie 3 wartości to:")
print(values[-3:])

print("\n\n")
my_foods = ["salami", "calzone", "hawaii"]
friend_foods = my_foods[:]

my_foods.append("rucola")
friend_foods.append("vege")

#for food in my_foods:
print("My foods:")
for food in my_foods:
    print(food)

#for food in friend_foods:
print("\nFriend foods:")
for food in friend_foods:
    print(food)
