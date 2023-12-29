#!/usr/bin/env python
# coding: utf-8

# In[2]:


#CSV Files - Comma Separated Values


# # 1. Importing Pandas

# In[3]:


import pandas as pd


# # 2. Opening a Local CSV File

# In[6]:


csv_data = pd.read_csv("car_prediction_data.csv")
csv_data


# # 3. Opening a CSV File from an URL

# In[7]:


import requests
from io import StringIO

url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
my_headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0"}
req = requests.get(url, headers=my_headers)
data = StringIO(req.text)

pd.read_csv(data)


# # 4. Sep Parameter

# In[12]:


read_tsv_files = pd.read_csv('movie_titles_metadata.tsv',sep='\t',names=['sno.','name','release_year','rating','votes','genres'],index_col='sno.')
read_tsv_files


# # 5. Index_col Parameter

# In[14]:


df = pd.read_csv('Placement_Data_Full_Class.csv', index_col='Sno')
df


# # 6. Header Parameter

# In[18]:


Test_CSV = pd.read_csv('test.csv',header=1)
Test_CSV


# # 7. use_cols Parameter

# In[26]:


Car_Prediction_Data = pd.read_csv('car_prediction_data.csv',usecols=['Car_Name','Selling_Price','Present_Price','Kms_Driven'])
Car_Prediction_Data


# # 8. Squeeze Parameters

# In[33]:


# Read the CSV file without using squeeze
movie_data = pd.read_csv('car_prediction_data.csv', usecols=['Selling_Price'])

# Use the squeeze() method or select the column to obtain a Series
selling_price_series = movie_data['Selling_Price'].squeeze()

selling_price_series


# # 9. Skiprows/nrows Parameter

# In[39]:


#movie_data = pd.read_csv('car_prediction_data.csv', skiprows=[0,1,2,3,4,5,6,7,8,9])
movie_data = pd.read_csv('car_prediction_data.csv', nrows=100)
movie_data


# # 10. Encoding Parameter

# In[42]:


Zomato = pd.read_csv('zomato.csv',encoding='latin-1')
Zomato


# # 11. Skip Bad Lines

# In[43]:


# Error_Data = pd.read_csv('', encoding='latin-1',error_bad_lines=False)


# # 12. DTypes Parameters

# In[49]:


pd.read_csv('aug_train.csv',dtype={'target':int})


# # 13. Handling Dates

# In[51]:


pd.read_csv('IPL Matches 2008-2020.csv',parse_dates=['date']).info()


# # 14. Converters

# In[56]:


def rename(name):
    if(name == "Royal Challengers Bangalore"):
        return "RCB"
    elif(name == "Mumbai Indians"):
        return "MI"
    elif(name == "Delhi Daredevils"):
        return "DD"
    elif(name == "Kolkata Knight Riders"):
        return "KNR"
    else:
        return name

pd.read_csv('IPL Matches 2008-2020.csv',converters={'team1':rename,'team2':rename})


# # 15. na_values parameter

# In[59]:


pd.read_csv('aug_train.csv',na_values=['Has relevent experience','Male'])


# # 16. Loading a Huge Dataset in Chunks

# In[63]:


dataframes = pd.read_csv('aug_train.csv',chunksize=5000)


# In[69]:


for chunks in dataframes:
    print(chunks.shape)


# In[ ]:




