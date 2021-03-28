#!/usr/bin/env python
# coding: utf-8

# In[15]:


def coin(ar):   
   n=len(ar)
   res=1
   for i in range(0,n):
       if(ar[i]<=res):
           res+=ar[i]
       else:
           break
   return res

i = int(input())
ar=[]
for x in range(i):
   a=int(input())
   ar.append(a)
ans= coin(ar)
ans


# In[ ]:




