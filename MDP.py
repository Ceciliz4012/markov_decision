
import numpy as np

# need to use 3-d array to represend all info

p = [[[0.3, 0.7, 0, 0, 0], [0.7, 0.3, 0, 0, 0]],
     [[0.3, 0, 0.7, 0, 0], [0.7, 0, 0.3, 0, 0]],
     [[0.3, 0, 0, 0.7, 0], [0.7, 0, 0, 0.3, 0]],
     [[0.3, 0, 0, 0, 0.7], [0.7, 0, 0, 0, 0.3]],
     [[0.3, 0, 0, 0, 0.7], [0.7, 0, 0, 0, 0.3]]]

r = [[[3, 0, 0, 0, 0], [3, 0, 0, 0, 0]],
     [[3, 0, 0, 0, 0], [3, 0, 0, 0, 0]],
     [[3, 0, 0, 0, 0], [3, 0, 0, 0, 0]],
     [[3, 0, 0, 0, 0], [3, 0, 0, 0, 0]],
     [[3, 0, 0, 0, 10], [3, 0, 0, 0, 10]]]


stop = 0.001
p = np.array(p)
r = np.array(r)

v = np.zeros([5, 1])

thresh = float('inf') 

state = np.array([1, 2, 3, 4, 5])
action = np.array([0, 1])

t = 0
while thresh >= stop:
    
    temp = np.copy(v)

    for i in range(len(state)):
        m = float('-inf') 
        for j in range(len(action)):
            s = 0
            for k in range(len(state)):
                s = s + ((r[i, j, k] + 0.9 * temp[k]) * p[i, j, k])
            m = max(m, s)
        v[i] = m
    diff = abs(temp - v)
    thresh = max(diff)
    t += 1

print(v)

pres = np.zeros([5, 1])
qres = np.zeros([5, 2])
vv = np.copy(v)

for i in range(len(state)):
    for j in range(len(action)):
        s = 0    
        for k in range(len(state)):
            s = s + ((r[i, j, k] + 0.9 * vv[k]) * p[i, j, k])
        qres[i, j] = s
    pres[i] = np.argmax(qres[i])        

print(qres)
print(pres)

