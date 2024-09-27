import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

plt.style.use('bmh')

data = pd.read_csv('social_media_impact1.csv')

sns.set(style="whitegrid")

df = pd.DataFrame(data)
plt.figure(figsize=(10,6))

plt.plot(df['Measure'], df['Positive Impact (%)'], marker='o', label='Positive Impact (%)', color='g')
plt.plot(df['Measure'], df['Negative Impact (%)'], marker='o', label='Negative Impact (%)', color='r')

plt.title('Positive vs Negative Impacts across Categories', fontsize=14)
plt.xlabel('Measures', fontsize=12)
plt.ylabel('Impact (%)', fontsize=12)


plt.xticks(rotation=90)

plt.legend()

plt.tight_layout()
plt.savefig("social_media.png")
plt.show()
