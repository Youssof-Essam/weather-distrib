import pandas as pd
import seaborn as sns

df = pd.read_csv("data/open-meteo-52.50N13.50E38m.csv")
print(df.head())

df = df.dropna().set_index(["location_id","time"])
df.to_csv("data/open-meteo-52.50N13.50E38m.csv")
