import pygame
import easygui
import sys

pygame.init()
try:
    print(input("what number X number"))
    number=int(input())
except ValueError:
    easygui.msgbox("ValueError:the number is NULL")
    sys.close()
screen=pygame.display.set_mode([number,number])
pygame.display.set_caption("em")

game_going=True
whiles=(255,255,255)

mouse_down=False

while game_going==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_going=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down=True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_down=False
    if mouse_down:
        spot=pygame.mouse.get_pos()
        pygame.draw.circle(screen,whiles,spot,20)
        pygame.display.update()
pygame.quit()