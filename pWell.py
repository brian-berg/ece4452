from Wafer import Wafer
import matplotlib.pyplot as plt

W = Wafer(0.002,'n',2.22e15,1.0e-9)
x = []

# Create x for plots
for i in range(int(W.thick / W.res)):
	x.append(i * W.res)



# P-well Predeposition
print "P-well Predeposition"
W.predep(14*60,890,'p',1.1e20)
xj = W.extract_xj()
print "xj"
print xj
print "Cs"
print W.p_profile[0]
plt.figure(1)
plt.subplot(211)
plt.title('P-well Predeposition')
plt.grid(True)
plt.yscale('log')
plt.ylabel('Concentration (/cm^2)')
plt.xlabel('Distance form Surface (cm)')
plt.plot(x, W.net_profile)
plt.subplot(212)
plt.grid(True)
plt.yscale('log')
plt.ylabel('Concentration (/cm^2)')
plt.xlabel('Distance form Surface (cm)')
plt.plot(x, W.p_profile)
plt.plot(x, W.n_profile)

# P-well Drive-in
print "P-well Drive-in"
W.drivein(6*60*60,1175,'p')
xj = W.extract_xj()

print "xj"
print xj
print "Cs"
print W.p_profile[0]
plt.figure(2)
plt.subplot(211)
plt.title('P-well Drivein')
plt.grid(True)
plt.yscale('log')
plt.ylabel('Concentration (/cm^2)')
plt.xlabel('Distance form Surface (cm)')
plt.plot(x, W.net_profile)
plt.subplot(212)
plt.grid(True)
plt.yscale('log')
plt.ylabel('Concentration (/cm^2)')
plt.xlabel('Distance form Surface (cm)')
plt.plot(x, W.p_profile)
plt.plot(x, W.n_profile)

# P+ S/D Predep
print "P+ S/D Predeposition"
W.drivein(30*60,935,'p')
xj = W.extract_xj()
print "xj"
print xj
print "Cs"
print W.p_profile[0]
plt.figure(3)
plt.subplot(211)
plt.title('P+ S/D Predep')
plt.grid(True)
plt.yscale('log')
plt.ylabel('Concentration (/cm^2)')
plt.xlabel('Distance form Surface (cm)')
plt.plot(x, W.net_profile)
plt.subplot(212)
plt.grid(True)
plt.yscale('log')
plt.ylabel('Concentration (/cm^2)')
plt.xlabel('Distance form Surface (cm)')
plt.plot(x, W.p_profile, label = "P-well Drivein")
plt.plot(x, W.n_profile)

# P+ S/D Drive-in
print "P+ S/D Drive-in"
W.drivein(25*60,1100,'p')
xj = W.extract_xj()
print "xj"
print xj
print "Cs"
print W.p_profile[0]
plt.figure(4)
plt.subplot(211)
plt.title('P+ S/D Drivein')
plt.grid(True)
plt.yscale('log')
plt.ylabel('Concentration (/cm^2)')
plt.xlabel('Distance form Surface (cm)')
plt.plot(x, W.net_profile)
plt.subplot(212)
plt.grid(True)
plt.yscale('log')
plt.ylabel('Concentration (/cm^2)')
plt.xlabel('Distance form Surface (cm)')
plt.plot(x, W.p_profile, label = "P-well Drivein")
plt.plot(x, W.n_profile)

# N+ S/D Predep
print "N+ S/D Predeposition"
W.predep(2*60*60,950,'n',7e20)
xj = W.extract_xj()
print "xj"
print xj
print "Cs, p"
print W.p_profile[0]
print "Cs, n"
print W.n_profile[0]
plt.figure(5)
plt.subplot(211)
plt.title('N+ S/D Predeposition')
plt.grid(True)
plt.yscale('log')
plt.ylabel('Concentration (/cm^2)')
plt.xlabel('Distance form Surface (cm)')
plt.plot(x, W.net_profile)
plt.subplot(212)
plt.grid(True)
plt.yscale('log')
plt.ylabel('Concentration (/cm^2)')
plt.xlabel('Distance form Surface (cm)')
plt.plot(x, W.p_profile, label = "P-well Drivein")
plt.plot(x, W.n_profile)

# N+ S/D Drive-in
print "N+ S/D Drive-in"
W.drivein(40*60,1000,'p')
W.drivein(40*60,1000,'n', False, 2)
xj = W.extract_xj()
print "xj"
print xj
print "Cs, p"
print W.p_profile[0]
print "Cs, n"
print W.n_profile[0]
plt.figure(6)
plt.subplot(211)
plt.title('N+ S/D Drivein')
plt.grid(True)
plt.yscale('log')
plt.ylabel('Concentration (/cm^2)')
plt.xlabel('Distance form Surface (cm)')
plt.plot(x, W.net_profile)
plt.subplot(212)
plt.grid(True)
plt.yscale('log')
plt.ylabel('Concentration (/cm^2)')
plt.xlabel('Distance form Surface (cm)')
plt.plot(x, W.p_profile, label = "P-well Drivein")
plt.plot(x, W.n_profile)

#print Dose info
print "Dose:"
print W.dose

plt.show()
