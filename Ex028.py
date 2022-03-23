import time
from random import randint
from time import sleep

computador = randint(0,5)
print('I am thinking about a number between 0 and 5. Try to guess it!')
jogador = int(input('What number am I thinking? '))
print('PROCESSING...')
sleep(3)
if jogador == computador:
    print('You won!')
else:
    print('You lost! I am thinking about {} not {}.'.format(computador,jogador))
sleep(5)