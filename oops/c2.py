class Cat:

    def __init__(self, breed, fur_color, gender = 'F', age = 1, w = 1, h = 1, is_tamed = True):
        self.breed = breed
        self.fur_color = fur_color
        self.gender = gender 
        self.age = age 
        self.weight = w
        self.height = h 
        self.is_tamed = is_tamed

    def eat(self , food = 'catfood'):
        print(f'cat is eating {food}')

    def play(self):
        print(f'cat is playing')

    def sleep(self):
        print(f'cat is sleeping')

    def info(self):
        print('--' *15) # optional
        print(f'BREED:{self.breed}')
        print(f'FUR COLOR:{self.fur_color}')
        print(f'GENDER:{self.gender}')
        print(f'AGE:{self.age}year')
        print(f'WEIGHT:{self.weight}kg')
        print(f'HEIGHT:{self.height}ft')
        print(f'TAMED:{self.is_tamed}')
        print('--' *15) # optional

leo = Cat( 'street' ,'grey' , age = 100 , gender = 'M')

print("LEO")
leo.info()
leo.eat('catfood')      
