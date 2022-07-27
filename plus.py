from turtle import*

speed('fastest')
pencolor('black')
pensize(3)
fillcolor('red')
begin_fill()
for i in range(4):
    left(90)
    forward(50)
    for j in range(4):
      right(90)
      forward(50)
    
end_fill()
mainloop()