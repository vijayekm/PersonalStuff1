#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      murugaia
#
# Created:     05/01/2021
# Copyright:   (c) murugaia 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pandas as pd
import numpy as np
import datetime

DB='C:\Vijayekm\Plain.Live\PersonalWorkspaces\jupyter.nb\GTD-01.xlsx'
projects = pd.read_excel(DB, sheet_name='Projects', index_col='Project')
projects.head()

ais = pd.read_excel(DB, sheet_name='Organize')
c0 = ais.replace(np.nan, '', regex=True) #get copy1 from the ais

c1 = c0.loc[c0["Status"]!="Done"].copy()

#get a series with boolean flags indicating if its dated
dated=c1['Target'].apply(lambda x: pd.to_datetime(x,errors='ignore', unit='D')==None)

#append to the DF
c1["dated"] = dated

dated_df = c1.loc[c1["dated"]==True].sort_values(by="Target") # filter only calendered items and sort by date

past_df = dated_df.loc[ pd.to_datetime(dated_df['Target']).dt.date < datetime.datetime.now().date() ]

today_df = dated_df.loc[ pd.to_datetime(dated_df['Target']).dt.date == datetime.datetime.now().date() ]

asap_df = c1.loc[c1["Target"]=="ASAP"].sort_values(by=["ProjPrio","Priority"])

