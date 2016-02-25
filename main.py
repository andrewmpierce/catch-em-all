import sys, pygame;
from pygame.locals import *;
#import player;


class Player:
    def __init__(self, xpos, ypos):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load("images/player.png")
        self.bitmap = pygame.transform.scale(self.bitmap,(25,25))
        self.bitmap.set_colorkey((0,0,0))

    def set_position(self, xpos, ypos):
        self.x = xpos
        self.y = ypos

    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))


class Ball:
    def __init__(self, xpos, ypos):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load("images/ball.jpg")
        self.bitmap = pygame.transform.scale(self.bitmap, (5,5))
        self.bitmap.set_colorkey((0,0,0,))

    def set_position(self, xpos, ypos):
        self.x = xpos
        self.y = ypos

    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))




pygame.init()

size = width, height = 500, 400
speed = [2, 2]
black = 0, 0, 0
white = 100, 100, 100
screen = pygame.display.set_mode(size)
backdrop = pygame.image.load("images/grass.png")
backdrop = pygame.transform.scale(backdrop, size)


player = Player(225, 375)
balls = [Ball(-5,-5) for x in range(10)]
ball_num = 0


pygame.key.set_repeat(10,10)

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
              if player.y > 380:
                  player.y = 380
          if event.key_pressed() == pygame.K_SPACE:
              balls[ball_num].x = player.x
              balls[ball_num].y = player.y
              ball_num += 1
              if ball_num == 9:
                  ball_num = 0

  for ball in balls:
      ball.render()
      ball.y -=1
  player.render()
  pygame.display.update()
