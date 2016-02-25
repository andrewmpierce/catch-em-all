from pygame import *;

class Player:
        def __init__(self, xpos, ypos):
                self.x = xpos
                self.y = ypos
                self.bitmap = image.load("images/player.png")
                self.bitmap.set_colorkey((0,0,0))
        def set_position(self, xpos, ypos):
                self.x = xpos
                self.y = ypos
        def render(self):
                pygame.screen.blit(self.bitmap, (self.x, self.y))
