clothes = ['T-shirt', 'Sweater']

action = input('Welcome to our shop, what do you want (C, R, U, D)?')

if action == 'R' or action == 'r':
    print('Our items: ', ', '.join(clothes))

elif action == 'C' or action == 'c':
    new_item = input('Enter new item: ')
    new_item = ' '.join(new[0].upper() + new[1:] for new in new_item.split())
    clothes.append(new_item)
    print('Out items: ', ', '.join(clothes))

elif action == 'U' or action == 'u':
    while True:
        update_position = int(input('Update position?'))
        if update_position < 1 or update_position > len(clothes):
            print('Out of range')
        else:
            replacement = input('New item?')
            replacement = ' '.join(update[0].upper() + update[1:] for update in replacement.split())
            clothes[position - 1] = replacement
            print('Our items: ', ', '.join(clothes))
            break

elif action == 'D' or action == 'd':
    delete_position = int(input('Delete position? '))
    if delete_position < 1 or delete_position > len(clothes):
        print('Out of range')
    else:
        del(clothes[delete_position - 1])
        print('Our items: ', ', '.join(clothes))

else:
    print('Out of service range. Please enter either C, R, U, or D')
