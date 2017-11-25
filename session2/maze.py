from turtle import *

speed(-1)
shape("turtle")
color("red")

forward(3)

for i in range(0, 300, 3):
    left(90)
    forward(i)


mainloop()
