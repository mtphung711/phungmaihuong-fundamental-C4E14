fav = ['deathnote', 'netflix', 'teaching']

print('Hi, your favorite things so far are: ', *fav, sep =', ') #separator

addition = input('Name one thing you want to add ')

fav.append(addition)

print(*fav, sep =', ')
