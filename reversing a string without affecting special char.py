#!/usr/bin/env python
# coding: utf-8

# In[1]:


def swap(a, b):
    temp = a
    a = b
    b = temp
        
def reversingString(s): 

    r = len(s) - 1
    l = 0

    while l < r:       
        if s[l].isalpha() == False:
            l+=1
        elif s[r].isalpha() == False:
            r-=1
        else:
            t=s[r]
            s[r]=s[l]
            s[l]=t
            l+=1
            r-=1
    
    return s
string = input()
string = reversingString(list(string)) 
print ( "".join(string)) 


# In[ ]:




