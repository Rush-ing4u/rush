import pgzrun
from random import randint 
HEIGHT = 500 
WIDTH = 600

ps = 3 # player speed 
es = 1 # enemy speed
p = Actor('ironman')
e = Actor('enemy')

game_over = False # switch
game_started = False # switch 

center = ( WIDTH // 2, HEIGHT // 2) # points to center coordinates of screen 

bg = Actor('bg.jpg', center =(0,0))

def show_screen_1() :
    bg.draw()
    screen.draw.text('Our Game', center = center , fontsize = 100 , color = ' black')
    screen.draw.text('press Space to start', center = (center[0], center[1]+100) , fontsize = 40 , color = 'black')

def show_game_screen():
    bg.draw()
    p.draw()
    e.draw()

def show_game_over():
    bg.draw()
    screen.draw.text('Game Over', center = center , fontsize = 100 , color = ' white')
    

def draw():
    screen.clear()
    if not game_started:
       show_screen_1()
    elif game_started and not game_over:
     show_game_screen()
    elif  game_over :
        show_game_over()


def update():
    global game_started
    if keyboard.SPACE and not game_started :
        game_started = True 
    
    if game_started and not game_over :
        game_started = True  
        play_control()
        enemy_control()

def play_control():
    if keyboard.RIGHT and  not p.right > WIDTH:
      p.x += ps
    elif keyboard.LEFT and  not p.left < 0:
      p.x += -ps
    elif keyboard.DOWN and  not p.top > HEIGHT:
      p.y += ps
    elif keyboard.UP and  not p.bottom < 0:
      p.y += -ps
    else :
        p.angle = 0


def enemy_control():
   if p.x > e.x: 
    e.x += es
   if p.x < e.x:
    e.x += -e.x
   if p.y > e.y:
    e.y += es
   if p.y < e.y:
    e.y += -e.y
   if p.colliderect(e):
    game_over = True 


         


# outside functions
pgzrun.go()