#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Solution:
    def noOfPaths (self, n, m):
        if(n==1 or m==1):
            return 1
        return self.noOfPaths(m-1,n)+self.noOfPaths(m,n-1)
    
m, n = map(int, input().split())
ob = Solution()
ans = ob.noOfPaths(m, n)
print(ans)


# In[ ]:




