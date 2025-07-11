
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("unemployment_data.csv")

# Print basic stats
print("Average Unemployment Rate:", df['Unemployment_Rate'].mean())
print("Country with highest unemployment:", df.loc[df['Unemployment_Rate'].idxmax(), 'Country'])

# Plot
plt.figure(figsize=(10, 6))
plt.bar(df['Country'], df['Unemployment_Rate'])
plt.title('Unemployment Rate in Europe (2020)')
plt.xlabel('Country')
plt.ylabel('Unemployment Rate (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("unemployment_plot.png")
plt.show()
