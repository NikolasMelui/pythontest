import numpy as np
import pandas as pd

content = pd.read_csv('revenue-profit.csv',
                      sep=';').rename(columns={'no_data': 'Year'})
print(content)
