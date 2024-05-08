def space(km, mt, cm, mm, mc, nm):
	#km mt cm mm mc nm
	
	nanometro = 1;
	micrometro = nanometro * 1000;
	milimetro = micrometro * 1000;
	centimetro = milimetro * 10;
	metro = centimetro * 100;
	kilometro = metro * 1000;
	
	nm *= nanometro
	mc *= micrometro
	mm *= milimetro
	cm *= centimetro
	mt *= metro
	km *= kilometro
	
	return km + mt + cm + mm + mc + nm

def micrometros(space):
	micrometros = space/1000
	return micrometros

def milimetros(space):
	milimetros = space/1000000
	return milimetros
	
def centimetros(space):
	centimetros = space/10000000
	return centimetros
	
def metros(space):
	metros = space/1000000000
	return metros
	
def kilometros(space):
	kilometros = space/1000000000000
	return kilometros

"""

#Conversions

mc = space(0, 0, 0, 0, 1, 0)
mm = space(0, 0, 0, 1, 0, 0)
cm = space(0, 0, 1, 0, 0, 0)
mt = space(0, 1, 0, 0, 0, 0)
km = space(1, 0, 0, 0, 0, 0)
print("km\t\t", "mt\t", "cm\t", "mm \t", "mc\t")
print(km, mt, cm, mm, mc)

"""


	

