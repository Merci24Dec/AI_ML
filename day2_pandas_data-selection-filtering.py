# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 12:18:57 2020

@author: anshu
"""

# Data Exploration, Selection and Filtering

import pandas as pd

df = pd.read_csv(r"D:\AI\data\datawh.csv",index_col=['Dates'])

'''
Exploration - understand data, collect information,
              identify challenges in data
'''
df.shape
print(df.columns)
df.head() # top 5 rows
df.head(2) # top 2 rows
df.tail()

df.info() # overall data summary

df.describe() # overall statistical summary


##########################################################
df.head()
# Data selection
df['Temperature']
df.Temperature # not recommended

df[['Temperature','Humidity']]

type(df['Temperature'])
type(df[['Temperature','Humidity']])

df['05-05-2018':'12-05-2018']

df['05-05-2018':'12-05-2018']['Temperature']
df['05-05-2018':'12-05-2018'][['Temperature','Humidity']]

df.iloc[5:18,1:3]

###########################################################
# Filteirng

df[df.Temperature>2000]
df[df['Temperature']>2000]

df[df['Temperature']>2000][['Temperature','Humidity']]

df[df['Temperature']>2000][df['Humidity']>200]

#AND
df[ (df['Temperature']>2000) & (df['Humidity']>200)]

#OR 
df[ (df['Temperature']>2000) | (df['Humidity']>200)]




#########################################################
# Statistics

df.describe()

df['Temperature'].mean()
df['Temperature'].median()
df['Temperature'].mode()
df['Temperature'].min()
df['Temperature'].max()
df['Temperature'].var()
df['Temperature'].std()
df['Temperature'].skew()






















