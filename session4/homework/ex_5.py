rabbits = {0: 0, 1: 1}

def F(n):
    if n not in rabbits:
        no_of_rabbits = F(n - 2) + F(n - 1)
        rabbits[n] = no_of_rabbits
    return rabbits[n]

for i in range(5):
    print('Month', i, ':', F(i), 'pair(s) of rabbits')
