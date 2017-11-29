favs = ['deathnote', 'netflix', 'teaching']

for i, fav in enumerate(favs): #khong dat trung ten keo mat du lieu chet me
    print(i + 1, favs[i], sep = ". ")

while True:
    position = int(input('position you want to delete'))
    if position < 1 or position > len(favs):
        print("out of range")
    else:
        del favs[position - 1]

        for i, fav in enumerate(favs):
            print(i + 1, favs[i], sep=". ")
        break
