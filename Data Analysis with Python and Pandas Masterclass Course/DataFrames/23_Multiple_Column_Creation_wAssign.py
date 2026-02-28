import pandas as pd

retail = pd.read_csv(r"C:\Users\Kevin\Desktop\retail.csv")

sample_df = retail.sample(5, random_state=85)

print(sample_df)

sample = sample_df.assign(
    onpromotion_flag = sample_df["onpromotion"] > 0,
    familt_abbrev = sample_df["family"].str[:3],
    onpromotion_ratio = sample_df["sales"] / sample_df["onpromotion"],
    sales_onprom_target = lambda x: x["onpromotion_ratio"] > 100).query("sales_onprom_target == True")

print(sample)