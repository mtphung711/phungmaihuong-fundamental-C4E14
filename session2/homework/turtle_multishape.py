from turtle import *

sides = 3

for i in range(4):
    sides = sides + i
    if sides % 2 == 0:
        color("red")
    else:
        color("blue")
    for j in range(sides):
        forward(100)
        left(360/sides)

mainloop()
