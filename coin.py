WIDTH = 400
from random import randint
HEIGHT = 400
score = 0
game_over = False
fox = Actor ("fox")
fox.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200

def draw():
    screen.fill ("green")
    fox.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))

def place_coin():
    pass

def time_up():
    pass

def update():
    pass
