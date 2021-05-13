import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import geopandas as gpd

df = pd.read_csv('D:/rektorov_rad/programirano/Urbano/47d1a797-e6f9-4231-abbf-93c489be1028_Data.csv')
df=df.iloc[:-52,2:-1]
#print(df.tail(10))
df.columns=['Country Name', 'Country Code', '1990', '2000',
            '2011', '2012', '2013', '2014', '2015', '2016',
            '2017', '2018', '2019']

def stringops(text):
    if text=='..':
        return None
    else:
        return text

for i in df.columns:
    df[i]=df[i].apply(stringops)

df=df.dropna()

#print(df.isnull().sum())
#print(df.shape)

lista=['1990', '2000',
            '2011', '2012', '2013', '2014', '2015', '2016',
            '2017', '2018', '2019']

for i in lista:
    df[i]=pd.to_numeric(df[i])

#print(df.dtypes)

print(df.shape)

print(df.head())

df=df.sort_values(by='2019', ascending=False)
print(df.iloc[:10,:])

fig=px.bar(df.iloc[0:10],y='2019',x='Country Name',color='Country Name',
           text='2019',template='plotly_dark',title='(Highest) Percentage of Urban Population in largest city')
fig.show()

df=df.sort_values(by='2019', ascending=True)
print(df.iloc[:10,:])

fig=px.bar(df.iloc[0:10],y='2019',x='Country Name',color='Country Name',
           text='2019',template='plotly_dark',title='(Lowest) Percentage of Urban Population in largest city')
fig.show()


def specific_country(country_name):
    country_data = df[df['Country Name']==country_name]
    country_data=country_data.T
    country_data=country_data.iloc[2:,:]
    year=country_data.index.tolist()
    data=country_data.iloc[:,0].tolist()
    fig=px.bar(y=data,x=year,color=year,
           template='plotly_dark',title=country_name+' Percentage of Urban Population in largest city',
           labels=dict(x="Years", y="Percentage of Urban Population in largest city", color="Years"))
    fig.show()
    fig=px.line(y=data,x=year,
           template='plotly_dark',title=country_name+' Percentage of Urban Population in largest city',
           labels=dict(x="Years", y="Percentage of Urban Population in largest city"))
    fig.show()

a=input('Your Country Name: __ ')

try:
    specific_country(a)
except:
    print('Invalid Country Name')
