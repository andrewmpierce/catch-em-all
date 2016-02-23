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
          if event.key == pygame.K_RIGHT:
              ballrect.x += speed[0]
              if ballrect.x > 450:
                  ballrect.x = 450
          if event.key == pygame.K_LEFT:
              ballrect.x -= speed[0]
              if ballrect.x < 0:
                  ballrect.x = 0
          if event.key == pygame.K_UP:
              ballrect.y -= speed[1]
              if ballrect.y < 0:
                  ballrect.y = 0
          if event.key == pygame.K_DOWN:
              ballrect.y += speed[1]
              if ballrect.y > 350:
                  ballrect.y = 350

  screen.fill(black)
  screen.blit(ball, ballrect)
  pygame.display.flip()
