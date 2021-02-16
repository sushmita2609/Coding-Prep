#!/usr/bin/env python
# coding: utf-8

# In[4]:




def sum(arr, n, t):
    l=0
    r=n-1
    arr1=[]
    while l<r:
        if(arr[l]+arr[r] == t):
            print(l,r)
            return 1
        elif(arr[l]+arr[r] < t):
            l=l+1
        else:
            r=r-1          
    return 1
        

arr=[2,7,11,15]
t=18
d=sum(arr,len(arr),t)
    
    
    


# In[ ]:



    

