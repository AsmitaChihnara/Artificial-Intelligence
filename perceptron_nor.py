# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 09:28:21 2018

@author: Asmita
"""

from random import choice
from numpy import array, dot, random
from pylab import plot, ylim
import matplotlib.pyplot as plt
import numpy as np

fig,ax = plt.subplots()

unit_step = lambda x: 0 if x < 0 else 1   #decide threshhold value

training_data = [
    (array([0,0,1]), 1),
    (array([0,1,1]), 0),
    (array([1,0,1]), 0),
    (array([1,1,1]), 0),
]

j=np.array([
        [0,0,1],
        [0,1,1],
        [1,0,1],
        [1,1,1],
        ])
w = random.rand(3)                      #take random weights
errors = []
eta = 0.2
n = 100

for i in xrange(n):
    x, expected = choice(training_data)
    result = dot(w, x)
    error = expected - unit_step(result)#update error
    errors.append(error)
    w += eta * error * x#update weight

list_out=[]
for x, _ in training_data:
    result = dot(x, w)
    print("{}: {} -> {}".format(x[:2], result, unit_step(result)))
    list_out.append(unit_step(result))
    
for d, sample in enumerate(j):
    if list_out[d] < 1:#negative result
        plt.scatter(sample[0], sample[1], s=120, marker='_', linewidths=2)
    else:#positive result
        plt.scatter(sample[0], sample[1], s=120, marker='+', linewidths=2)

# print line with possible hyperplane
plt.plot([0,0.9],[0.9,0])
plt.show()
plt.close()
ylim([-1,1])
plot(errors)