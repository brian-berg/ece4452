import math
class DealGrove:
	def __init__(self):
		# Current Oxide Thickness
		self.ox_thick = 0
		# Total Silicon Consumed
		self.si_consumed = 0
		# Used to track oxide growth
		self.ox_process = []
		
	def etch(self, etch_thick = -1):
	
		if etch_thick <= 0:
			# etches all oxide, leaving a clean wafer if no argument
			self.ox_process.append(-1 * self.ox_thick)
			self.ox_thick = 0
		else:
			# etches oxide to thickness of etch_thick
			self.ox_process.append(-1 * etch_thick)
			self.ox_thick = self.ox_thick - etch_thick
		
		
	def grow(self, time, A, B, tau = -1):
		
		tox = self.ox_thick
		
		if tau <= 0:
			tau = (math.pow(tox,2.0) + A * tox) / B
		
		tox = (-A + math.sqrt(math.pow(A,2.0) + 4.0 * B * (time + tau))) / 2.0
		
		self.ox_process.append(tox)
		self.ox_thick = tox