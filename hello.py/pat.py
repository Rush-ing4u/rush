from turtle import*
pensize(3)
for i in range(8):
    pencolor('red')
    forward(100)
    for j in range(6):
      pencolor('black')
      forward(100)
      left(360/6)
    left(360/8)
mainloop()