# %%
# Делим parquet пополам, чтобы уместить в гитхаб
import pandas as pd
df = pd.read_parquet('geo-reviews-dataset-2023.parquet')
df1 = df.head(250000)
df2 = df.tail(250000)
# %%
df1.to_parquet('geo-reviews-dataset-2023-1.parquet')
df2.to_parquet('geo-reviews-dataset-2023-2.parquet')