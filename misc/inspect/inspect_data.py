import pandas as pd
from pathlib import Path
p = Path(r'c:/Users/Aaradhya/Downloads/_Organized/Fuse AI Fellowship/FUSE AIF 2026 M2/WK7/online_retail_II.xlsx')
df = pd.read_excel(p, sheet_name='Year 2010-2011')
print('shape', df.shape)
print('columns', df.columns.tolist())
print(df.head(5).to_string())
print('dtypes', df.dtypes.to_dict())
print('missing', df.isnull().sum().to_dict())
print('Invoice sample', df['Invoice'].astype(str).head(10).tolist())
print('Unique Customer IDs', df['Customer ID'].nunique(), 'non-null', df['Customer ID'].notnull().sum())
print('InvoiceDate dtype', df['InvoiceDate'].dtype)
