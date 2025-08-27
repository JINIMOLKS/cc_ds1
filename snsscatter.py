import seaborn as sns
df = sns.load_dataset("tips")
import matplotlib.pyplot as plt
sns.scatterplot(x="total_bill",y="tip",data=df,hue="sex",style="time")
plt.title=("Scatter Plot")
plt.show()