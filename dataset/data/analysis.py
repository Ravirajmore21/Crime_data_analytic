import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"K:\Crime_Data_Analytics\dataset\data\crime_data.csv")

print("Dataset loaded successfully!")

# =========================
# BASIC ANALYSIS
# =========================

year_cases = df.groupby("Year")["Cases"].sum()
city_cases = df.groupby("City")["Cases"].sum()
crime_cases = df.groupby("Crime_Type")["Cases"].sum()

print("\n===== YEAR-WISE CASES =====")
print(year_cases)

print("\n===== CITY-WISE CASES =====")
print(city_cases)

print("\n===== CRIME TYPE-WISE CASES =====")
print(crime_cases)

# =========================
# CRIME INSIGHTS
# =========================

print("\n===== CRIME INSIGHTS =====")

print(f"Highest crime year: {year_cases.idxmax()} ({year_cases.max()} cases)")
print(f"Highest crime city: {city_cases.idxmax()} ({city_cases.max()} cases)")
print(f"Most common crime type: {crime_cases.idxmax()} ({crime_cases.max()} cases)")
print(f"Lowest crime type: {crime_cases.idxmin()} ({crime_cases.min()} cases)")

# =========================
# BASIC STATISTICS
# =========================

print("\n===== BASIC STATISTICS =====")

print(f"Total cases: {df['Cases'].sum()}")
print(f"Average cases per record: {df['Cases'].mean():.2f}")
print(f"Maximum cases in a record: {df['Cases'].max()}")
print(f"Minimum cases in a record: {df['Cases'].min()}")

# =========================
# YEARLY TREND
# =========================

print("\n===== YEARLY TREND ANALYSIS =====")

first_year = year_cases.iloc[0]
last_year = year_cases.iloc[-1]

change = last_year - first_year
percentage_change = (change / first_year) * 100

print(f"Cases in {year_cases.index[0]}: {first_year}")
print(f"Cases in {year_cases.index[-1]}: {last_year}")
print(f"Change in cases: {change}")
print(f"Percentage change: {percentage_change:.2f}%")

# =========================
# CITY-WISE CRIME TYPE
# =========================

print("\n===== CITY-WISE CRIME TYPE ANALYSIS =====")

city_crime = pd.pivot_table(
    df,
    values="Cases",
    index="City",
    columns="Crime_Type",
    aggfunc="sum",
    fill_value=0
)

print(city_crime)

# =========================
# GRAPHS
# =========================

plt.figure(figsize=(12, 8))

# Year-wise
plt.subplot(2, 2, 1)
plt.plot(year_cases.index, year_cases.values, marker="o")
plt.title("Year-wise Crime Cases")
plt.xlabel("Year")
plt.ylabel("Cases")
plt.grid(True)

# City-wise
plt.subplot(2, 2, 2)
plt.bar(city_cases.index, city_cases.values)
plt.title("City-wise Crime Cases")
plt.xlabel("City")
plt.ylabel("Cases")

# Crime type-wise
plt.subplot(2, 2, 3)
plt.bar(crime_cases.index, crime_cases.values)
plt.title("Crime Type-wise Cases")
plt.xlabel("Crime Type")
plt.ylabel("Cases")
plt.xticks(rotation=30)

plt.tight_layout()
plt.show()
# Top 5 Crime Records
print("\n===== TOP 5 CRIME RECORDS =====")

top_records = df.sort_values(
    by="Cases",
    ascending=False
).head(5)

print(top_records)
