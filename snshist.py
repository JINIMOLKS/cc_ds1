import matplotlib.pyplot as plt
import seaborn as sns
df=sns.load_dataset("tips")
sns.histplot(df["total_bill"],bins=20,kde=True,color="skyblue")
plt.title("Histogram + KDE")
plt.show()