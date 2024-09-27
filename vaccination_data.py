import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('bmh')

data = pd.read_csv('vaccination_data.csv')

sns.set(style="whitegrid")


data['First-dose matched'] = data['First-dose matched (%)'].str.extract('(\d+)').astype(int)
data['Second-dose matched'] = data['Second-dose matched (%)'].str.extract('(\d+)').astype(int)


df_melted = data.melt(id_vars=["Region"], 
                    value_vars=["First-dose vaccinated", "Second-dose vaccinated", 
                                "First-dose matched", "Second-dose matched"], 
                    var_name="Category", 
                    value_name="Value")


plt.figure(figsize=(12, 6))
sns.barplot(x="Region", y="Value", hue="Category", data=df_melted, palette="muted")


plt.title("Vaccination Counts and Matched Numbers by Region")
plt.xlabel("Region")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.legend(title="Categories")

plt.tight_layout()
plt.savefig('vaccination_graph.png')

plt.show()
