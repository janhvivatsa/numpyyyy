data = {
    "department": ["IT", "HR", "IT", "HR"],
    "salary": [50000, 40000, 60000, 45000]
}

df = pd.DataFrame(data)

grouped = df.groupby("department")["salary"].mean()
print(grouped)
