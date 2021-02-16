#!/usr/bin/env python
# coding: utf-8

# In[4]:


class newNode:
    def __init__(s, key):
        s.key=key
        s.left= None
        s.right=None
        
def sum_tree(root):
    if(root==None):
        return 0
    else:
        sum = root.key + sum_tree(root.left)+sum_tree(root.right)
    return sum

if __name__ == '__main__':
    root = newNode(3)
    root.left = newNode(9)
    root.right = newNode(20)
    root.right.left = newNode(15)
    root.right.right = newNode(7)
    add=sum_tree(root)
    print(add)


# In[ ]:




