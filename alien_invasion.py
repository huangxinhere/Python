#encoding:utf-8
import pygame
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

 
def run_game():
	# ��ʼ����Ϸ������һ����Ļ����
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	# ����play��ť
	play_button = Button(ai_settings,screen,"Play")
	
	# ����һ�����ڴ洢��Ϸͳ����Ϣ��ʵ��
	stats = GameStats(ai_settings)
	
	# ����һ�ҷɴ���һ�����ڴ洢�ӵ��ı��顢һ�������˱���
	ship = Ship(ai_settings,screen)
	bullets = Group()
	aliens = Group()
	
	# ����������Ⱥ
	gf.create_fleet(ai_settings,screen,ship,aliens)
	
	# ��ʼ��Ϸ����ѭ��
	while True:
		gf.check_events(ai_settings,screen,stats,play_button,ship,
			bullets)
		
		if stats.game_active: 
			ship.update()
			gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
			gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
			
		gf.update_screen(ai_settings,screen,stats,ship,aliens,bullets,
			play_button)

run_game()

