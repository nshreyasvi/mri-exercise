import pandas as pd
import io
import os
import xnat
import gc

df = pd.read_csv('dataset_full.csv')
df_scd = df.loc[df['Group']==1]
df_td = df.loc[df['Group']==3]

df_scd_test = pd.concat([df_scd, df_td], axis=0) 
#df_scd_test = df_scd_test.loc[df_scd_test['MR Sessions']==1]

#ft = df_scd_test[['Subject','M/F','Hand','MR Sessions','Group','Labels','Race','label','Ethnicity','AGE']]
ft = df_scd_test[['MR ID','Subject','Session','Scans','Date','M/F','Hand','Group','Race','Ethnicity','LABEL','AGE']]
ft_s = ft.groupby('Group').head(20)
print(ft.head())
ft_s.to_csv('data_test.csv', index = False)

connection = xnat.connect('https://central.xnat.org', user="nshreyasvi", password="Reoshrey1@")
nu_project = connection.projects["NUDataSharing"]

subjects = nu_project.subjects
print(str(subjects))
connection.disconnect()