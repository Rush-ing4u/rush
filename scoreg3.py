import pgzrun
from random import randint

HEIGHT = 500
WIDTH = 600

music.play('bgm')

p = Actor('ironman.png',(100,100))
c = Actor('sn.png')
c.x =  randint(64, WIDTH-64)
c.y =  randint(64, HEIGHT-64)

score = 0
speed = 3 

def draw():
    screen.fill('sky blue')
    p.draw()
    c.draw()
    screen.draw.text(f'score:{score}',(WIDTH-80,10))

def update():
    player_control()
    update_score()

def update_score():
    global score
    if p.colliderect(c):
        score += 1
        c.pos = (randint(64, WIDTH-64),randint(64,HEIGHT-64))
        sounds.eating2.play()

def player_control():
    if keyboard.RIGHT and  not p.right > WIDTH:
      p.x += speed
    elif keyboard.LEFT and  not p.left < 0:
      p.x += -speed
    elif keyboard.DOWN and  not p.top > HEIGHT:
      p.y += speed
    elif keyboard.UP and  not p.bottom < 0:
      p.y += -speed
    else :
        p.angle = 0

         

pgzrun.go()   # outside the function 