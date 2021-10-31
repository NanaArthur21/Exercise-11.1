#!/usr/bin/env python
# coding: utf-8

# In[1]:


eng2sp = dict()


# In[2]:


print(eng2sp)


# In[3]:


eng2sp = {'abalones': 'cobbler': 'halfhearted': 'instruments': 'precautions': 'referral': 'sapphire': 'titanic': 'union'}
print(eng2sp)


# In[4]:


eng2sp = {'cobbler': 'abalones', 'halfhearted':'precautions', 'titanic': 'instruments', 'referral': 'sapphire', 'union': 'bright'}
print(eng2sp)


# In[5]:


count = 0    


# In[6]:


eng2sp = dict()


# In[7]:


fin = open('words.txt')


# In[8]:


for line in fin:
    words = line.split()
    for word in words:
        count += 1
        if word in eng2sp:
            continue
        eng2sp[word] = count


# In[9]:


if 'abalones' in eng2sp:
    print('True')
else:
    print('False')


# In[10]:


count = 0  


# In[11]:


eng2sp = dict()


# In[12]:


for line in eng2sp:
    words = line.split()
    for word in words:
        count += 1
        if word in eng2sp:
            continue
        eng2sp[word] = count


# In[13]:


if 'halfhearted' in eng2sp:
    print('True')
else:
    print('False')


# In[14]:


eng2sp = {'cobbler': 'abalones', 'halfhearted':'precautions', 'titanic': 'instruments', 'referral': 'sapphire', 'union': 'bright'}
print(eng2sp)


# In[15]:


eng2sp = dict()


# In[16]:


for line in eng2sp:
    words = line.split()
    for word in words:
        count += 1
        if word in eng2sp:
            continue
        eng2sp[word] = count


# In[17]:


if 'halfhearted' in eng2sp:
    print('True')
else:
    print('False')


# In[18]:


eng2sp = {'cobbler': 'abalones', 'halfhearted':'precautions', 'titanic': 'instruments', 'referral': 'sapphire', 'union': 'bright'}
print(eng2sp)


# In[19]:


for line in eng2sp:
    words = line.split()
    for word in words:
        count += 1
        if word in eng2sp:
            continue
        eng2sp[word] = count


# In[20]:


if 'bright' in eng2sp:
    print('True')
else:
    print('False')


# In[ ]:




