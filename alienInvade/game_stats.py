#coding=UTF-8
'''
Created on 2018年7月23日

@author: Administrator
'''
class GameStats():
    """跟踪游戏的统计信息"""
    
    def __init__(self,ai_sittings):
        """初始化统计信息"""
        self.ai_settings = ai_sittings
        self.reset_status()
        #游戏刚启动时处于非活动状态
        self.game_active = False
        
    def reset_status(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit#飞船数量