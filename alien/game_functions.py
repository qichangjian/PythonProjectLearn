#coding=UTF-8
'''
Created on 2018年7月19日

@author: Administrator

   通过创建模块game_functions，可避免alien_invasion.py太长，并使其逻辑更容易理解。
'''
import sys

import pygame
from alien.bullet import Bullet

#鼠标按下
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        #向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        #向左边移动
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #调用发射子弹的方法
        fire_bullet(ai_settings,screen,ship,bullets)
        
#鼠标离开
def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

#事件响应       
def check_events(ai_sittings,screen,ship,bullets):
    """事件管理：监视键盘和鼠标"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #使用sys模块的exit方法退出
            sys.exit()
        #检查时间类型是否是keyword时间 箭头左右移动，控制飞船移动
        elif event.type == pygame.KEYDOWN:#鼠标按下
            check_keydown_events(event, ai_sittings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:#鼠标离开
            check_keyup_events(event, ship)

def update_screen(ai_settings,screen,ship,bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环时候都会重绘屏幕
    #用背景色填充屏幕；这个方法只接受一个实参：一种颜色
    screen.fill(ai_settings.bg_color)
    #在飞船和外星人后面重绘所有子弹
    '''方法bullets.sprites()返回一个列表，其中包含编组bullets中的所有精灵'''
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #调用ship中的方法绘制飞机
    ship.blitme()
               
    #让最近绘制的屏幕可见，不断更新屏幕，隐藏原来的屏幕
    pygame.display.flip()      
    
def update_bullets(bullets):
    """更新子弹的位置，并删除已经消失的子弹"""
    #更新子弹的位置
    bullets.update()
    #print("刷新：" + str(len(bullets)))
    #删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    

def fire_bullet(ai_settings,screen,ship,bullets):
    """如果还没有达到限制，就发射一颗子弹"""
    #创建新子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        #创建一个子弹，并将其加入到编组bullets中
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet) 