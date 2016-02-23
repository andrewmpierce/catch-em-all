import sys, pygame;
from pygame.locals import *;
#import player;

pygame.init()

size = width, height = 500, 400
speed = [2, 2]
black = 0, 0, 0
white = 100, 100, 100
screen = pygame.display.set_mode(size)

ball = pygame.image.load("images/ball.bmp")
ballrect = ball.get_rect()
pygame.key.set_repeat(10,10)

while 1:
  for event in pygame.event.get():
      if event.type == pygame.QUIT: sys.exit()
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_k:
              ballrect.x = ballrect.x +speed[0]

  screen.fill(black)
  screen.blit(ball, ballrect)
  pygame.display.flip()
