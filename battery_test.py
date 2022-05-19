"Battery test"
# test battery package

import matplotlib.pyplot as plt

import battery.battery as bat

mybat = bat.Battery()
print(mybat.voltage)


x=[]
y=[]


for v in range(280, 440, 1):
    vo = v/100.0
    p = mybat.charge(vo)
    x.append(vo)
    y.append(p)

plt.plot(x,y)
plt.xlabel('Volt')
plt.ylabel('%')
plt.show()

x=[]
y=[]

for p in range(1,100):
    po = p/100
    t=mybat.battery_time(po)
    x.append(po)
    y.append(t)
    print("time", po,p)

plt.plot(x,y)
plt.xlabel('charge %')
plt.ylabel('min left')
plt.show()
