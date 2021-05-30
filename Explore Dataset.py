import pandas as pd
import matplotlib.pyplot as plt

Data = pd.read_csv('insurance.csv',index_col=False)

print(Data.shape)
print(Data.head())
print(Data.info())
print(Data.count())

for i in Data.columns:
    vals = Data[i].unique()

    if len(vals)<10:
        print("The variable ",i,"has",len(vals)," unique values.")
        print("They are",vals)
    else:
        print("The variable", i, "can take many values")
        print("The min value is", vals.min(),". The max value is",vals.max() )

charges = list(Data['charges'])

plt.hist(charges, bins = 30)
plt.show()


