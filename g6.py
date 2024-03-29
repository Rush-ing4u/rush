import pgzrun 

HEIGHT = 500
WIDTH = 500

class Player(Actor):
    speed = 3

    def move(self):
        if keyboard.LEFT and  self.left > 0:
            self.x += -self.speed
        if keyboard.RIGHT and self.right < WIDTH:
            self.x += self.speed

print(dir(Player))

class Enemy(Actor):
    speed = 1

    def chase(self,player):
        if self.x < player.x: 
          self.x += self.speed
        if self.x > player.x:
          self.x += -self.speed
        
p = Player('ironman' , pos = (100,100))
e = Enemy('enemy.png', pos= (300,300) )

def draw():
    screen.clear()
    p.draw()
    e.draw()

def update():
    p.move()
    e.chase(p)
pgzrun.go()