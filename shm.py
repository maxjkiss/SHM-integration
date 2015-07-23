from numpy import pi, zeros, sin
from pylab import plot,show,xlabel,ylabel
import matplotlib.pyplot as plt

#~~~~~~~~~~~ Forward Euler Method ~~~~~~~~~~~
x,y,t = [],[],[]
h,i,j = pi/10,0,0
x.append(0), y.append(1), t.append(0)

while True:
	if(t[i] > 8*pi):
		break
	x.append(x[i]+y[i]*h)
	y.append(y[i]-x[i]*h)
	t.append(t[i]+h)
	i = i + 1

#~~~~~~~~~~~ Velocity Verlet Scheme ~~~~~~~~~~~
def a(x):
	return -x

r, v, t2 = [],[],[]
r.append(0), v.append(1), t2.append(0)

while True:
	if(t2[j] > 8*pi):
		break
	v.append(v[j] + h*a(r[j]))
	r.append(r[j] + h*v[j+1])
	t2.append(t[j] + h)
	j = j + 1

#~~~~~~~~~~~ Plotting ~~~~~~~~~~~
plt.plot(t, x)
plt.plot(t2, r)
plt.plot(t, sin(t))
plt.title("Methods of Integration of SHM")
xlabel("t")
ylabel("x(t)")
plt.legend(['Forward Euler','Verlet Method', 'Exact Solution'])
show()


