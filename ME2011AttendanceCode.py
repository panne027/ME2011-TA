# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 08:58:45 2020

@author: panne027
"""

import os 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from fuzzywuzzy import fuzz #pip install fuzzywyzzy
from fuzzywuzzy import process
import glob #pip install glob
from fuzzywuzzy import process

#%%
path='C:/Users/panne027/Google Drive/ME2011/001attendance/' #folder containing all registration reports from zoom
path2='C:/Users/panne027/Google Drive/ME2011/001students.csv' #csv file containing names of all students
reports= os.listdir(path)
students=pd.read_csv(path2)
threshold=70 #name matching threshold out of 100

for file in reports:
    readreport=pd.read_csv(path+file)
    if len(readreport)<10:
        continue
    date=readreport['Join Time'][3].split(' ',2)[0]
    if date not in students.columns:
        students[date]=0 
    # 
    for j in range(len(students)):
        for k in range(len(readreport)):
            if fuzz.partial_ratio(students['Student'][j],readreport['Name'][k])>=threshold:
                students[date][j]=1

#%%
path3='C:/Users/panne027/Google Drive/ME2011/' #output file
students.to_csv(path3+'001-011attendanceoutput.csv', index=False) 

