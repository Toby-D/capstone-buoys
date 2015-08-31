
# coding: utf-8

# # Analyzing data from the National Bouy System

# ## Background
# 
# The National Data Buoys Data center publish oceanographic data from their buoys on their web. Bouys send up their measurements every hour and the data is published as a spreadsheet in the NOAA web site.
# 
# We want to collect the data for any, or many, bouys, clean it up, and analyze it to make a plot.
# 
# ## Challenges
# 
# - Get the data from the web and read it into our Python notebook.
# - Clean up the data, which sometimes has missing measurements.
# - Choose the bouys we want to analyze using their ID numbers.
# - Run our analysis (we will just make a plot).
# - Save our code as a script or module for reusing it later.

# ## References 
# 
# - National Data Buoy Center: http://www.ndbc.noaa.gov/
# - Data for Station 44255 - NE Burgeo Bank: http://www.ndbc.noaa.gov/station_realtime.php?station=44255
# - How a buoy get an ID: http://www.ndbc.noaa.gov/staid.shtml
# - All the station IDs: http://www.ndbc.noaa.gov/to_station.shtml

# In[1]:

url = 'http://www.ndbc.noaa.gov/data/realtime2/44255.txt'


# In[35]:

import requests #Library for getting stuff from web


# In[36]:

response = requests.get(url)


# In[37]:

type(response.text)


# In[38]:

#So convert into 
import StringIO #For converting into strings
data_str = StringIO.StringIO(response.text)


# In[39]:

import pandas as pd #cf. Excel. Go-to for data processing #as pd is just giving shortcut


# In[44]:

data = pd.read_csv(StringIO.StringIO(response.text), 
                   delim_whitespace=True, 
                   skiprows=[1,2], 
                   usecols=[0,1,2,3,6,8])


# In[47]:

import numpy as np
from numpy import nan
data=data.replace('MM', nan)
data=data.dropna(axis=0)


# In[53]:

get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
data.WSPD.plot()


# In[54]:

print data.WSPD.mean()


# In[ ]:

#nbviewer.com


# In[ ]:



