#encoding:utf-8

class Settings():
	
	def __init__(self):
		
	# --静态设置--
		# 屏幕设置
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)
		# 飞船的设置
		self.ship_speed_factor = 1.5
		self.ship_limit = 3
		# 子弹设置
		self.bullet_width =400
		self.bullet_height = 15
		self.bullet_color = 60,60,60
		self.bullets_allowed = 3
		# 外星人设置
		self.fleet_drop_speed = 20
		
		# 加快游戏节奏
		self.speedup_scale = 1.1
		# 点数的提高速度
		self.score_scale = 1.5
		
		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
	# 动态设置
		self.ship_speed_factor = 2
		self.bullet_speed_factor = 4
		self.alien_speed_factor = 0.5
		
		# 1:右移，-1左移（方便），且对应坐标
		self.fleet_direction = 1
		# 计分
		self.alien_points = 50
	
	def increase_speed(self):
		# 提高速度
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		
		self.alien_points = int(self.alien_points * self.score_scale)
