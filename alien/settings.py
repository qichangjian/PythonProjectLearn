#coding=UTF-8
'''
Created on 2018年7月19日

@author: Administrator

             用于将所有设置存储在一个地方，以免在代码中到处添加设置。
这样，我们就能传递一个设置对象，而不是众多不同的设置。另外，这让函数调用更简单，且在
项目增大时修改游戏的外观更容易：要修改游戏，只需修改settings.py中的一些值，而无需查找
散布在文件中的不同设置。
'''
class Settings():
    """存储《外星人入侵》的所有设置的类"""
    
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置 屏幕长度宽度和背景颜色
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        #飞船的移动速度
        self.ship_speed_factor = 1.5 
        #子弹的设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3 #3像素
        self.bullet_height = 15
        self.bullet_color = 60,60,60 #深灰色
        self.bullets_allowed = 3#存储所允许的最大子弹数：
        
        