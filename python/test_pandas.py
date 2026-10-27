import pandas as pd

data = {
    "Crime": ["Theft", "Robbery", "Murder"],
    "Cases": [120, 50, 10]
}

df = pd.DataFrame(data)

print(df)