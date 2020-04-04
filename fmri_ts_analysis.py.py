# import dependencies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import scipy
import scipy.stats as stats
import seaborn as sns
import pingouin as pg
import os

# import excel file containing variables of interest
variables = pd.read_excel (r'C:\Users\variable_spreadsheet.xlsx', sheet_name='df')

# create holder with file locations
# os.walk or glob.iglob can also be used
holder=[]
folders = [r'C:\Users\1012\time_series',           
           r'C:\Users\1013\time_series',       
          ]
# import time_series data as a series of dataframes per subject into holder
for i in folders:
    li = []
    df = pd.DataFrame()
    os.chdir(i)
    li = os.listdir()
    df = pd.concat([pd.read_csv(item, names=[item[:-4]]) for item in li], axis=1)
    holder.append(df)

# make a list of column names (in this instance ROI names)
list = df.columns.tolist()
# delete the regions you *want to keep* and save list
# this will then get rid of the columns in the list leaving you with a 
# reduced dataframe with your specific ROI
#for i in holder:
    #i.drop(list,axis=1, inplace=True)

# plot correlation matrix from holder and append to cor_holder
cor_holder = []
for i in holder:
    df_corr = i.corr(method='pearson') 
    cor_holder.append(df_corr)
    
# print a correlation matrix as a first inspection
for i in cor_holder:
    plt.matshow(i.corr())
    plt.show

# flatten correlation matrix and append row-wise for each subject &
# convert tuple column name to string
stacked = []
for i in cor_holder:
    unstack2 = i.unstack()
    unstack2 = pd.DataFrame(unstack2)
    unstack2 = unstack2.transpose()
    stacked.append(unstack2)
stacked_df = pd.concat(stacked)
stacked_df = stacked_df.T[stacked_df.any()].T
stacked_df = stacked_df.reset_index()
stacked_df.columns = ['-'.join(x) for x in stacked_df.columns] 

# concatenate regressors/variables with roi correlation values 
# make subject index 
stacked_beh = pd.concat([variables, stacked_df], axis=1)
stacked_beh = stacked_beh.set_index('subject')

