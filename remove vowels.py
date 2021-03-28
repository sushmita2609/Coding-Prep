#!/usr/bin/env python
# coding: utf-8

# In[13]:


def rem_vowel(st,l):
    n = len(st)
    for x in st.lower():
        if x in l:
            st=st.replace(x,"")
    return st
l=('a','e','i','o','u')
st=input()
print(rem_vowel(st,l))


# In[ ]:




