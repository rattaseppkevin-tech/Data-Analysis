import pandas as pd

sales = pd.read_csv(r"C:\Users\Kevin\Desktop\transactions.csv")

filtering = sales.query("transactions > 2000").shape[0]
first_calc = (filtering / sales.shape[0])
print(first_calc)

sec_filtering = sales.query("store_nbr == 25 and transactions > 2000")
tervik = sales.query("store_nbr == 25")
second_calc = sec_filtering.shape[0] / tervik.shape[0]
print(second_calc)
print(sec_filtering["transactions"].sum())

third_filtering = sales.query("store_nbr in [3, 25] and date.str.contains('-05-|-06-') and transactions < 2000")
sum_stores = third_filtering["transactions"].sum()
print(sum_stores)


mask = (
    (sales["store_nbr"].isin([3, 25])) & 
    (sales["date"].str.contains("-05-|-06-")) & 
    (sales["transactions"] < 2000)
)

final_df = sales.loc[mask]

print("Poodide kontroll:", final_df["store_nbr"].unique())
print("Kuude kontroll:", final_df["date"].str[5:7].unique())
print("Lõplik summa:", final_df["transactions"].sum())