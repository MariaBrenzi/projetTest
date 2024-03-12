# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 10:19:43 2023

@author: famil
"""

import pandas as pd
import streamlit as st
df=pd.read_csv('Kickstarter Campaigns DataSet.csv')
st.write("Aperçu des données")
st.dataframe(df.head())