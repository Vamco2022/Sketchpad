import pygame
import easygui

pygame.init()
number=0
language=0
try:
    print(input("what number X number"))
    number=int(input())
except ValueError:
    number=500
    #设置画布大小
try:
    print(input("language(English = 0,Chinese(简体中文) = 1"))
    language = int(input())
except ValueError:
    language = 0
    #设置语言

screen=pygame.display.set_mode([number,number])
screen.fill((255,255,255))
pygame.display.set_caption("Sketchpad v2.1")

game_going=True
pen=(0,0,0)
pen_size=10
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
                if language == 0:
                    #判断用户的语言
                    #控制面板
                    Down = easygui.buttonbox("menu","menu",
                        choices = ['Brush color','Brush size','clear screen','language'])
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
                            try:
                                set_r = easygui.enterbox("R")
                                set_g = easygui.enterbox("G")
                                set_b = easygui.enterbox("B")
                                pen=(int(set_r),int(set_g),int(set_b))
                            except ValueError:
                                easygui.msgbox("ERROR:Color","ERROR")
                                pen=(0,0,0ssssss)
                    if Down == 'Brush size':
                        #选大小(不会英语,被迫的)
                        SizeTemp = easygui.buttonbox("What Size","Brush size",
                            choices = ['10','50','100','Customization'])
                        if SizeTemp == '10':
                            #设置大小为10
                            pen_size = 10
                        elif SizeTemp == '50':
                            #设置大小为50
                            pen_size = 50
                        elif SizeTemp == '100':
                            #设置大小为100
                            pen_size = 100
                        elif SizeTemp == 'Customization':
                            #用户自定义大小
                            InuptSizeTemp = easygui.enterbox("How Size","Customization Size")
                            pen_size = InuptSizeTemp
                    if Down == 'clear screen':
                        #清空屏幕
                        screen.fill([255,255,255])
                    if Down == 'language':
                        #调整语言
                        languageTemp = easygui.buttonbox("language list","language",
                            choices=['Chinese(简体中文)','English(英语)'])
                        if languageTemp == 'Chinese(简体中文)':
                            language = 1
                        elif languageTemp == 'English(英语)':
                            language = 0
                elif language == 1:
                    #控制面板
                    Down = easygui.buttonbox("菜单","控制面板",
                        choices = ['调颜色','调大小','清空画板','语言'])
                    #判断用户选择的功能
                    if Down == '调颜色':
                        #选颜色
                        ColorTemp = easygui.buttonbox("选择颜色","颜色",
                            choices = ['黑色','红色','蓝色','黄色','绿色','自定义'])
                        #Customization是自定义
                        if ColorTemp == '黑色':
                            #设置颜色为黑色
                            pen=(0,0,0)
                        if ColorTemp == '红色':
                            #设置画笔颜色为红色
                            pen=(255,0,0)
                        elif ColorTemp == '蓝色':
                            #设置画笔颜色为蓝色
                            pen=(0,0,255)
                        elif ColorTemp == '黄色':
                            #Set Color is yellow(我懒得写中文了)
                            pen=(255,255,0)
                        elif ColorTemp == '绿色':
                            #Set Color is Green
                            pen=(0,255,0)
                        elif ColorTemp == '自定义':
                            #emmm
                            try:
                                set_r = easygui.enterbox("R")
                                set_g = easygui.enterbox("G")
                                set_b = easygui.enterbox("B")
                                pen=(int(set_r),int(set_g),int(set_b))
                            except ValueError:
                                easygui.msgbox("ERROR:Color","ERROR")
                                pen = (0,0,0)
                    if Down == '调大小':
                        #选大小(不会英语,被迫的)
                        SizeTemp = easygui.buttonbox("选择大小","大小",
                            choices = ['10','50','100','自定义'])
                        if SizeTemp == '10':
                            #设置大小为10
                            pen_size = 10
                        elif SizeTemp == '50':
                            #设置大小为50
                            pen_size = 50
                        elif SizeTemp == '100':
                            #设置大小为100
                            pen_size = 100
                        elif SizeTemp == '自定义':
                            #用户自定义大小
                            InuptSizeTemp = easygui.enterbox("多大","自定义大小")
                            pen_size = InuptSizeTemp
                    if Down == '清空画板':
                        #清空屏幕
                        screen.fill([255,255,255])
                    if Down == '语言':
                        #调整语言
                        languageTemp = easygui.buttonbox("语言列表","语言",
                            choices=['Chinese(简体中文)','English(英语)'])
                        if languageTemp == 'Chinese(简体中文)':
                            language = 1
                        elif languageTemp == 'English(英语)':
                            language = 0

    if mouse_down:
        #绘制
        try:
            spot=pygame.mouse.get_pos()
            pygame.draw.circle(screen,pen,spot,int(pen_size))
            pygame.display.update()
        except ValueError:
            easygui.msgbox("ValueError:Size","ERROR")
            pen_size = 10
pygame.quit()
