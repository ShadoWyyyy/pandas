import pandas as pd
import matplotlib.pyplot as plt
# load a csv file
df = pd.read_csv('pandas/data.csv')
# Render a DataFrame to a console-friendly tabular output
print(df.to_string())
# Check version
print(pd.__version__)
print(pd.options.display.max_rows)

# load a json file
df = pd.read_json('pandas/data.json')
print(df.info())

# cleaning empty cells
df["Pulse"].dropna(inplace=True)
df["Calories"].fillna(df["Calories"].mean(), inplace=True)
print(df["Maxpulse"].mode()[0]) # Mode = the value that appears most frequently.

# dealing with wrong format
df['Date'] = pd.to_datetime(df['Date'])

# dealing with wrong data
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120
    elif df.loc[x, "Duration"] > 240:
        df.drop(x, inplace=True)

# Remove duplicates
print(df.duplicated())
df.drop_duplicates(inplace = True)

# Correlations
print(df.corr())

# Plotting
df.plot()
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
df["Duration"].plot(kind = 'hist')