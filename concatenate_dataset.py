# %%
import pandas as pd

df1 = pd.read_parquet('geo-reviews-dataset-2023-1.parquet')
df2 = pd.read_parquet('geo-reviews-dataset-2023-2.parquet')

result = pd.concat([df1, df2], ignore_index=True)
print(result)