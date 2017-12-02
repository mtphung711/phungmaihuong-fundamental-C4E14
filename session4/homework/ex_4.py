initial = int(input('How many B bacteria are there?'))

mins = int(input('How many minutes will we wait?'))

if mins % 2 == 1:
    mins = mins - 1

total = initial * (2**(mins / 2))        #mins/2 = the number of times bacteria replicate themselves

print('After', mins, 'minutes, we would have', total, 'bacteria')
