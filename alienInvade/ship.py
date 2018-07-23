#coding=UTF-8
'''
Created on 2018年7月19日

@author: Administrator
'''
import pygame


class Ship():
    
    def __init__(self,ai_settings,screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen#后边屏幕
        self.ai_settings = ai_settings
        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()#rect的意思是对象的区块大小，他把大小设定为图片的大小
        self.screen_rect = screen.get_rect()#我们将把飞船放在屏幕底部中央。为此，首先将表示屏幕的矩形存储在self.screen_rect
        
        #将每艘新飞船放在屏幕底部中央
        #飞船中心的x坐标:self.rect.centerx 飞船下边缘的y坐标:self.rect.bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        
        #移动标志，当按下箭头的时候就移动
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right: #限制飞船的活动范围
            self.center += self.ai_settings.ship_speed_factor              #更新飞船的center值，而不是rect
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor
        #根据self.center跟新rect对象
        self.rect.centerx = self.center
        
    def blitme(self):
        """在指定位置绘制飞船"""
        #它根据self.rect指定的位置将图像绘制到屏幕上
        self.screen.blit(self.image,self.rect)
    
    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx
        