
class Employee:
	def __init__(self,fun):
		self.emp=[] #tablica podwładnych
		self.fun=fun
		self.g=-1
		self.f=-1


#funkcja f(v)-najlepsza impreza w T(v)
#g(v)-najlepsza impreza w T(v) na którą v nie idzie

def f(v):
	if v.f>=0:
		return v.f
	x=v.f
	for vi in v.emp:
		x+=g(vi)
	y=g(v)
	v.f=max(x,y)
	return v.f

def g(v):
	if v.g>=0:
		return v.g
	v.g=0
	for vi in v.emp:
		v.g+=f(vi)
	return v.g

