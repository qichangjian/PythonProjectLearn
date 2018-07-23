#coding=UTF-8
'''
Created on 2018年7月19日

@author: Administrator

   通过创建模块game_functions，可避免alien_invasion.py太长，并使其逻辑更容易理解。
'''
import sys
from time import sleep

import pygame

from alienInvade.alien import Alien
from alienInvade.bullet import Bullet


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
    elif event.key == pygame.K_q:#不用关闭窗口了，直接按q就可以关闭窗口
        sys.exit()
        
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

def update_screen(ai_settings,screen,ship,aliens,bullets):
    """更新屏幕上的图像 并切换到新屏幕"""
    #每次循环时候都会重绘屏幕
    #用背景色填充屏幕；这个方法只接受一个实参：一种颜色
    screen.fill(ai_settings.bg_color)
    #在飞船和外星人后面重绘所有子弹
    '''方法bullets.sprites()返回一个列表，其中包含编组bullets中的所有精灵'''
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #调用ship中的方法绘制飞机
    ship.blitme()
    #使用alien中的方法绘制外星人aliens.blitme(screen)
    aliens.draw(screen)#aliens.draw(screen)在屏幕上绘制编组中的每个外星人
               
    #让最近绘制的屏幕可见，不断更新屏幕，隐藏原来的屏幕
    pygame.display.flip()      
    
def update_bullets(ai_settings,screen,ship,aliens,bullets):
    """更新子弹的位置 并删除已经消失的子弹"""
    #更新子弹的位置
    bullets.update()
    #print("刷新：" + str(len(bullets)))
    #删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #调用子弹和外星人碰撞的方法
    check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets)
    
def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets):   
    """相应子弹和外星人的碰撞"""
    #删除发生碰撞的子弹和外星人
    #检查是否有子弹击中外星人，
    #如果是这样，就删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    '''说明：
    新增的这行代码遍历编组bullets中的每颗子弹，再遍历编组aliens中的每个外星人。每当
有子弹和外星人的rect重叠时，groupcollide()就在它返回的字典中添加一个键值对。两个实参
True告诉Pygame删除发生碰撞的子弹和外星人。（要模拟能够穿行到屏幕顶端的高能子弹——消
灭它击中的每个外星人，可将第一个布尔实参设置为False，并让第二个布尔实参为True。这样
被击中的外星人将消失，但所有的子弹都始终有效，直到抵达屏幕顶端后消失。）
    '''
    if len(aliens) == 0:
        #删除现有子弹并创建一群外星人
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)#调用创建新外星人群的的方法

def fire_bullet(ai_settings,screen,ship,bullets):
    """如果还没有达到限制，就发射一颗子弹"""
    #创建新子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        #创建一个子弹，并将其加入到编组bullets中
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet) 
        
def create_fleet(ai_settings,screen,ship,aliens):
    """创建外星人群"""
    #创建一个外星人，并计算一行可容纳多少个外星人
    #外星人间距为外星人宽度
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
   
    #创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)
        
def get_number_aliens_x(ai_settings,alien_width):
    #计算每行能够容纳多少外星人
    #可利用的屏幕宽度
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))
    return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    #创建一个外星人并将其加入当前行
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2*alien_width*alien_number#设置x坐标将其加入当前行
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height * row_number
    aliens.add(alien)
    
def get_number_rows(ai_settings,ship_height,alien_height):
    """计算屏幕可容纳多少行外星人"""
    #可利用的屏幕高度
    #将屏幕高度减去第一行外星人的上边距（外星人高度）、飞船的高度以及最初外星人群与飞船的距离（外星人高度的两倍）：
    available_apace_y = (ai_settings.screen_height - (3*alien_height) - ship_height)
    number_row = int(available_apace_y/(2*alien_height))
    return number_row

def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
    """检查是否有外星人位于拼命边缘 并更新整群外星人的位置"""
    check_fleet_edges(ai_settings,aliens)
    #更新外星人群中所有外星人的位置的位置
    aliens.update()
    #检测外星人和飞船相撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets)#调用方法
        #print("Ship Hit!!!")
    #检查是否有外星人到达屏幕低端
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)
    
def check_fleet_edges(ai_sittings,aliens):
    """有外星人到达屏幕边缘"""
    '''方法aliens.sprites()返回一个列表，其中包含编组aliens中的所有精灵'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_sittings,aliens)#调用下移改变方向方法
            break
        
def change_fleet_direction(ai_sittings,aliens):
    """将整群外星人下移 并改变方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_sittings.fleet_drop_speed
    ai_sittings.fleet_direction *= -1 #设置为相反方向
        
        
def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        #将ships_left减1
        stats.ships_left -= 1    #飞船数量 
        #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        #创建一群新的外星人，并将飞船放在屏幕底部中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        #暂停
        sleep(0.5)
    else:
        stats.game_active = False
    
        
def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
    """检查是否有外星人到达屏幕低端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #像飞船被撞一样进行处理
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)#调用方法
            break
    

        