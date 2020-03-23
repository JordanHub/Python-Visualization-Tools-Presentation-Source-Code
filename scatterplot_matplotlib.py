#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 19:25:38 2020

@author: jordan
"""

import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('/Users/jordan/Desktop/iris.data')
color_map = dict(zip(data.Name.unique(), ['blue', 'orange', 'green']))
for name, group in data.groupby('Name'):
    plt.scatter(group['PetalLength'], group['PetalWidth'], color = color_map[name], edgecolor = None, label = name)
plt.legend(frameon = True, title = 'Name')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')