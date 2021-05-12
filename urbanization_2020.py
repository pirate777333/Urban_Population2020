import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

web_page = requests.get('https://en.wikipedia.org/wiki/Urbanization_by_country')

soup = BeautifulSoup(web_page.text, 'html.parser')

columns = ['Nation', 'Urban_Population%','Urbanization_Rate%_15to20']

table = soup.table.tbody

rows = table.find_all('tr')

nations = []
urban_population = []
urbanization_rate = []

#1,2,4
for row in rows[1:]:
    table_data = row.find_all('td')
    #print(table_data)
    nation = table_data[1].find('span').text.strip()
    up = table_data[2].text.strip()
    ur = table_data[4].text.strip()
    nations.append(nation)
    urban_population.append(up)
    urbanization_rate.append(ur)

data4df={columns[0]:nations,columns[1]:urban_population,
      columns[2]:urbanization_rate}

df=pd.DataFrame(data4df)

df.to_csv('Urbanization_by_country_2020.csv',index=False)

#print(table)
