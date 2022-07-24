from turtle import*
speed('slowest')
pencolor('red')
bgcolor('pink')

side = 12
size = 50
for i in range(side):
    forward(size)
    left(360/side)
mainloop()