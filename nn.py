import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 22],
    "salary": [50000, 60000, 45000]
}

df = pd.DataFrame(data)
print(df)
