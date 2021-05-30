import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

Data = pd.read_csv('insurance.csv',index_col=False)
Data["Child_Cat"] = np.where(Data["children"] >1, "0 - 1", "2+")
Data["BMI_Cat"] = np.where(Data["bmi"] < 30, "<30", "30+")

smoker = Data[Data['smoker'] == 'yes']
nonsmoker = Data[Data['smoker'] == 'no']

p1 = sns.relplot(x='age', y='charges', hue='BMI_Cat', col='region', data=smoker)
p2 = sns.relplot(x='age', y='charges', hue='BMI_Cat', col='Child_Cat', data=smoker)

plt.show()