from turtle import *

screensize(1000, 1000)
width(10)

n = int(input('Enter a number'))

for i in range(n):
    if i % 6 < 3:
        color('pink')
    else:
        color('green')

    forward(40)
    penup()
    forward(40)
    pendown()




mainloop()
