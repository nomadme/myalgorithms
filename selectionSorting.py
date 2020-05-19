#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))


# In[18]:


numCollection = [*range(5000)]
random.shuffle(numCollection)
print(numCollection)


# In[19]:


print(selectionSort(numCollection))


# In[ ]:




