sheeps = [5, 12, 4, 23, 45, 17]

print('Hello, my name is Huong and these are my sheep size: ', sheeps) #month0
biggest_size = max(sheeps)
print("Now my biggest sheep has size", biggest_size, "let's sheer it" )
for i, size in enumerate(sheeps):
    if size == max(sheeps):
        sheeps[i] = 8
        print('After sheering, here is my flock: ', sheeps)

for month in range(1,4): #month1to3
  print('MONTH ', month)
  sheeps = [size + 50 for size in sheeps]
  print('One month has passed, now here is my flock: ', sheeps)

  biggest_size = max(sheeps)
  print("Now my biggest sheep has size", biggest_size, "let's sheer it" )

  for i, size in enumerate(sheeps):
      if size == max(sheeps):
          sheeps[i] = 8
          print('After sheering, here is my flock: ', sheeps)
          break

total_size = sum(sheeps)
print('My flock has size in total: ', total_size)
money = total_size * 2
print('I would get', total_size, '*', '2', '$', '=', money, '$')
