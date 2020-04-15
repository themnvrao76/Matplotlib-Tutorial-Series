from matplotlib import pyplot as plt
import pandas as pd
plt.style.use("fivethirtyeight")
data=pd.read_csv("hist.csv")
age=data["Age"]
bins=[10,20,30,40,50,60,70,80,90]
plt.hist(age,bins=bins,edgecolor="black",color="Purple")
plt.title("Survey")
plt.xlabel("Ages")
plt.ylabel("Total")
plt.show()