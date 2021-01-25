invited = ['Aga', 'Ewa', 'Jan', 'Kuba']
message0 = f'Feel free to join us {invited[0].title()}'
message1 = f'Feel free to join us {invited[1].title()}'
message2 = f'Feel free to join us {invited[2].title()}'
message3 = f'Feel free to join us {invited[3].title()}'
print(message0)
print(message1)
print(message2)
print(message3)
print(f'Unfortunatelly, {invited[0].title()} is unable to come over')
del invited[0]
print(invited)
invited.insert(0, 'dioda')
print(invited)
message0 = f'Feel free to join us {invited[0].title()}'
message1 = f'Feel free to join us {invited[1].title()}'
message2 = f'Feel free to join us {invited[2].title()}'
message3 = f'Feel free to join us {invited[3].title()}'
print(message0)
print(message1)
print(message2)
print(message3)
print('Larger table has been found!')
invited.append('irek')
message0 = f'Feel free to join us {invited[0].title()}'
message1 = f'Feel free to join us {invited[1].title()}'
message2 = f'Feel free to join us {invited[2].title()}'
message3 = f'Feel free to join us {invited[3].title()}'
message4 = f'Feel free to join us {invited[4].title()}'
print(message0)
print(message1)
print(message2)
print(message3)
print(message4)
print('There is no table at all')
invited.pop()
invited.pop()
invited.pop()
print(invited)
