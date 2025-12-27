#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('display', 'latex')
var('z')
z^12


# In[2]:


sqrt(z^2 + 1/2)


# In[3]:


'a string'


# In[4]:


QQ


# In[5]:


ZZ['x']


# In[6]:


matrix(QQ, 2, 3, [[2,4,6],[-1,-1,-1]])


# In[7]:


get_ipython().run_line_magic('display', 'plain')


# In[8]:


get_ipython().run_line_magic('display', 'latex')
QQ


# In[9]:


latex.blackboard_bold(True)
QQ


# In[10]:


latex.blackboard_bold(False)
get_ipython().run_line_magic('display', 'plain')


# In[11]:


get_ipython().run_line_magic('display', 'latex')
var('x y')
sqrt(x + y)


# In[12]:


latex.add_macro(r"\newcommand{\sqrt}[1]{(#1)^\frac{1}{2}}")
sqrt(x + y)


# In[13]:


latex.extra_macros('')
get_ipython().run_line_magic('display', 'plain')

