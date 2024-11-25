import pandas as pd

df = pd.read_parquet("redshifted_photons.parquet")
df.head()