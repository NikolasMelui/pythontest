import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

content = pd.read_csv('revenue-profit.csv',
                      sep=';').rename(columns={'no_data': 'Year'})
print(content)

plt.plot(content.Year, content.Revenue)
plt.xlabel('Year')
plt.ylabel('Revenue')
plt.show()
