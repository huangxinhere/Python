class GameStats():
	# ������Ϸ��ͳ����Ϣ
	
	def __init__(self,ai_settings):
		self.ai_settings = ai_settings
		self.reset_stats()
		# ��Ӧ������߷�
		self.high_score = 0
		
		# ����ʱ���ڷǻ״̬
		self.game_active = False
		
	def reset_stats(self):
		# ��ʼ������Ϸ�ڼ���ܱ仯��ͳ����Ϣ
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1
