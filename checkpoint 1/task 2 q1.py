players20 = pd.read_csv("c:/Users/emily/Documents/CMU MSP/stat 650/final project/data/players_20.csv")
players19 = pd.read_csv("c:/Users/emily/Documents/CMU MSP/stat 650/final project/data/players_19.csv")

# select long name and overall columns
df1 = players20[["long_name", "overall"]]
df2 = players19[["long_name", "overall"]]

# merge dataframes so the same players are being displayed
common = df1.merge(df2, on = ["long_name"])

# rename columns
df3 = common.rename(columns={'overall_x': '2020_overall', 'overall_y': '2019_overall', 'long_name': 'Name'})

# add in difference column
df3['Difference'] = df3['2020_overall'] - df3['2019_overall']

# sort largest to smallest difference
df3 = df3.sort_values(by = 'Difference', ascending = False)

# 10 most improved players
df3.head(x)
