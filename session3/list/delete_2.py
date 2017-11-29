favs = ['deathnote', 'netflix', 'teaching']

for i, item in enumerate(favs): #khong dat trung ten keo mat du lieu chet me
    print(i + 1, favs[i], sep = ". ")


delete_item = input('item you want to delete ')
if delete_item in favs: #"not in" also exists
    favs.remove(delete_item)

    for i, item in enumerate(favs):
        print(i + 1, favs[i], sep = ". ")

else:
    print("item not found")
