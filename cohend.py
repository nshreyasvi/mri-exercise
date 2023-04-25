import pandas as pd
from statistics import mean, stdev
from math import sqrt
from numpy import var, mean, sqrt
from pandas import Series
import gc

# Right Hemisphere
aparc_df = pd.read_csv("thickness_rh.csv")

aparc_df_scd = aparc_df.loc[aparc_df['Group']==1]
aparc_df_td = aparc_df.loc[aparc_df['Group']==3]

test_columns = aparc_df.columns[2:]

for i in range(0,len(test_columns)):
    d1 = aparc_df_scd[str(test_columns[i])]
    d2 = aparc_df_td[str(test_columns[i])]

    # calculate the size of samples
    n1, n2 = len(d1), len(d2)
    # calculate the variance of the samples
    s1, s2 = var(d1, ddof=1), var(d2, ddof=1)
    # calculate the pooled standard deviation
    s = sqrt(((n1 - 1) * s1 + (n2 - 1) * s2) / (n1 + n2 - 2))
    # calculate the means of the samples
    u1, u2 = mean(d1), mean(d2)
    cohend = (u1-u2)/s
    
    print(str(test_columns[i])+', '+ str(cohend))
    gc.collect()

#Left Hemisphere
aparc_df = pd.read_csv("thickness_lh.csv")

aparc_df_scd = aparc_df.loc[aparc_df['Group']==1]
aparc_df_td = aparc_df.loc[aparc_df['Group']==3]

test_columns = aparc_df.columns[2:]

for i in range(0,len(test_columns)):
    d1 = aparc_df_scd[str(test_columns[i])]
    d2 = aparc_df_td[str(test_columns[i])]

    # calculate the size of samples
    n1, n2 = len(d1), len(d2)
    # calculate the variance of the samples
    s1, s2 = var(d1, ddof=1), var(d2, ddof=1)
    # calculate the pooled standard deviation
    s = sqrt(((n1 - 1) * s1 + (n2 - 1) * s2) / (n1 + n2 - 2))
    # calculate the means of the samples
    u1, u2 = mean(d1), mean(d2)
    cohend = (u1-u2)/s
    
    print(str(test_columns[i])+', '+ str(cohend))
    gc.collect()