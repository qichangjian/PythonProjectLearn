#coding=UTF-8
'''
Created on 2018年7月19日

@author: Administrator
introduce:
    创建一个空的Pygame窗口
'''

import pygame
from pygame.sprite import Group
from alienInvade.settings import Settings
from alienInvade.ship import Ship
import alienInvade.game_functions as gf
from alienInvade.game_stats import GameStats
from alienInvade.button import Button


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
    
    #创建Play按钮
    play_button = Button(ai_settings,screen,"Play")
    
    #创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    
    #创建一艘飞船，一个子弹编组和一个外星人编组
    #创建一艘飞船
    ship = Ship(ai_settings,screen)
    #创建一个用于存储子弹的编组
    bullets = Group()
    #创建一个外星人alien = Alien(ai_settings,screen)
    #创建一根外星人编组
    aliens = Group()
    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)
    
    #开始游戏的主循环
    while True:
        #调用game_function中监视键盘和鼠标的函数
        gf.check_events(ai_settings,screen,stats,play_button,ship,bullets)
        if stats.game_active:
            #检测事件后就跟新
            ship.update() 
            #删除已经消失的子弹
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            #更新每个外星人的位置
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
        
        #调用game_function中更新屏幕的函数
        gf.update_screen(ai_settings, screen,stats,ship,aliens,bullets,play_button)
        
run_game()
                
                                     
    