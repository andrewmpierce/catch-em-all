import sys, pygame;
from pygame.locals import *;
import random;


class Sprite:
    def __init__(self, xpos, ypos, img, l, w):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(img)
        self.bitmap = pygame.transform.scale(self.bitmap,(l,w))
        self.bitmap.set_colorkey((0,0,0))

    def set_position(self, xpos, ypos):
        self.x = xpos
        self.y = ypos

    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))



pygame.init()

size = width, height = 600, 500
speed = [2, 2]
black = 0, 0, 0
white = 100, 100, 100
screen = pygame.display.set_mode(size)
backdrop = pygame.image.load("images/grass.png")
backdrop = pygame.transform.scale(backdrop, size)
pokemon_caught = 0

def set_wild_pokemon(amount = 10):
    wild_pokemon = []
    rattatas = [Sprite(random.randint(10, width-10), random.randint(10, height-10), "images/rattata.jpg", 15, 15) for x in range(amount)]
    for x in rattatas:
        wild_pokemon.append(x)
    return wild_pokemon


font = pygame.font.SysFont("Times New Roman", 18)
player = Sprite(225, 375, "images/player.png", 30, 30)
balls = [Sprite(-5,-5, "images/ball.jpg", 8, 8) for x in range(10)]
ball_num = 0


def intersect(x1, x2, y1, y2):
    if x1 - x2 > -5 and x1 - x2 < 5:
        if y1 - y2 > -5 and y1 - y2 < 5:
            global pokemon_caught
            pokemon_caught += 1
            return True
    return False

def check_hits():
    for pokemon in wild_pokemon:
        for ball in balls:
            if intersect(ball.x, pokemon.x, ball.y, pokemon.y):
                pokemon.x = random.randint(10, width-10)
                pokemon.y = random. randint(25, height-10)


pygame.key.set_repeat(10,10)
space_pressed = False
wild_pokemon = set_wild_pokemon()
while 1:
  screen.blit(backdrop, (0, 0))
  for event in pygame.event.get():
      if event.type == pygame.QUIT: sys.exit()
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RIGHT:
              player.x += speed[0]
              if player.x > 480:
                  player.x = 480
          if event.key == pygame.K_LEFT:
              player.x -= speed[0]
              if player.x < 0:
                  player.x = 0
          if event.key == pygame.K_UP:
              player.y -= speed[1]
              if player.y < 0:
                  player.y = 0
          if event.key == pygame.K_DOWN:
              player.y += speed[1]
              if player.y > 480:
                  player.y = 480
          if event.key == pygame.K_SPACE and space_pressed == False:
              balls[ball_num].x = player.x
              balls[ball_num].y = player.y
              ball_num += 1
              if ball_num == 9:
                  ball_num = 0
              space_pressed = True
          if pygame.key.get_pressed()[pygame.K_SPACE] == False:
              space_pressed = False

  pokemon_counter = font.render(("Pokemon Caught: " + str(pokemon_caught)), 1, black)
  screen.blit(pokemon_counter, (5,5))

  check_hits()
  for pokemon in wild_pokemon:
      pokemon.render()
  for ball in balls:
      ball.render()
      ball.y -=1
  player.render()
  pygame.display.update()
