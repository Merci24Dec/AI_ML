# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 17:02:24 2020

@author: anshu
"""

import pandas as pd
df = pd.read_csv(r"D:\AI\data\regiment.csv")

'''
1. which is the best regiment after the training?
2. which company of which regiment is best peforming after training?
3. create a column which shows improvement of every soldier during training?
4. which regiment soldiers made maximum improvement during training?
'''
# question 1
df.postTestScore.mean()
df.groupby(['regiment'])['postTestScore'].mean()
# question 2
df.groupby(['regiment','company'])['postTestScore'].mean()

# question 3
df['improvement'] = df['postTestScore'] - df['preTestScore']

# question 4
df.groupby(['regiment'])['improvement'].mean()




