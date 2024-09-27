import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('bmh')


data = pd.read_csv('provisional_mortality_2023_2024.csv')
data.columns = data.columns.str.strip() 


data_melted = data.melt(id_vars=["Age group (years)"], 
                         var_name="Week", 
                         value_name="Impact")


plt.figure(figsize=(12, 6))


colors = ['blue', 'orange', 'green', 'red', 'purple', 'cyan']

sns.barplot(x='Week', y='Impact', hue='Age group (years)', 
            data=data_melted, palette=colors, ci=None,width=1.0)


plt.title('Provisional Mortality across Age Groups')
plt.xlabel('Week')
plt.ylabel('Impact')

plt.xticks(rotation=45)

plt.legend(title="Age Groups" ,bbox_to_anchor=(1.2, 1))

plt.tight_layout()

plt.savefig('provisional_mortality.png')

plt.show()
