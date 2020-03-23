#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 19:25:38 2020

@author: jordan
"""

import pandas as pd
import seaborn as sns
data = pd.read_csv('/Users/jordan/Desktop/iris.data')
sns.set() #applies seaborn style to matplotlib graphs
sns.pairplot(data, hue = 'Name') #produces pairplot