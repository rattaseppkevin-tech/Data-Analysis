import pandas as pd

sales = pd.read_csv(r"C:\Users\Kevin\Desktop\transactions.csv")

# 1. Eemaldame ESIMESE rea püsivalt
# Kasutame iloc[1:], et jätta alles kõik alates indeksist 1
sales = sales.iloc[1:]

# 2. Eemaldame "date" tulba (mitte püsivalt, vaid vaatamiseks)
print(sales.drop("date", axis=1).head())

# 3. LEIAME IGA POE VIIMASE REA
# keep="last" jätab alles kõige viimase sissekande iga poe numbri kohta
last_entries = sales.drop_duplicates(subset="store_nbr", keep="last")

print(last_entries.head())