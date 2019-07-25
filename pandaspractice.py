# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

# DataFrame: a 2D table containing rows and columns (think an excel sheet)
df_data = {
        #Creating a single column with 5 rows
    'col1':np.random.rand(5),
    'col2':np.random.rand(5),
    'col3':np.random.rand(5)
}

df = pd.DataFrame(df_data)

#Fetch some rows
#print(df[:2])
#Fetch a column
#print(df['col1'])
#Fetch multiple columns
print(df[['col1','col2']])
