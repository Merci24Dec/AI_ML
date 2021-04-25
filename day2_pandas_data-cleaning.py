# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 16:19:48 2020

@author: anshu
"""

# Data CLeaning
import pandas as pd
df = pd.read_csv(r"D:\AI\data\datawh_missing.csv")

'''
1. Handling duplicated entries
2. Hnadling missing values
'''
# to check for duplicates - 
df.duplicated().sum()

# drop the duplicated rows
df.drop_duplicates(inplace=True)
# df2  = df.drop_duplicates(inplace=False)


#############################################
# Handling missing values
#check for missing values
df.isnull().sum()


df = pd.read_csv(r"D:\AI\data\datawh_missing.csv",
                 na_values=['.','?'])

#check for missing values
df.isnull().sum()

# dropping those rows which has less than 3 real values
df.dropna(thresh=3,inplace=True)

df.info()
df.skew()
# filling missing values of tempreature using mean
df['Temperature'].fillna(df['Temperature'].mean(),inplace=True)
# filling rest of missing values by median
df.fillna(df.median(),inplace=True)












