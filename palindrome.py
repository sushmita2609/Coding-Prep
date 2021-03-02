#!/usr/bin/env python
# coding: utf-8

# In[7]:


def palin(str):
    str_len=len(str)
    str_l=str[0]
    str_r=str[str_len-1]
    f=0
    for i in range(int(str_len/2)):
        if(str_l==str_r):
            str_l=str[i+1]
            str_r=str[(str_len-1)-1]
            f=1       
        else:
            print("not a palindrome")
            return 0
    if(f):
        print("palindrome")
    return 1
    
str=input()
palin(str)


# In[ ]:




