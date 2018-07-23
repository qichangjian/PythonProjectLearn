#coding=UTF-8
'''
Created on 2018年7月19日

@author: Administrator
introduce:
    创建一个空的Pygame窗口
'''

import pygame
from pygame.sprite import Group

import alien.game_functions as gf
from alien.settings import Settings
from alien.ship import Ship


def run_game():
    #初始化游戏并创建一个屏幕对象
    #初始化背景设置，让Pygame能够正确地工作
    pygame.init()
    
    #初始化pygame.设置Settings
    ai_settings = Settings()
    
    #们调用pygame.display.set_mode()来创建一个名为screen的显示窗口。
    #通过将这些尺寸值传递给pygame.display.set_mode()创建一个游戏窗口
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    #窗口的名称，左上角的名称
    pygame.display.set_caption("Alien Invasion")
    
    #创建一艘飞船
    ship = Ship(ai_settings,screen)
    #创建一个用于存储子弹的编组
    bullets = Group()
    
    #开始游戏的主循环
    while True:
        #调用game_function中监视键盘和鼠标的函数
        gf.check_events(ai_settings,screen,ship,bullets)
        #检测事件后就跟新
        ship.update()
          
        #删除已经消失的子弹
        gf.update_bullets(bullets)
        #调用game_function中更新屏幕的函数
        gf.update_screen(ai_settings, screen, ship,bullets)
        
run_game()
                
                                     
    