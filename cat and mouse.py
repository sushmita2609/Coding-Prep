#!/usr/bin/env python
# coding: utf-8

# In[3]:



import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    d1=abs(z-x)
    d2=abs(z-y)
    if(d1<d2):
        return "Cat A"
    elif(d2<d1):
        return "Cat B"
    elif(d1==d2):
        return "Mouse C"

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        print(catAndMouse(x, y, z))



# In[ ]:




