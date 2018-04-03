from Wafer import Wafer
import matplotlib.pyplot as plt

W = Wafer(0.001,'n',5e16,1.0e-9)
x = []
for i in range(int(W.thick / W.res)):
	x.append(i * W.res)

W.predep(25*60,900,'p',1.1e20)
W.drivein(3*60*60,1000,'p')
W.drivein(2*60*60,1100,'p')

xj = W.extract_xj()

print xj

plt.plot(x, W.net_profile)
plt.show()

