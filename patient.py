Name :- Hari singh r
batch id:- DSWDMCOD 25082022 B

import pandas as pd
from lifelines import KaplanMeierFitter

patient_data=pd.read_csv("D:/assignments of data science/22 survival analytics/Patient.csv")
patient_data.head()
patient_data.describe()

patient_data["Followup"].describe()

#defining followup of the customer
T = patient_data.Followup

kmf = KaplanMeierFitter()

#Fitting the model on followup and event type of the data set
kmf.fit(T, event_observed=patient_data.Eventtype)

# Time-line estimations plot 
kmf.plot()


#Fitting the model for different PatientID's
patient_data.PatientID.value_counts()

# Applying KaplanMeierFitter model on different patients
kmf.fit(T[patient_data.PatientID], patient_data.Eventtype[patient_data.PatientID])
ax = kmf.plot()
