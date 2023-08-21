import pygame
import easygui

pygame.init()
number=0
try:
    number = easygui.enterbox("请输入画布大小")
    number = int(number)
except ValueError:
    easygui.msgbox("参数·输入错误")
    number=500
    #设置画布大小
int(number)
screen = pygame.display.set_mode([number,number])
screen.fill((255,255,255))
pygame.display.set_caption("Sketchpad v2.2 - Chinese")

game_going=True

pen = (0,0,0)
pen_size = 10
#初始化画笔

mouse_down = False
#鼠标监测
while game_going == True:

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
                Down = easygui.buttonbox("菜单","菜单",
                    choices = ['调颜色','调大小','清空屏幕'])
                #判断用户选择的功能
                if Down == '调颜色':
                    #选颜色
                    ColorTemp = easygui.buttonbox("什么颜色","调颜色",
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
                        set_r = easygui.enterbox("R")
                        set_g = easygui.enterbox("G")
                        set_b = easygui.enterbox("B")
                        pen=(int(set_r),int(set_g),int(set_b))
                if Down == '调大小':
                    #选大小(不会英语,被迫的)
                    SizeTemp = easygui.buttonbox("多大","调大小",
                        choices = ['10','50','100','自定义'])
                    if SizeTemp == '20':
                        #设置大小为10
                        pen_size = 10
                    if SizeTemp == '50':
                        #设置大小为50
                        pen_size = 50
                    if SizeTemp == '100':
                        #设置大小为100
                        pen_size = 100
                    if SizeTemp == '自定义':
                        #用户自定义大小
                        InuptSizeTemp = easygui.enterbox("多大","自定义大小")
                        pen_size = InuptSizeTemp
                if Down == '清空屏幕':
                    #清空屏幕
                    screen.fill([255,255,255])


    if mouse_down:
        #绘制
        spot=pygame.mouse.get_pos()
        pygame.draw.circle(screen,pen,spot,int(pen_size))
        pygame.display.update()
pygame.quit()
