import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Data = pd.read_csv('insurance.csv',index_col=False)

p1 = sns.pairplot(Data, x_vars=['age','bmi'], y_vars=['charges'],kind = 'reg')

plt.show()

