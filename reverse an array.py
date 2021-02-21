#!/usr/bin/env python
# coding: utf-8

# In[2]:


n = int(input())

while n:
    
    N = int(input())
    
    Arr = [int(x) for x in input().split()]
    
    Arr.reverse()
    
    for x in Arr:
        print(x, end=" ")
    
    print()
    
    n -= 1


# In[ ]:




