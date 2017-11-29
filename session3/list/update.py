menu = ['com', 'canh', 'ca']


for i in range(len(menu)):
    print(i + 1, ". ", menu[i])

position = int(input('position you want to update '))

print(menu[position - 1])

replacement = input('Your replacement ')

menu[position - 1] = replacement

print(*menu, sep = ", ")
