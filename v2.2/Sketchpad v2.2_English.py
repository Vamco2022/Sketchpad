import pygame
import easygui

pygame.init()
number=0
try:
    print(input("what number X number"))
    number=int(input())
except ValueError:
    number=500
    #设置画布大小
screen=pygame.display.set_mode([number,number])
screen.fill((255,255,255))
pygame.display.set_caption("Sketchpad v2.0")

game_going=True
pen=(0,0,0)
pen_size=10
IsEnglish=True
#初始化画笔

mouse_down=False
#鼠标监测
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
                #控制面板
                Down = easygui.buttonbox("menu","menu",
                    choices = ['Brush color','Brush size','clear screen'])
                #判断用户选择的功能
                if Down == 'Brush color':
                    #选颜色
                    ColorTemp = easygui.buttonbox("What color","Brush color",
                        choices = ['black','red','blue','yellow','Green','Customization'])
                    #Customization是自定义
                    if ColorTemp == 'black':
                        #设置颜色为黑色
                        pen=(0,0,0)
                    if ColorTemp == 'red':
                        #设置画笔颜色为红色
                        pen=(255,0,0)
                    elif ColorTemp == 'blue':
                        #设置画笔颜色为蓝色
                        pen=(0,0,255)
                    elif ColorTemp == 'yellow':
                        #Set Color is yellow(我懒得写中文了)
                        pen=(255,255,0)
                    elif ColorTemp == 'Green':
                        #Set Color is Green
                        pen=(0,255,0)
                    elif ColorTemp == 'Customization':
                        #emmm
                        set_r = easygui.enterbox("R")
                        set_g = easygui.enterbox("G")
                        set_b = easygui.enterbox("B")
                        pen=(int(set_r),int(set_g),int(set_b))
                if Down == 'Brush size':
                    #选大小(不会英语,被迫的)
                    SizeTemp = easygui.buttonbox("What Size","Brush size",
                        choices = ['10','50','100','Customization'])
                    if SizeTemp == '20':
                        #设置大小为10
                        pen_size = 10
                    if SizeTemp == '50':
                        #设置大小为50
                        pen_size = 50
                    if SizeTemp == '100':
                        #设置大小为100
                        pen_size = 100
                    if SizeTemp == 'Customization':
                        #用户自定义大小
                        InuptSizeTemp = easygui.enterbox("How Size","Customization Size")
                        pen_size = InuptSizeTemp
                if Down == 'clear screen':
                    #清空屏幕
                    screen.fill([255,255,255])


    if mouse_down:
        #绘制
        spot=pygame.mouse.get_pos()
        pygame.draw.circle(screen,pen,spot,int(pen_size))
        pygame.display.update()
pygame.quit()
