import pandas as pd

df_titles = pd.read_csv('data/prices_pigs.csv')
df_prices = pd.read_csv('data/price_pigs_scraped.csv')

df_all = df_titles.set_index('url').join(df_prices.set_index('url'))

df_all.to_csv('data/price_pigs_full.csv')
