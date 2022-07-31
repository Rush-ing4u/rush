from random import randint
win_count = 0
lose_count = 0

dice = ['1','2','3','4','5','6'] # 0,1,2,3,4,5=1,2,3,4,5,6
while True:
    print("Press enter to Roll Dice")
    out = randint(0,5)
    print(f'dice => {dice[out-1]}')
    if out == 6:
        win_count += 1
    elif out == 1:
        lose_count += 1
    if win_count == 3:
        print("You win")
        break
    elif lose_count == 3:
        print("You lose")
        break
