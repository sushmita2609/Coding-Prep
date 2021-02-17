#!/usr/bin/env python
# coding: utf-8

# In[34]:


def merge(arr1,arr2,n,m):
    #code here
    arr1.extend(arr2)
    arr1.sort()
    del arr2[:]
    arr2=arr1[n:]
    arr1=arr1[:n]
    arr1
    arr2
    return arr1,arr2
    
    
arr1 = [10,12] 
arr2 = [5,18,20]
N=len(arr1)
M=len(arr2)
res=merge(arr1,arr2,N,M)
res


# In[ ]:




