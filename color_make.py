import pandas as pd
import numpy as np
import io
import os
import glob

#df = pd.read_csv('color_test.txt', sep = ' ')
df_c = pd.read_csv('cohens_d.csv', names = ['Label Name:','Cohens_d'])

no = [0]*70

for i in range(0,35):
    #print(1001+i)
    no[i] = 1001+i

for i in range(0,35):
    #print(2001+i)
    no[35+i] = 2001+i

#df_c['#No.'] = 1001+np.arange(df_c.shape[0])

df_c['#No.'] = no
df_c['Label Name:'] = 'ctx_' + df_c['Label Name:'].astype(str)

#Normalize cohens_d values
df_c['R'] = 50+(df_c['Cohens_d']/max(df_c['Cohens_d']))*100
df_c['G'] = 0
df_c['B'] = 0
df_c['A'] = 0
df_c.loc[df_c['Cohens_d'] < 0, 'G'] = 255

df_c.loc[df_c['R'] < 0, 'R'] = -1*df_c['R']
df_c['R'] = round(df_c['R'])

df_c = df_c.drop('Cohens_d', axis=1)
df_c['R'] = df_c['R'].astype(np.int64)

print(min(df_c['R']))
print(max(df_c['R']))

cols = ['#No.','Label Name:','R','G','B','A']
df_c = df_c[cols]

print(df_c.head())

df_c.to_csv('color_gen.txt', index = False, sep = ' ')

#======Positive, Negative, Zero============================================

#df = pd.read_csv('color_test.txt', sep = ' ')
df_c = pd.read_csv('cohens_d.csv', names = ['Label Name:','Cohens_d'])

no = [0]*70

for i in range(0,35):
    #print(1001+i)
    no[i] = 1001+i

for i in range(0,35):
    #print(2001+i)
    no[35+i] = 2001+i

#df_c['#No.'] = 1001+np.arange(df_c.shape[0])

df_c['#No.'] = no
df_c['Label Name:'] = 'ctx_' + df_c['Label Name:'].astype(str)

#Only 3 colors are kept based on positive negative and zero values
df_c['R'] = 0
df_c['G'] = 0
df_c['B'] = 0
df_c['A'] = 0

df_c.loc[df_c['Cohens_d'] > 0, 'R'] = 255
df_c.loc[df_c['Cohens_d'] < 0, 'G'] = 255
df_c.loc[df_c['Cohens_d'] == 0, 'B'] = 255

df_c = df_c.drop('Cohens_d', axis=1)

cols = ['#No.','Label Name:','R','G','B','A']
df_c = df_c[cols]

print(df_c.head())

df_c.to_csv('color_gen_class.txt', index = False, sep = ' ')