import pandas as pd
import numpy as np
import streamlit as st
import pandaslib as pl
  
#TODO Write your extraction code here
survey = pd.read_csv('https://docs.google.com/spreadsheets/d/1IPS5dBSGtwYVbjsfbaMCYIWnOuRmJcbequohNxCyGVw/export?resourcekey=&gid=1625408792&format=csv')

survey['year'] = survey['Timestamp'].apply(pl.extract_year_mdy)

survey.to_csv('cache/survey.csv', index=False)

unique_years = survey['year'].unique()

for year in unique_years:
    cost_of_living_data = pd.read_html(f"https://www.numbeo.com/cost-of-living/rankings.jsp?title={year}&displayColumn=0")
    cost_of_living_data =  cost_of_living_data[1]
    cost_of_living_data['year'] = year
    cost_of_living_data.to_csv(f'cache/col_{year}.csv', index=False)

states_url = "https://docs.google.com/spreadsheets/d/14wvnQygIX1eCVo7H5B7a96W1v5VCg6Q9yeRoESF6epw/export?format=csv"
states_data = pd.read_csv(states_url)
states_data.to_csv('cache/states.csv', index=False)