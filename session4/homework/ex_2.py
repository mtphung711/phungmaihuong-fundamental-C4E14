nums = [1, 6, 5, 1, 2, 9, 6, 9, 25]

x = int(input('Enter a number: '))

count  = 0


for num in nums:
    if x == num:
        count = count + 1

print(x, 'appears', count, 'times in my list')
