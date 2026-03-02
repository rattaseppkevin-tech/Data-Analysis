import pandas as pd
import numpy as np

# 1. Genereerime 10 000 rida suvalisi andmeid
n_rows = 10000

# Meeskondade nimekiri, mida kood hakkab suvaliselt valima
teams = ['Arsenal', 'Chelsea', 'Liverpool', 'Man City', 'Man United', 
         'Tottenham', 'Everton', 'Leicester City', 'West Ham', 'Aston Villa']

data = {
    'id': np.arange(4389, 4389 + n_rows),
    'league_name': 'England Premier League',
    'season': '2015/2016',
    'HomeTeam': np.random.choice(teams, n_rows),
    'AwayTeam': np.random.choice(teams, n_rows),
    'HomeGoals': np.random.randint(0, 6, n_rows),
    'AwayGoals': np.random.randint(0, 6, n_rows)
}

# 2. Loome DataFrame'i
premier_league = pd.DataFrame(data)

# 3. Teeme kohe sinu õpitud optimeerimise, et mälu säästa!
premier_league['HomeGoals'] = premier_league['HomeGoals'].astype('int8')
premier_league['AwayGoals'] = premier_league['AwayGoals'].astype('int8')
premier_league['league_name'] = premier_league['league_name'].astype('category')

print(premier_league.head())

print(premier_league.loc[:, ["HomeGoals", "AwayGoals"]].std())

