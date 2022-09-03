import pgzrun
from random import randint

HEIGHT = 500
WIDTH = 600

music.play('bgm')

e = Actor('alien')
p = Actor('ironman.png',(100,100))
c = Actor('sn.png')
c.x =  randint(4, WIDTH-4)
c.y =  randint(4, HEIGHT-4)

score = 0
speed = 3
time = 120   #seconds

def draw():
    screen.clear()
    screen.fill('sky blue')
    p.draw()
    c.draw()
    e.draw()
    screen.draw.text(f'score:{score}',(WIDTH-80,10))
    time_string = str(time)
    screen.draw.text( time_string, (50,0), color = 'white')


def update(delta):
    player_control()
    update_score()
    global score , time 
    time = time - delta
    if time <= 0:
        exit()
    if e.x < c.x:
      e.x = e.x + 1
    if e.x > c.x:
      e.x = e.x - 1
    if e.y < c.y:
      e.y = e.y + 1
    if e.y > c.y:
      e.y = e.y - 1
    if c.colliderect(e):
      exit()  

def update_score():
    global score
    if p.colliderect(c):
        c.pos = (randint(4, WIDTH-4),randint(4, HEIGHT-4))
        score += 1
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
