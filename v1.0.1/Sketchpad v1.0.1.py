import pygame
import easygui

pygame.init()
number=0
try:
    print(input("what number X number"))
    number=int(input())
except ValueError:
    number=500
screen=pygame.display.set_mode([number,number])
pygame.display.set_caption("em")
background_color=(0,0,0)

game_going=True
pen=(255,255,255)

mouse_down=False

while game_going==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_going=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down=True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_down=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                pen=(255,0,0)
            if event.type==pygame.K_g:
                pen=(0,255,0)
            if event.key == pygame.K_b:
                pen=(0,0,155)
            if event.type==pygame.K_e:
                pen=(255,255,255)
            if event.key == pygame.K_b:
                pen=(0,0,0)
            if event.type==pygame.K_y:
                pen=(255,255,0)
    if mouse_down:
        spot=pygame.mouse.get_pos()
        pygame.draw.circle(screen,pen, spot,20)
        pygame.display.update()
pygame.quit()
