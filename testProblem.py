from Wafer import Wafer

W = Wafer(0.03,'n',5e16,1.0e-9)

W.predep(25*60,900,'p',1.1e20)
W.drivein(3*60*60,1000,'p')
W.drivein(2*60*60,1100,'p')

xj = W.extract_xj()

print xj

