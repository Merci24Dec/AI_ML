# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 10:30:34 2020

@author: anshu
"""

'''
Pandas
- Data Import / Export
- Data selection & Filtering
#   - Basics of Statistics
- Data Cleaning
- Data Aggregation
'''
import pandas as pd

'''
1. Pandas series - 1D data
2. Pandas Dataframe - 2D data
3. Pandas Panel - 3D data
'''

df = pd.read_csv(r"D:\AI\data\datawh.csv",
                 index_col=['Dates'])

df = pd.read_csv(r"D:\AI\data\datanh.csv",
                 header=None)

df.columns=['Temperature',"humidity","airq",'pressure']


url = "https://coinmarketcap.com/currencies/bitcoin/historical-data/"

dfs = pd.read_html(url)

type(dfs)
len(dfs)
df1 = dfs[0]
df2 = dfs[1]
df3 = dfs[2]

# export
df3.to_excel(r"D:\ai\techtrunk\giet\bitcoin_data.xlsx")










