import pandas as pd
import matplotlib.pyplot as plt

Data = pd.read_csv('insurance.csv',index_col=False)

smoker = list(Data['charges'][Data['smoker'] == 'yes'])
nonsmoker = list(Data['charges'][Data['smoker'] == 'no'])

plt.hist(smoker, bins = 20,alpha = 0.5, label = 'smoker')
plt.hist(nonsmoker, bins = 20,alpha = 0.5, label = 'non-smoker')
plt.legend(loc = 'upper right')
plt.show()

