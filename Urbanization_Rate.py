import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import geopandas as gpd

df = pd.read_csv('D:/rektorov_rad/programirano/Urbano/1073a525-06c6-482d-b69a-7cb2c84982a1_Data.csv')
df=df.iloc[:-5,2:-1]
df.columns=['Country Name', 'Country Code', '1990', '2000',
            '2011', '2012', '2013', '2014', '2015', '2016',
            '2017', '2018', '2019']
df = df[df['Country Name'] != 'Eritrea']
df = df[df['Country Name'] != 'Kosovo']
df = df[df['Country Name'] != 'St. Martin (French part)']
df = df[df['Country Name'] != 'Not classified']
df = df[df['Country Name'] != 'West Bank and Gaza']

lista=['1990', '2000',
            '2011', '2012', '2013', '2014', '2015', '2016',
            '2017', '2018', '2019']

#print(df.shape)

df['1990']=pd.to_numeric(df['1990'])
df['2000']=pd.to_numeric(df['2000'])
df['2011']=pd.to_numeric(df['2011'])
df['2012']=pd.to_numeric(df['2012'])
df['2013']=pd.to_numeric(df['2013'])
df['2014']=pd.to_numeric(df['2014'])
df['2015']=pd.to_numeric(df['2015'])
df['2016']=pd.to_numeric(df['2016'])
df['2017']=pd.to_numeric(df['2017'])
df['2018']=pd.to_numeric(df['2018'])
df['2019']=pd.to_numeric(df['2019'])

#print(df.head(10))
#print(df.columns)

df=df.sort_values(by='2019', ascending=False)

world = df[df['Country Name'] == 'World']
print(world)

df = df[df['Country Name'] != 'Pre-demographic dividend']
df = df[df['Country Name'] != 'Heavily indebted poor countries (HIPC)']
df = df[df['Country Name'] != 'Sub-Saharan Africa (excluding high income)']
df = df[df['Country Name'] != 'Sub-Saharan Africa (IDA & IBRD countries)']
df = df[df['Country Name'] != 'Sub-Saharan Africa']
df = df[df['Country Name'] != 'Least developed countries: UN classification']
df = df[df['Country Name'] != 'Low income']
df = df[df['Country Name'] != 'IDA only']
df = df[df['Country Name'] != 'World']
df = df[df['Country Name'] != 'IDA total']
df = df[df['Country Name'] != 'IDA blend']
df = df[df['Country Name'] != 'Fragile and conflict affected situations']
df = df[df['Country Name'] != 'Other small states']
df = df[df['Country Name'] != 'Lower middle income']
df = df[df['Country Name'] != 'South Asia (IDA & IBRD)']
df = df[df['Country Name'] != 'South Asia']
df = df[df['Country Name'] != 'Small states']
df = df[df['Country Name'] != 'Arab World']
df = df[df['Country Name'] != 'East Asia & Pacific (IDA & IBRD countries)']
df = df[df['Country Name'] != 'East Asia & Pacific (excluding high income)']
df = df[df['Country Name'] != 'Low & middle income']
df = df[df['Country Name'] != 'IDA & IBRD total']
df = df[df['Country Code'] != 'MNA']
df = df[df['Country Name'] != 'Middle East & North Africa (IDA & IBRD countries)']
df = df[df['Country Name'] != 'Early-demographic dividend']
df = df[df['Country Name'] != 'Middle East & North Africa']
df = df[df['Country Name'] != 'Pacific island small states']
df = df[df['Country Name'] != 'Middle income']
df = df[df['Country Name'] != 'South Africa']
df = df[df['Country Name'] != 'East Asia & Pacific']
df = df[df['Country Name'] != 'IBRD only']
df = df[df['Country Name'] != 'Upper middle income']
df = df[df['Country Name'] != 'Late-demographic dividend']
df = df[df['Country Name'] != 'Latin America & Caribbean (excluding high income)']
df = df[df['Country Code'] != 'TLA']
df = df[df['Country Name'] != 'Latin America & Caribbean']
df = df[df['Country Name'] != 'Caribbean small states']
df = df[df['Country Name'] != 'OECD members']
df = df[df['Country Name'] != 'Europe & Central Asia (excluding high income)']
df = df[df['Country Name'] != 'Europe & Central Asia (IDA & IBRD countries)']
df = df[df['Country Name'] != 'Europe & Central Asia']
df = df[df['Country Name'] != 'Post-demographic dividend']
df = df[df['Country Name'] != 'Euro area']
df = df[df['Country Name'] != 'European Union']
df = df[df['Country Name'] != 'Central Europe and the Baltics']

#print(df.shape)

df=df.sort_values(by='2019', ascending=False)
print(df.iloc[:10,:])

fig=px.bar(df.iloc[0:10],y='2019',x='Country Name',color='Country Name',
           text='2019',template='plotly_dark',title='(Highest) Annual Urban Population Growth in %')
fig.show()

df=df.sort_values(by='2019', ascending=True)
print(df.iloc[:10,:])

fig=px.bar(df.iloc[0:10],y='2019',x='Country Name',color='Country Name',
           text='2019',template='plotly_dark',title='(Lowest) Annual Urban Population Growth in %')
fig.show()

world=world.T
world=world.iloc[2:,:]
year=world.index.tolist()
data=world.iloc[:,0].tolist()
fig=px.bar(y=data,x=year,color=year,
       template='plotly_dark',title='World Annual Urban Population Growth in %',
       labels=dict(x="Years", y="Annual Urban Population Growth in %", color="Years"))
fig.show()

def specific_country(country_name):
    country_data = df[df['Country Name']==country_name]
    country_data=country_data.T
    country_data=country_data.iloc[2:,:]
    year=country_data.index.tolist()
    data=country_data.iloc[:,0].tolist()
    fig=px.bar(y=data,x=year,color=year,
           template='plotly_dark',title=country_name+' Annual Urban Population Growth in %',
           labels=dict(year="Years", data="Annual Urban Population Growth in %", color="Years"))
    fig.show()
    fig=px.line(y=data,x=year,
           template='plotly_dark',title=country_name+' Annual Urban Population Growth in %',
           labels=dict(x="Years", y="Annual Urban Population Growth in %"))
    fig.show()

a=input('Your Country Name: __ ')

try:
    specific_country(a)
except:
    print('Invalid Country Name')

df=df.sort_values(by='2019', ascending=False)

df = pd.melt(df, id_vars=['Country Name', 'Country Code'], value_vars=lista)
print(df)
fig = px.choropleth(df,                            # Input Dataframe
                     locations="Country Code",           # identify country code column
                     color="value",                     # identify representing column
                     hover_name="Country Name",              # identify hover name
                     animation_frame="variable",        # identify date column
                     projection="natural earth",        # select projection
                     color_continuous_scale = 'Peach',  # select prefer color scale
                     range_color=[-10,10]              # select range of dataset
                     )        
fig.show()
