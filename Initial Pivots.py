import pandas as pd
import numpy as np

Data = pd.read_csv('insurance.csv',index_col = False)

factors = list(Data.columns)
del factors[0]
del factors[1]
del factors[4]
print(factors)

for i in factors:
    print(Data.groupby(i)["charges"].agg([np.count_nonzero, np.mean, np.median, np.min, np.max]))




