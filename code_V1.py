#importing packagers required.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

#importing the data
df = pd.read_csv('data.csv')
df.head()
df.shape
#dataset contain 14 coloums as 10,000 rows 

df.info()

#considering both numarical and non-numarical data 
df.describe(include='all').T

#Initially remove unused columns 
df = df[[
   #'UDI', 'Product ID', 
   'Type', 'Air temperature [K]',
       'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]',
       'Tool wear [min]', 'Machine failure', 
       #'TWF', 'HDF', 'PWF', 'OSF',
       #'RNF'
    ]].copy()  
 df.head()
 
 df.shape
 #after removing uncessory columns colums reduced to 7 
 new_names = {
      'Air temperature [K]':'Air_temperature_[K]', 'Process temperature [K]':'Process_temperature_[K]',
       'Rotational speed [rpm]':'Rotational_speed_[rpm]', 'Torque [Nm]':'Torque_[Nm]', 'Tool wear [min]':'Tool_wear_[min]',
       'Machine failure':'Machine_failure'
            }
     
 
 df = df.rename(columns=new_names)
 
 df.columns
 
 df.head()
 
 #check for correlation 
 
 plt.figure(figsize=(10,10))
 correlation_matrix = df.corr()
 sns.heatmap(correlation_matrix,annot = True, cmap='coolwarm')
 plt.title("Correlation Heatmap")
 plt.show()
 
 '''there is a strong positive correlation between Air_temperature and the Process_temperature.  
    there is a strong negative correlation between Torque and rotationa speed.
    we can remove one of temperature based on the correlation. 
 '''
 