import random
from random import randint

balls = []
for i in range(10):
    x = random.randint(0,9)
    y = random.randint(0,9)
    ball = dict(x=x, y=y)
    balls.append(ball)
for n in range(0,2):
    print('try №', n, ':', balls)
    i = 0
    for ball in balls:
        choise = input('y or n?\n')
        if choise == 'y':
            print(ball)
            balls.pop(balls.index(ball))
            print('deleted №', i, ': ', balls)
        i += 1
    print('The last version is: ', balls, '\n')