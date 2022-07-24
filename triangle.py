from turtle import*
speed('slowest')
pencolor('red')
bgcolor('pink')

side = 3
size = 200
for i in range(side):
    forward(size)
    left(360/side)
mainloop()