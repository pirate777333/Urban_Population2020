import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import geopandas as gpd

web_page = requests.get('https://en.wikipedia.org/wiki/Number_of_urban_areas_by_country')

soup = BeautifulSoup(web_page.text, 'html.parser')

columns = ['Nation', 'UA_over_500k','UA_over_1mil','UA_over_2mil','UA_over_5mil']

tables = soup.find_all('table')

#print(len(tables))

table=tables[1]

#print(table)

rows = table.find_all('tr')

Nations = []
UA_500k = []
UA_1mil = []
UA_2mil = []
UA_5mil = []

for row in rows[2:]:
    nation = row.th.text.strip()
    table_data = row.find_all('td')
    ua500 = table_data[0].text.strip()
    ua1 = table_data[1].text.strip()
    ua2 = table_data[2].text.strip()
    ua5 = table_data[3].text.strip()

    Nations.append(nation)
    UA_500k.append(ua500)
    UA_1mil.append(ua1)
    UA_2mil.append(ua2)
    UA_5mil.append(ua5)
    
    #print(nation,ua500,ua1,ua2,ua5)
    #table_data = row.find_all('td')

data4df={columns[0]:Nations, columns[1]:UA_500k,
         columns[2]:UA_1mil, columns[3]:UA_2mil, columns[4]:UA_5mil}

df=pd.DataFrame(data4df)

df.to_csv('Urban_Areas_by_Country_16.csv',index=False)
