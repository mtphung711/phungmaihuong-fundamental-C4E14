sheeps = [5, 12, 4, 23, 45, 17]

print('Hello, my name is Huong and these are my sheep size: ', sheeps)

biggest_size = max(sheeps)

print("Now my biggest sheep has size", biggest_size, "let's sheer it" )

for i, size in enumerate(sheeps):
    if size == max(sheeps):
        sheeps[i] = 8
        print('After sheering, here is my flock: ', sheeps)

sheeps = [size + 50 for size in sheeps]

print('One month has passed, now here is my flock: ', sheeps)
