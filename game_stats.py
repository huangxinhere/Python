class GameStats():
	# 跟踪游戏的统计信息
	
	def __init__(self,ai_settings):
		self.ai_settings = ai_settings
		self.reset_stats()
		# 不应重置最高分
		self.high_score = 0
		
		# 启动时处于非活动状态
		self.game_active = False
		
	def reset_stats(self):
		# 初始化在游戏期间可能变化的统计信息
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1
