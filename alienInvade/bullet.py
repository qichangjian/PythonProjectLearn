#coding=UTF-8
'''
Created on 2018年7月20日

@author: Administrator
'''
from pygame.sprite import Sprite
import pygame


class Bullet(Sprite):
    """一个对飞船发射进行管理的类"""
    
    def __init__(self,ai_settings,screen,ship):
        """在飞船所处的位置创建一个子弹对象"""
        '''
                                        继承了我们从模块pygame.sprite中导入的Sprite类。
                                        通过使用精灵，可将游戏中相 关的元素编组，进而同时操作编组中的所有元素
                                        
                                        码super(Bullet, self).__init__()使用了Python 2.7语法。
                                        这种语法也适用于Python 3，但你也可以将这行代码简写为super().__init__()。
        '''
        super(Bullet,self).__init__() 
        self.screen = screen #后边的屏幕
        
        #在（0，0）处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        #设置正确的位置
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #存储用小数表示的子弹位置
        #我们将子弹的y坐标存储为小数值，以便能够微调子弹的速度
        self.y = float(self.rect.y)
        
        #设置子弹的颜色和数据
        self.color= ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
        
    def update(self):
        """向上移动子弹"""
        #更新表示子弹位置的小数值
        self.y -= self.speed_factor
        #更新表示子弹的rect的位置
        self.rect.y = self.y
        
    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
    
    
        