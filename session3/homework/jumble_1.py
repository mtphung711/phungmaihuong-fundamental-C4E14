import random

word = list('flabbergasted')

correct = 'flabbergasted'

random.shuffle(word)

print(*word)

your_answer = input('Your answer: ')
if your_answer == correct:
    print('Hura')
else:
    print('Please try again')
