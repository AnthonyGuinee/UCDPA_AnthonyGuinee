import pandas as pd


Data = pd.read_csv('insurance.csv',index_col=0)

nrow = len(Data)
i=0
sum_low = 0
count_low = 0
sum_med = 0
count_med = 0
sum_high = 0
count_high = 0

Data["Rank"] = Data["charges"].rank()
Data = Data.set_index("Rank")
Data_sort = Data.sort_index(ascending = False)
Count5PC = round((Data["charges"].count() * 0.05),0)
print(Count5PC)
Top5PCClaims = Data_sort.iloc[0:67]
UpperBoundclaim = Top5PCClaims["charges"].min()
Mean = round(Data["charges"].mean(),2)
Count = round(Data["charges"].count())
TotalClaims = round(Data["charges"].sum(),2)

while i < (nrow - 1):
    if Data.iloc[i,5] < Mean:
        sum_low = sum_low + Data.iloc[i,5]
        count_low = count_low + 1
    elif Data.iloc[i,5] < UpperBoundclaim:
        sum_med = sum_med + Data.iloc[i,5]
        count_med = count_med + 1
    else:
        sum_high = sum_high + Data.iloc[i,5]
        count_high = count_high + 1
    i = i + 1

PLow = "{:.0%}".format(round(sum_low,2)/TotalClaims)
PMed = "{:.0%}".format(round(sum_med,2)/TotalClaims)
PHigh = "{:.0%}".format(round(sum_high,2)/TotalClaims)

print("For",count_low,"Claims,",PLow,"of total claims was paid out where total charge was less than",Mean)
print("For",count_med,"Claims,",PMed,"of total claims was paid out where total charge was greater than",Mean,"and less than",UpperBoundclaim)
print("For",count_high,"Claims,",PHigh,"of total claims was paid out where total charge was greater than or equal to",UpperBoundclaim)
