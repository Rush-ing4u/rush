import pgzrun

HEIGHT = 600
WIDTH = 600

p = Actor('ironman.png', pos = (100,100))

def draw():
    screen.clear()
    screen.draw.text('welcome to pgzero',(10,10), color = 'pink' , fontsize = 50)
    screen.draw.text("created by Rushil Sharma ",(5,280), color = 'pink')
    p.draw()

# outside functions
pgzrun.go()
 