import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

Data = pd.read_csv('insurance.csv',index_col=False)
Data["BMI_Cat"] = np.where(Data["bmi"] < 30.0, "<30", "30+")

smoker = Data[Data['smoker'] == 'yes']
nonsmoker = Data[Data['smoker'] == 'no']

p1 = sns.lmplot(x='bmi', y='charges', hue='smoker', data=Data)
p2 = sns.lmplot(x='age', y='charges', hue='smoker', data=Data)
p3 = sns.relplot(x='bmi', y='charges', col='smoker', data=Data)
p4 = sns.relplot(x='age', y='charges', col='smoker', data=Data)
p5 = sns.pairplot(Data, x_vars=['age','bmi'], y_vars=['charges'],kind = 'reg',hue = 'smoker')


p6 = sns.relplot(x='age', y='charges', col='BMI_Cat', data=smoker)

plt.show()