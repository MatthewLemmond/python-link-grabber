
# coding: utf-8

# ### Import urllib and read in data from webpage

# In[1]:


import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('https://en.wikipedia.org/wiki/Computer_graphics')
lines = []
for line in fhand:
    lines.append(line.decode().strip())


# ### Import regex library and compile the regular expression to grab a tags

# In[2]:


import re

match_string = re.compile('(?:<a)(?:\s+.*?href="(.*?)")(?:.*?<\/a>)')
match_string


# ### Loop through the text line by line and match against the regular expression built earlier

# In[3]:


tag_texts = []
for line in lines:
    temp = re.findall(match_string, line)
    if len(temp) != 0:
        tag_texts.extend(temp)


# ### Display the number of tags extracted and the tags themselves

# In[7]:


print("Number of links grabbed: " + str(len(tag_texts)) + "\nList of Links:")
tag_texts

