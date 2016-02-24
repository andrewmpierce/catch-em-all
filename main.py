import sys, pygame;
from pygame.locals import *;
#import player;

pygame.init()

size = width, height = 500, 400
speed = [2, 2]
black = 0, 0, 0
white = 100, 100, 100
screen = pygame.display.set_mode(size)

player = pygame.image.load("images/player.png")
player = pygame.transform.scale(player, (25, 25))
playerrect = player.get_rect()
pygame.key.set_repeat(10,10)
playerrect.x = 225
playerrect.y = 375

while 1:
  for event in pygame.event.get():
      if event.type == pygame.QUIT: sys.exit()
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RIGHT:
              playerrect.x += speed[0]
              if playerrect.x > 480:
                  playerrect.x = 480
          if event.key == pygame.K_LEFT:
              playerrect.x -= speed[0]
              if playerrect.x < 0:
                  playerrect.x = 0
          if event.key == pygame.K_UP:
              playerrect.y -= speed[1]
              if playerrect.y < 0:
                  playerrect.y = 0
          if event.key == pygame.K_DOWN:
              playerrect.y += speed[1]
              if playerrect.y > 380:
                  playerrect.y = 380

  screen.fill(black)
  screen.blit(player, playerrect)
  pygame.display.flip()
