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
screen.fill((255,255,255))
pygame.display.set_caption("Sketchpad v1.0.3")

game_going=True
pen=(0,0,0)
pen_bis=20

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
            if event.key == pygame.K_q:
                pen_input=easygui.buttonbox("What Color",
                    choices=['red','blue','green','while'])
                str(pen_input)
                if (pen_input=='red'):
                    pen=(255,0,0)
                elif (pen_input=='blue'):
                    pen=(0,0,255)
                elif (pen_input=='green'):
                    pen=(0,255,0)
                elif (pen_input=='while'):
                    pen=(255,255,255)
            if event.key == pygame.K_w:
                bis=easygui.buttonbox("How many bit",
                                      choices=['enter','20','50'])
                if (bis=='enter'):
                    bis_enter = easygui.enterbox("How is bit")
                    int(bis_enter)
                    pen_bis=bis_enter
                elif (bis==20):
                    pen_bis=20
                elif (bis==50):
                    pen_bis=50

    if mouse_down:
        spot=pygame.mouse.get_pos()
        pygame.draw.circle(screen,pen,spot,int(pen_bis))
        pygame.display.update()
pygame.quit()
