#%%
import pandas as pd

df = pd.read_csv("../data/haikus.csv")

# %%
df.isna().sum()
# %%
df[df["2"].isna()]
