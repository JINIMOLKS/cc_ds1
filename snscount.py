import seaborn as sns
df=sns.load_dataset("tips")
import matplotlib.pyplot as plt
sns.countplot(x="day",data=df,palette="Set2")
plt.title("Count Plot")
plt.show()