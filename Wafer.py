import numpy
import math

class Wafer:
	def __init__(self, t, dop_type, dop_conc, res = 1.0e-8):
		# Thickness in cm
		self.thick = t
		# Check dopant type is valid
		if (dop_type != 'p' and dop_type != 'n'):
			print "Invalid dopant type! Must be p or n!"
		self.type = dop_type
		
		# Background concentration
		self.bg_conc = dop_conc
		# Distance domain resolution in cm
		self.res = res
		
		# Create initial doping profile with background concentration
		self.n_profile = []
		self.p_profile = []
		self.net_profile = []
		self.abs_profile = []
		
		for i in range(int(self.thick / self.res)):
			if self.type == 'n':
				self.n_profile.append(self.bg_conc)
				self.p_profile.append(0.0)
				self.net_profile.append(self.bg_conc)
				self.abs_profile.append(0.0)
			else:
				self.p_profile.append(self.bg_conc)
				self.n_profile.append(0.0)
				self.net_profile.append(self.bg_conc)
				self.abs_profile.append(0.0)
		
		# Initialize a list to contain the doses
		# Positive doses are p, Negative doses are n
		self.dose = []
		
		self.Dt = []
		
		# Activation Energy
		self.Ea = 3.690
		
		
	def calc_Dt(self, time, Temp):
		D = 10.500 * math.exp(-1.000 * self.Ea / (8.614e-5 * (Temp + 273.0)) )
		print "D"
		print D
		new_Dt = D * time
		print "Dt"
		print new_Dt
		self.Dt.append(new_Dt)
		print "Dt_eff"
		print sum(self.Dt)
		return sum(self.Dt)
		
	def updateDose(self):
		n_dose_sum = 0
		p_dose_sum = 0
		for x in self.dose:
			if x <= 0:
				n_dose_sum = n_dose_sum + x
			else:
				p_dose_sum = p_dose_sum + x
		self.dose = [n_dose_sum, p_dose_sum]
	
	def updateNetProfile(self):
		for x in range(len(self.net_profile)):
			
			if self.type == 'n':
				self.net_profile[x] = abs( self.p_profile[x] - self.n_profile[x] )
				
			if self.type == 'p':
				self.net_profile[x] = abs( self.n_profile[x] - self.p_profile[x] )
				
			self.abs_profile[x] = self.p_profile[x] - self.n_profile[x]
		
	def drivein(self, time, Temp, dop, calcDt = True, Dt_steps = 0):
		# Drives in one type of dopant
		# Check for dopant type
		if (dop != 'p' and dop != 'n'):
			print "Invalid dopant type! Must be p or n!"
		# Check for dose
		if len(self.dose) == 0:
			print "Must predep before Drive-in!"
		
		# Calculate Dt
		if calcDt:
			Dt = self.calc_Dt(time, Temp)
		elif not calcDt and Dt_steps > 0:
			Dt = sum(self.Dt[-1*Dt_steps:])
		else:
			Dt = sum(self.Dt)
		
		for dose in self.dose:
			if dose > 0 and dop == 'p':
				for x in range(len(self.p_profile)):
					new_profile = dose / math.sqrt(math.pi * Dt) * math.exp(-1.0 * math.pow((x * self.res),2.0) / (4.0 * Dt))
					if new_profile < 0:
						new_profile = 0.0
					self.p_profile[x] = new_profile
			if dose <= 0 and dop == 'n':
				for x in range(len(self.n_profile)):
					new_profile = -1.0 * dose / math.sqrt(math.pi * Dt) * math.exp(-1.0 * math.pow((x * self.res),2.0) / (4.0 * Dt))
					if new_profile < 0:
						new_profile = 0.0
					self.n_profile[x] = new_profile

		# Add in background doping
		if dop == self.type:
			if self.type == 'p':
				for x in range(len(self.p_profile)):
					self.p_profile[x] = self.p_profile[x] + self.bg_conc
			if self.type == 'n':
				for x in range(len(self.n_profile)):
					self.n_profile[x] = self.n_profile[x] + self.bg_conc
		
		# Update Net Profile
		self.updateNetProfile()
			
		
		
	def predep(self, time, Temp, dop, conc):
		# This function is called to perform a predeposition step.  It will additionally perform diffusions on any previously diffused material
		# Check for dopant type
		if (dop != 'p' and dop != 'n'):
			print "Invalid dopant type! Must be p or n!"
		
		# Calculation of Diffusion Coefficient
		Dt = self.calc_Dt(time, Temp)
		Dt = self.Dt[-1]
		
		# If previous depositions, perform drive-in
		if len(self.dose) != 0:
			if self.dose[0] != 0:
				self.drivein(time, Temp, 'n', False)
			if self.dose[1] != 0:
				self.drivein(time, Temp, 'p', False)
		
		if dop == 'n':
			for x in range(len(self.n_profile)):
				new_diffused = conc * math.erfc((float(x) * self.res) / (2.0 * math.sqrt(Dt)))
				if new_diffused < 0:
					new_diffused = 0.0
				self.n_profile[x] = self.n_profile[x] + new_diffused
			new_dose = 2.0 * conc / math.sqrt(math.pi) * math.sqrt(Dt)
			self.dose.append(-1.0 * new_dose)
		if dop == 'p':
			for x in range(len(self.p_profile)):
				new_diffused = conc * math.erfc((float(x) * self.res) / (2.0 * math.sqrt(Dt)))
				if new_diffused < 0:
					new_diffused = 0.0
				self.p_profile[x] = self.p_profile[x] + new_diffused
			new_dose = 2.0 * conc / math.sqrt(math.pi) * math.sqrt(Dt)
			self.dose.append(new_dose)
		
		# Update dose with sum of doses of the same type
		self.updateDose()
		# Update net profile
		self.updateNetProfile()
		# print self.net_profile
			
	def extract_xj(self):
		xj = []
		x2 = []
		
		# Get zero crossings from absolute doping profile
		xj = numpy.where(numpy.diff(numpy.sign(self.abs_profile)))[0]
		
		# Convert zero crossing indices to real distance
		for x in range(len(xj)):
			x2.append( float(xj[x]) * self.res )
		
		return x2

			
			
			
			
			
			