# -*- coding: utf-8 -*-
import pygame
window = pygame.display.set_mode((400, 400))
pygame.display.set_caption('kek!')
screen = pygame.Surface((400, 400))
# square = pygame.Surface((40, 40))
class Meow:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((255, 255, 255))
    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))
# x = 0
hero = Meow(0, 0, 'kek1.png')
aim = Meow(200, 200, 'kek2.png')
hero_goright = True
# y = 0
# square_down = True
# square_right = True
done = True
while done:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = False
    screen.fill((103, 233, 247))
    hero.render()
    aim.render()
    # screen.blit(square, (x, y))
    window.blit(screen, (0, 0))
    pygame.display.flip()
    if hero_goright == True:
        hero.x += 1
        if hero.x > 300:
            hero_goright = False
    else:
        hero.x -= 1
        if hero.x <= 0:
            hero_goright = True
    # if square_down == True:
    #     y += 1
    #     if y > 360:
    #         square_down = False
    # else:
    #     y -= 1
    #     if y <= 0:
    #         square_down = True
    pygame.time.delay(5)
