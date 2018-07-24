#coding=UTF-8
'''
Created on 2018年7月24日

@author: Administrator

由于Pygame没有内置创建按钮的方法，我们创建一个Button类，用于创建带标签的实心矩形
'''
import pygame.font#导入了模块pygame.font，它让Pygame能够将文本渲染到屏幕


class Button():
    
    def __init__(self,ai_settings,screen,msg):#msg是要在按钮中显示的文
        """初始化按钮的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        #设置按钮的尺寸和其他属性
        self.width,self.height = 200,50
        self.button_color = (0,255,0)#button_color让按钮的rect对象为亮绿色
        self.text_color = (255,255,255)#text_color让文本为白色。
        self.font = pygame.font.SysFont(None,48)#实参None让Pygame使用默认字体，而48指定了文本的字号
        
        #创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0,0,self.width,self.height)#为让按钮在屏幕上居中，我们创建一个表示按钮的rect对象
        self.rect.center = self.screen_rect.center#其center属性设置为屏幕的center属性。
        
        #按钮的标签只需要创建一次
        self.prep_msg(msg) #Pygame通过将你要显示的字符串渲染为图像来处理文本
        
    def prep_msg(self,msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        #。调用font.render()将存储在msg中的文本转换为图像，然后将该图像存储在msg_image中
        #方法font.render()还接受一个布尔实参，该实参指定开启还是关闭反锯齿功能（反锯齿让文本的边缘更平滑）。余下的两个实参分别是文本颜色和背景色
        #（如果没有指定背景色，Pygame将以透明背景的方式渲染文本）。
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect() #根据文本图像创建一个rect
        self.msg_image_rect.center = self.rect.center#并将其center属性设置为按钮的center属性。
        
    
    def draw_button(self):
        #绘制一个用颜色填充的按钮，在绘制文本
        self.screen.fill(self.button_color,self.rect)#调用screen.fill()来绘制表示按钮的矩形，
        self.screen.blit(self.msg_image,self.msg_image_rect) #再调用screen.blit()，并向它传递一幅图像以及与该图像相关联的rect对象，从而在屏幕上绘制文本图像。
        
        
        
        
        
        
        