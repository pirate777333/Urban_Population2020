import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import geopandas as gpd

df = pd.read_csv('D:/rektorov_rad/programirano/Urbano/Urban_Areas_by_Country_16.csv')

#print(df.head())
#print(df.isnull().sum())
#print(df.dtypes)
print(df.columns)

lista = ['UA_over_500k', 'UA_over_1mil', 'UA_over_2mil', 'UA_over_5mil']

df=df.sort_values(by='UA_over_500k', ascending=False)
print(df.iloc[:20,:])

fig=px.bar(df.iloc[0:20],y='UA_over_500k',x='Nation',color='Nation',
           text='UA_over_500k',template='plotly_dark',
           title='(Highest) Number of Urban Areas with more than 500,000 people')
fig.show()

df=df.sort_values(by='UA_over_500k', ascending=True)
print(df.iloc[:20,:])

fig=px.bar(df.iloc[0:20],y='UA_over_500k',x='Nation',color='Nation',
           text='UA_over_500k',template='plotly_dark',
           title='(Lowest) Number of Urban Areas with more than 500,000 people')
fig.show()

df=df.sort_values(by='UA_over_5mil', ascending=False)
print(df.iloc[:20,:])

fig=px.bar(df.iloc[0:20],y='UA_over_5mil',x='Nation',color='Nation',
           text='UA_over_5mil',template='plotly_dark',
           title='(Highest) Number of Urban Areas with more than 5 mil people')
fig.show()

data=[]

for i in lista:
    data.append(df[i].sum())

fig=px.bar(y=data,x=lista,color=lista,
           text=data,template='plotly_dark',
           title='Number of World Urban Areas')
fig.show()

data2=[]

for i in lista:
    df2 = df[(df[i] > 0)]
    data2.append(df2.shape[0])

fig=px.bar(y=data2,x=lista,color=lista,
           text=data2,template='plotly_dark',
           title='Number of Countrie with Urban Areas')
fig.show()
