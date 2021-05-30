import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

Data = pd.read_csv('insurance.csv',index_col=0)
p1 = sns.boxplot(x='region', y='charges', data=Data)
p1.set_title('Box plot of charges by region')


plt.show()