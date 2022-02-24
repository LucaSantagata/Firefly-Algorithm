#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from numpy import exp
from numpy import sqrt
from numpy import cos
from numpy import sin
from numpy import e
from numpy import pi
from numpy import absolute

def Easom_2(individual):
    x1 = individual[0]
    x2 = individual[1]

    return -cos(x1)*cos(x2)*exp( -(x1-pi)**2 - (x2-pi)**2   ),

def Dropwave_2(individual):
    x1 = individual[0]
    x2 = individual[1]

    b = 0.5 * (x1 * x1 + x2 * x2) + 2
    a = -(1 + cos(12 * sqrt(x1 * x1 + x2 * x2))) / b
    return a,



def Eggholder_2(individual):
    x = individual[0]
    y = individual[1]

    return (-(y + 47.0) * np.sin(np.sqrt(abs(x/2.0 + (y + 47.0)))) - x * np.sin(np.sqrt(abs(x - (y + 47.0))))),

def three_hump_camel_function(individual):
    x = individual[0]
    y = individual[1]

    return 2*(x**2) - 1.05*(x**4) + (1/6)*(x**6) + x*y + (y**2),

def Levy_2(individual):
    x1 = individual[0]
    x2 = individual[1]

    return (sin(3*pi*x1))**2 + ((x1-1)**2)*(1+(sin(3*pi*x2))**2) + ((x2-1)**2)*(1+(sin(2*pi*x2))**2),


def Shubert_2(individual):
    x1= individual[0]
    x2 = individual[1]
    sum1 = 0
    sum2 = 0
    for i in range(1, 6):
        sum1 = sum1 + (i * cos(((i + 1) * x1) + i))
        sum2 = sum2 + (i * cos(((i + 1) * x2) + i))
    return sum1 * sum2,



def Ackley_2(individual):
    x1 = individual[0]
    x2 = individual[1]

    return -20.0 * exp(-0.2 * sqrt(0.5 * (x1**2 + x2**2))) -exp(0.5 * ( cos(2 *pi * x1) +cos(2 * pi * x2)  )) + e + 20,


def Ackley_10(individual):  # estraggo la x e la y dei punti
    x1 = individual[0]
    x2 = individual[1]
    x3 = individual[2]
    x4 = individual[3]
    x5 = individual[4]
    x6 = individual[5]
    x7 = individual[6]
    x8 = individual[7]
    x9 = individual[8]
    x10 = individual[9]

    return -20.0 * exp(-0.2 * sqrt(0.1 * (x1**2 + x2**2 +x3**2 +x4**2 +x5**2 +x6**2 +x7**2 +x8**2 +x9**2 +x10**2))) -exp(0.1 * ( cos(2 *pi * x1) +cos(2 * pi * x2) +cos(2 * pi * x3) +cos(2 * pi * x4) +cos(2 * pi * x5) +cos(2 * pi * x6) +cos(2 * pi * x7) +cos(2 * pi * x8) +cos(2 * pi * x9)+cos(2 * pi * x10) )) + e + 20,







def Rastrigin_2(individual):  # estraggo la x e la y dei punti
    x1 = individual[0]
    x2 = individual[1]

    return 10*2 + (x1**2 - 10*cos(2*pi*x1)) + (x2**2 - 10*cos(2*pi*x2)),



def Rastrigin_10(individual):  # estraggo la x e la y dei punti
    x1 = individual[0]
    x2 = individual[1]
    x3 = individual[2]
    x4 = individual[3]
    x5 = individual[4]
    x6 = individual[5]
    x7 = individual[6]
    x8 = individual[7]
    x9 = individual[8]
    x10 = individual[9]

    return 10*10 + (x1**2 - 10*cos(2*pi*x1)) + (x2**2 - 10*cos(2*pi*x2))+ (x3**2 - 10*cos(2*pi*x3)) + (x4**2 - 10*cos(2*pi*x4)) +(x5**2 - 10*cos(2*pi*x5)) +(x6**2 - 10*cos(2*pi*x6)) +(x7**2 - 10*cos(2*pi*x7)) +(x8**2 - 10*cos(2*pi*x8)) +(x9**2 - 10*cos(2*pi*x9)) +(x10**2 - 10*cos(2*pi*x10)),







def Rosenbrock_2(individual):
    x1 = individual[0]
    x2 = individual[1]

    return ( 100*(x2-x1**2)**2 + (x1-1)**2 ),

def Rosenbrock_3(individual):
    x1 = individual[0]
    x2 = individual[1]
    x3 = individual[2]

    return ( 100*(x3-x2**2)**2 + (x2-1)**2 + 100*(x2-x1**2)**2 + (x1-1)**2),



def Rosenbrock_10(individual):
    x1 = individual[0]
    x2 = individual[1]
    x3 = individual[2]
    x4 = individual[3]
    x5 = individual[4]
    x6 = individual[5]
    x7 = individual[6]
    x8 = individual[7]
    x9 = individual[8]
    x10 = individual[9]

    return ( (100*(x2-x1**2)**2 + (x1-1)**2) + (100*(x3-x2**2)**2 + (x2-1)**2) +(100*(x4-x3**2)**2 + (x3-1)**2) +(100*(x5-x4**2)**2 + (x4-1)**2) +(100*(x6-x5**2)**2 + (x5-1)**2) +(100*(x7-x6**2)**2 + (x6-1)**2) +(100*(x8-x7**2)**2 + (x7-1)**2) +(100*(x9-x8**2)**2 + (x8-1)**2) +(100*(x10-x9**2)**2 + (x9-1)**2) ),




def Shpere_2(individual):
    x1 = individual[0]
    x2 = individual[1]

    return x1**2 + x2**2,

def Shpere_3(individual):
    x1 = individual[0]
    x2 = individual[1]
    x3 = individual[2]

    return x1**2 + x2**2 + x3**2,


def Sphere_10(individual):
    x1 = individual[0]
    x2 = individual[1]
    x3 = individual[2]
    x4 = individual[3]
    x5 = individual[4]
    x6 = individual[5]
    x7 = individual[6]
    x8 = individual[7]
    x9 = individual[8]
    x10 = individual[9]

    return x1 ** 2 + x2 ** 2 + x3 ** 2 + x4 ** 2 + x5 ** 2 + x6 ** 2 + x7 ** 2 + x8 ** 2 + x9 ** 2 + x10 ** 2,


def Sphere_20(individual):
    x1 = individual[0]
    x2 = individual[1]
    x3 = individual[2]
    x4 = individual[3]
    x5 = individual[4]
    x6 = individual[5]
    x7 = individual[6]
    x8 = individual[7]
    x9 = individual[8]
    x10 = individual[9]
    x11 = individual[10]
    x12 = individual[11]
    x13 = individual[12]
    x14 = individual[13]
    x15= individual[14]
    x16 = individual[15]
    x17 = individual[16]
    x18 = individual[17]
    x19 = individual[18]
    x20 = individual[18]


    return x1 ** 2 + x2 ** 2 + x3 ** 2 + x4 ** 2 + x5 ** 2 + x6 ** 2 + x7 ** 2 + x8 ** 2 + x9 ** 2 + x10 ** 2+ x11 ** 2+ x12 ** 2+ x13 ** 2+ x14 ** 2+ x15 ** 2+ x16 ** 2+ x17 ** 2+ x18 ** 2+ x19 ** 2+ x20 ** 2,


# In[ ]:




