import pandas as pd

import requests

from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.71455000000003&lon=-74.00713999999994#.YQlJMI4zbIU')
soup = BeautifulSoup(page.content,'html.parser')
week = soup.find(id =  'seven-day-forecast-body')
#print(week)
items = week.findAll(class_= 'tombstone-container')
#print(items)
#print(items[0].find(class_='period-name').get_text())
#print(items[0].find(class_='short-desc').get_text())
#print(items[0].find(class_='temp').get_text())
period_names = [item.find(class_='period-name').get_text() for item in items]
short_desc = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]
#print(period_names)
#print(short_desc)
#print(temperatures)
weather_stuff = pd.DataFrame({
    'period': period_names,
    'short_description' : short_desc,
    'temperature' : temperatures,
})
print(weather_stuff)
