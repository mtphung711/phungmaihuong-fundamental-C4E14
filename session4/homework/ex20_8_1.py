letter_counts = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for letter in "Mine eyes dazZles she died young".lower():
    if letter in alphabet:
        if letter not in letter_counts:
            letter_counts[letter] = 1
        else:
            letter_counts[letter] += 1

letter_items = list(letter_counts.items())
letter_items.sort()
for item in letter_items:
    print(item)
