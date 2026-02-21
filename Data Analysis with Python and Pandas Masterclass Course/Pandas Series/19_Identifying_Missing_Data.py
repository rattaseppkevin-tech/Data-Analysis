import pandas as pd
import numpy as np

# 1. Teeme andmed, kus on meelega tühjad kohad (NaN ja None)
data = {
    'Toode': ['Saapad', 'Särgid', 'Püksid', 'Särgid', 'Särgid', 'Püksid'],
    'Müük': [100, np.nan, 150, np.nan, 200, np.nan]
}

df = pd.DataFrame(data)

# 2. .isna() muudab kõik väärtused True (kui on tühi) või False (kui on olemas)
# 3. .value_counts() loeb kokku, mitu True-d ja False-i on
missing_report = df['Müük'].isna().value_counts()

print("Kas väärtus on puudu?")
print(missing_report)