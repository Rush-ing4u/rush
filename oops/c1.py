# Bakwas Class
class Cat:
    breed = None
    gender = None
    fur_color = None
    age = None 
    weight = None
    height = None 
    is_tamed = None 

    def eat(self , food = 'catfood'):
        print(f'cat is eating {food}')
    def play(self):
        print(f'cat is playing')
    def sleep(self):
        print(f'cat is sleeping')


billu = Cat() #constructor calling 
leo = Cat()

billu.breed = 'persian'
billu.weight = 2
billu.age = 2
billu.fur_color = 'white'
billu.height = 1
billu.gender = 'M'
billu.is_tamed = True

leo.breed = 'street cat'
leo.weight = 1.5
leo.age = 100
leo.fur_color = 'white'
leo.height = 1.1
leo.gender = 'M'
leo.is_tamed = True

inzhangi = Cat()

inzhangi.breed = 'wild cat'
inzhangi.weight = 4
inzhangi.age = 1.5
inzhangi.fur_color = 'ginger'
inzhangi.height = 1
inzhangi.gender = 'F'
inzhangi.is_tamed = True


print('billu details')
print('breed',billu.breed)
print('gender',billu.gender)
print('age',billu.age)
print('weight',billu.weight)
print('height',billu.height)
print('fur_color',billu.fur_color)
print('pet', 'yes' if billu.is_tamed else 'no')
billu.sleep()
billu.play()
billu.eat()

print('leo details')
print('breed',leo.breed)
print('gender',leo.gender)
print('age',leo.age)
print('weight',leo.weight)
print('height',leo.height)
print('fur_color',leo.fur_color)
print('pet', 'yes' if leo.is_tamed else 'no')
leo.sleep()
leo.play()
leo.eat()

print('inzhangi details')
print('breed',inzhangi.breed)
print('gender',inzhangi.gender)
print('age',inzhangi.age)
print('weight',inzhangi.weight)
print('height',inzhangi.height)
print('fur_color',inzhangi.fur_color)
print('pet', 'yes' if inzhangi.is_tamed else 'no')
inzhangi.sleep()
inzhangi.play()
inzhangi.eat()
