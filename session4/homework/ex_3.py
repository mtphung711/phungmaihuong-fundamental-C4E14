x = int(input('Enter a number '))

prime_number = True
count = 0

while count < x - 2:
    for i in range(2, x - 1):
        count = count + 1
        if x % i == 0:
            prime_number = False

if not prime_number:
    print('not a prime number')
else:
    print('prime number')
