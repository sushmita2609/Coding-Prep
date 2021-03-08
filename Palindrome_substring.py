#!/usr/bin/env python
# coding: utf-8

# In[46]:


def reverse(str1):
    if(len(str1)==0):
        return str1
    else:
        return reverse(str1[1:])+str1[0]


# In[45]:


org_string = "sushmitabobpavi"
str2 = ''

for i in range(len(org_string)):
    str2 = str2 + org_string[i]
    
for i in range(len(org_string)):    
    for x in range(len(org_string)):
        org_string = org_string[:-1]
        if(org_string == reverse(org_string)):
            if(len(org_string) > 1):
                print(org_string)
    str2 = str2[1:]
    org_string = str2 


# In[ ]:





# In[ ]:




