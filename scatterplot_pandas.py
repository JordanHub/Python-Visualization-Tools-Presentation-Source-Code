#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 19:25:38 2020

@author: jordan
"""

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('/Users/jordan/Desktop/iris.data')
fig, ax = plt.subplots()
colors = {'Iris-setosa':'blue', 'Iris-versicolor':'orange', 'Iris-virginica':'green'}
grouped = data.groupby('Name')
for key, group in grouped:
    group.plot(ax=ax, kind='scatter', x='PetalLength', y='PetalWidth', label=key, color=colors[key])