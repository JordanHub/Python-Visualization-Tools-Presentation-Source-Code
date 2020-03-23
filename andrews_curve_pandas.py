#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 19:25:38 2020

@author: jordan
"""
import matplotlib as plt
import pandas as pd
from pandas.plotting import andrews_curves
data = pd.read_csv('/Users/jordan/Desktop/iris.data')
plt.figure.Figure()
andrews_curves(data, 'Name')