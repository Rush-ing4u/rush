from turtle import* 
pencolor('red')
fillcolor('pink')
speed('fastest')
for i in range(10,0,-1):
    begin_fill()
    circle(i*10)
    left(25)
    end_fill()

mainloop()