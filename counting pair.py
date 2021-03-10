#!/usr/bin/env python
# coding: utf-8

# In[15]:


input()
s = input().strip().split()
pair = 0

for element in set(s):
    pair += s.count(element) // 2
print(pair)


# In[ ]:





# In[ ]:




