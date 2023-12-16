import matplotlib.pyplot as plt
import numpy as np

E = []
T = []

with open('grafick.txt','r') as f:
    f.__next__()
    for line in f:
        e,t = line.split()
        E.append(float(e))
        T.append(float(t))
print(E,T)
# T.sort(reverse=True)
# i = 0
# while i < len(T) - 1:
#     j = 0
#     while j < len(T) - 1 - i:
#         if T[j] > T[j+1]:
#             T[j], T[j+1] = T[j+1], T[j]
#         j += 1
#     i += 1
plt.plot(T,E)
plt.xticks(np.arange(0, max(T)+1, 100.))
plt.show()