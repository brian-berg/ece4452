from DealGrove import DealGrove

def mins2hrs(mins):
	# helper function to convert minutes to hours for the model
	return float(mins/60.0)
	

FieldOxide = DealGrove()
Test1 = DealGrove()
Test2 = DealGrove()

#First Field Oxide, Diffusion Mask for P-Well
FieldOxide.grow(mins2hrs(5),.090,.027,tau = .076)
FieldOxide.grow(mins2hrs(15),.11,.51)
FieldOxide.grow(mins2hrs(5),.090,.027)

print FieldOxide.ox_thick
print ''

# Diffusion Mask for P+ Diffusion
# Using the A, B, Tau numbers for 1200C, actual process was 1175C
FieldOxide.grow(mins2hrs(10),.04,.045)
Test1.grow(mins2hrs(10),.04,.045,tau = .027)

print FieldOxide.ox_thick
print Test1.ox_thick
print ''

#Field Oxidation, Diffusion Mask for N+ Diffusion
FieldOxide.grow(mins2hrs(5),.090,.027)
FieldOxide.grow(mins2hrs(15),.11,.51)
FieldOxide.grow(mins2hrs(5),.090,.027)

Test1.grow(mins2hrs(5),.090,.027)
Test1.grow(mins2hrs(15),.11,.51)
Test1.grow(mins2hrs(5),.090,.027)

Test2.grow(mins2hrs(5),.090,.027,tau = .076)
Test2.grow(mins2hrs(15),.11,.51)
Test2.grow(mins2hrs(5),.090,.027)

print FieldOxide.ox_thick
print Test1.ox_thick
print Test2.ox_thick
print ''

# Field Oxide Measured after etching oxide from gate areas in preparation for Gate Oxide Growth
# Etch amount estimated from measured data
FieldOxide.etch(.02)
Test1.etch()
Test2.etch()

print FieldOxide.ox_thick
print ''

# Gate Oxide Growth
FieldOxide.grow(mins2hrs(40),.165,.0117)
Test1.grow(mins2hrs(40),.165,.0117, tau = 0.37)
Test2.grow(mins2hrs(40),.165,.0117, tau = 0.37)

print FieldOxide.ox_thick
print Test1.ox_thick
print Test2.ox_thick
print ''