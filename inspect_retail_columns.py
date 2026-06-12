import pandas as pd
from pathlib import Path
p = Path('online_retail_II.xlsx')
df = pd.read_excel(p, sheet_name='Year 2010-2011')
print('columns:', df.columns.tolist())
print('sample head:')
print(df.head(3).to_dict(orient='list'))
