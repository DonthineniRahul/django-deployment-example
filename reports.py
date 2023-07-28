import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv("C:/Users/Rahul Virat/Downloads/tourism/20- average-expenditures-of-tourists-abroad.csv")
df.sort_values(by ='Entity', inplace = True)
df['cummulative Tourism'] = df['Outbound Tourism Expenditure (adjusted for US 2021 inflation)'].cumsum()
print(df)

plt.figure(figsize=(5,10))
plt.plot(df['Entity'], df['cummulative Tourism'], marker='o', linestyle ='-')
plt.title('Toturism Trend')
plt.xlabel('Entity')
plt.ylabel('cummulative Tourism')
plt.xticks(rotation=45)
plt.show()

plt.savefig('tourism_trends.png')