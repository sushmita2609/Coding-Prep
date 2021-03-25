#!/usr/bin/env python
# coding: utf-8

# In[14]:


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def max_depth(n):
    if n is None:
        return 0
    else:
        l_depth = max_depth(n.left)
        r_depth = max_depth(n.right)
        d = max(l_depth,r_depth)      
        return d+1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(max_depth(root))


# In[4]:


root = Node(10)
root.left = Node(20)
root.right = Node(12)
root.right.left = Node(7)
root.left.right = Node(4)
root.right.left.right = Node(17)


# In[9]:


class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# Compute the "maxDepth" of a tree -- the number of nodes
# along the longest path from the root node down to the
# farthest leaf node
def maxDepth(node):
    if node is None:
        return 0 ;
 
    else :
 
        # Compute the depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
 
        # Use the larger one
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1
 
 
# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
 
print ("Height of tree is %d" %(maxDepth(root)))


# In[ ]:




