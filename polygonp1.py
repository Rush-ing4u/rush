from turtle import*
speed('slowest')
pencolor('black')
bgcolor('pink')
pensize(3)

side = 12
size = 50
fillcolor('red')
begin_fill()
for i in range(side):
    forward(size)
    left(360/side)
end_fill()
mainloop()