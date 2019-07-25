# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 14:23:46 2019

@author: garyt
"""
import pandas as pd
import numpy as np
#Read an Excel spreadsheet
tracks = pd.read_excel('Tracks.xlsx', sheet_name = 0)
#Print the entire sheet
#print(tracks)
#Print the columns
print(tracks.columns)
#Print a specific column
print(tracks['Milliseconds'])

#Read a CSV file
#Index col = false allows normal indexing 
#and removed the automated offset of columns
flights = pd.read_csv('flights.csv', index_col = False)
print(flights)