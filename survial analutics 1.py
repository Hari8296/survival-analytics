Name :- Hari singh r
batch id:- DSWDMCOD 25082022 B

import pandas as pd
from lifelines import KaplanMeierFitter

sa=pd.read_csv("D:/assignments of data science/22 survival analytics/Patient.csv")
sa.head()
sa.describe()

sa.Followup.describe()

t=sa.Followup
e=sa.Eventtype

kmf=KaplanMeierFitter()

kmf.fit(t, Eventtype_observed = sa.Eventtype)
kmf.fit(t, event_observed = e)

kmf.plot()

sa.Scenario.value_counts()
kmf.fit(t[sa.Scenario==1],sa.Eventtype[sa.Scenario==1],label='1')

kmf.fit(T[survival_unemp.ui==1], survival_unemp.event[survival_unemp.ui==1], label='1')
ax = kmf.plot()
