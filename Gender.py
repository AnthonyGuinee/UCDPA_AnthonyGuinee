import pandas as pd
import matplotlib.pyplot as plt

Data = pd.read_csv('insurance.csv',index_col=0)

male = list(Data['charges'][Data['sex'] == 'male'])
female = list(Data['charges'][Data['sex'] == 'female'])

plt.hist(male, bins = 20,alpha = 0.5, label = 'male')
plt.hist(female, bins = 20,alpha = 0.5, label = 'female')
plt.legend(loc = 'upper right')
plt.show()