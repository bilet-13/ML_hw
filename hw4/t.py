import numpy as np
import matplotlib.pyplot as plt

fdata = open("data.txt","r")
#handle file data
x = list()
y = list()
target = list()
maxx0 = -100
minx0 = 100
for line in fdata:
    data = line.split("\n")
    tx0 = float(data[0].split(",")[0])
    tx1 = float(data[0].split(",")[1])
    tx2 = float(data[0].split(",")[2])
    x.append(tx0)
    y.append(tx1)
    target.append(tx2)
    if tx0 < minx0:
        minx0 = tx0
    if tx0 > maxx0:
        maxx0 = tx0


def sig(x):
    return 1.0 / (1.0 + np.exp(-x))
def sig_der(x):
    return sig(x)*(1 - sig(x))

w = [0,1,-1,-1,1,-1,1]
b = [0,0,0]
ratio = 0.02
index = 0
while(1):
    index +=1
    error = 0
    w1 = 0
    w2 = 0
    w3 = 0
    w4 = 0
    w5 = 0
    w6 = 0
    b1 = 0
    b2 = 0
    for i in range(0,len(x)):
        z1 = w[1] * x[i] + w[2] * y[i] + b[1]
        z2 = w[3] * x[i] + w[4] * y[i] + b[1]
        f1 = sig(z1)
        f2 = sig(z2)
        z3 = w[5] * f1 + w[6] * f2 + b[2]
        a = sig(z3)
        error += (a - target[i]) * (a - target[i]) / 2
        dedf1 = (a - target[i]) * sig_der(z3) * w[5]
        dedf2 = (a - target[i]) * sig_der(z3) * w[6]
        w5 += (a - target[i]) * sig_der(z3) * f1
        w6 += (a - target[i]) * sig_der(z3) * f2
        w1 += dedf1 * sig_der(z1) * x[i]
        w2 += dedf1 * sig_der(z1) * y[i]
        w3 += dedf2 * sig_der(z2) * x[i]
        w4 += dedf2 * sig_der(z2) * y[i]
        b1 += dedf1 * sig_der(z1)
        b2 += (a - target[i]) * sig_der(z3)
    if error < 0.01:
        break
    if index % 1000 == 0:
        print("l2 norm error",index,":",error)
    w[1] -= ratio * w1
    w[2] -= ratio * w2
    w[3] -= ratio * w3
    w[4] -= ratio * w4
    w[5] -= ratio * w5
    w[6] -= ratio * w6
    b[1] -= ratio * b1
    b[2] -= ratio * b2
print("l2 norm error",index,":",error)
correct = 0
wrong = 0
fig, axs = plt.subplots(1, 2, constrained_layout=True)
px = np.linspace(minx0,maxx0,1000)
py = px
plt.figure()
for i in range(0,len(x)):
    z1 = w[1] * x[i] + w[2] * y[i] + b[1]
    z2 = w[3] * x[i] + w[4] * y[i] + b[1]
    f1 = sig(z1)
    f2 = sig(z2)
    z3 = w[5] * f1 + w[6] * f2 + b[2]
    a = sig(z3)
    if a <= 0.5:
        axs[0].scatter(x[i],y[i],color = 'red')
    else:
        axs[0].scatter(x[i],y[i],color = 'blue')
    if (a > 0.5 and x[i] < y[i]) or (a < 0.5 and x[i] > y[i]):
        correct += 1
    else:
        wrong +=1
axs[0].set_title('predict')
axs[0].plot(px,py,'g')
for i in range(0,len(x)):
    if target[i] == 0:
        axs[1].scatter(x[i],y[i],color = 'red')
    else:
        axs[1].scatter(x[i],y[i],color = 'blue')
axs[1].set_title('ground truth')
axs[1].plot(px,py,'g')
acc = correct / (correct + wrong)
print("accuracy:",acc)