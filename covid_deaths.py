import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('bmh')


data = pd.read_csv('covid_heart_attack_deaths_mumbai.csv')


labels = ['Covid deaths in 2020', 'Covid deaths in 2021', 
          'Heart attack deaths in 2020', 'Heart attack deaths in Jan-Jun 2021']
sizes = [11105, 10289, 5633, 17880]
colors = ['blue', 'red', 'green', 'pink']


def func(pct, allvalues):
    absolute = int(pct / 100. * sum(allvalues))  
    return f'{absolute} ({pct:.1f}%)'  

plt.figure(figsize=(7, 7))  

plt.pie(sizes, labels=labels, colors=colors, autopct=lambda pct: func(pct, sizes), 
        startangle=90)
plt.title('Covid-19 and Heart Attack Deaths in Mumbai')
plt.axis('equal')  
plt.savefig('covid_deaths.png')
plt.show()
