import pygame;
from main import screen;

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
