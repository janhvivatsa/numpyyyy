print(df["name"])           # single column
print(df[["name", "age"]])  # multiple columns

print(df.iloc[0])           # first row
print(df.loc[0, "name"])    # specific value
