import pgzrun
import math
import random 

HEIGHT = 300
WIDTH = 300

speed = 3


b = Actor('sn.png', pos = (50,50))


def draw():
    screen.clear()
    screen.fill('pink')
    b.draw()

def update():
    control()
    generate_lines()

def control():
    if keyboard.DOWN and not b.top > HEIGHT :
        b.y += speed 
    if keyboard.UP and not b.bottom < 0 :
        b.y += - speed 
    
    else:
        b.angle = 0






         


# outside functions
pgzrun.go()