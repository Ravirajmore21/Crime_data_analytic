import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"K:\Crime_Data_Analytics\dataset\data\crime_data.csv")


# ==================================================
# 1. TOP 5 CRIME RECORDS
# ==================================================

top5 = df.nlargest(5, "Cases")

print("\n===== TOP 5 CRIME RECORDS =====")
print(top5)

labels = (
    top5["Year"].astype(str) + " - " +
    top5["City"] + " - " +
    top5["Crime_Type"]
)

plt.figure(figsize=(10, 6))
plt.bar(labels, top5["Cases"])
plt.xlabel("Crime Record")
plt.ylabel("Number of Cases")
plt.title("Top 5 Crime Records")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(r"K:\Crime_Data_Analytics\top5_crime.png")
plt.close()


# ==================================================
# 2. CITY-WISE CRIME TYPE ANALYSIS
# ==================================================

city_crime = df.pivot_table(
    index="City",
    columns="Crime_Type",
    values="Cases",
    aggfunc="sum",
    fill_value=0
)

print("\n===== CITY-WISE CRIME TYPE ANALYSIS =====")
print(city_crime)

city_crime.plot(kind="bar", figsize=(10, 6))
plt.xlabel("City")
plt.ylabel("Number of Cases")
plt.title("City-wise Crime Type Analysis")
plt.xticks(rotation=0)
plt.legend(title="Crime Type")
plt.tight_layout()
plt.savefig(r"K:\Crime_Data_Analytics\city_wise_crime.png")
plt.close()


# ==================================================
# 3. YEAR-WISE CRIME ANALYSIS
# ==================================================

year_crime = df.groupby("Year")["Cases"].sum()

print("\n===== YEAR-WISE CRIME ANALYSIS =====")
print(year_crime)

plt.figure(figsize=(10, 6))
plt.plot(year_crime.index, year_crime.values, marker="o")
plt.xlabel("Year")
plt.ylabel("Total Number of Cases")
plt.title("Year-wise Crime Analysis")
plt.xticks(year_crime.index)
plt.grid(True)
plt.tight_layout()
plt.savefig(r"K:\Crime_Data_Analytics\year_wise_crime.png")
plt.close()


# ==================================================
# 4. CRIME-TYPE WISE ANALYSIS
# ==================================================

crime_type = (
    df.groupby("Crime_Type")["Cases"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== CRIME-TYPE WISE ANALYSIS =====")
print(crime_type)

plt.figure(figsize=(10, 6))
plt.bar(crime_type.index, crime_type.values)
plt.xlabel("Crime Type")
plt.ylabel("Total Number of Cases")
plt.title("Crime-Type Wise Analysis")
plt.tight_layout()
plt.savefig(r"K:\Crime_Data_Analytics\crime_type_wise.png")
plt.close()


print("\n===== ALL ANALYSIS COMPLETED SUCCESSFULLY =====")
print("Graphs saved in K:\\Crime_Data_Analytics")
# ==================================================
# 5. CITY-WISE TOTAL CRIME ANALYSIS
# ==================================================

city_total = (
    df.groupby("City")["Cases"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== CITY-WISE TOTAL CRIME ANALYSIS =====")
print(city_total)

plt.figure(figsize=(10, 6))

plt.bar(city_total.index, city_total.values)

plt.xlabel("City")
plt.ylabel("Total Number of Cases")
plt.title("City-wise Total Crime Analysis")

plt.tight_layout()

plt.savefig(
    r"K:\Crime_Data_Analytics\city_total_crime.png"
)

plt.close()
# ==================================================
# 6. CRIME PERCENTAGE ANALYSIS
# ==================================================

total_cases = df["Cases"].sum()

crime_percentage = (
    df.groupby("Crime_Type")["Cases"]
    .sum()
    .sort_values(ascending=False)
)

crime_percentage = (crime_percentage / total_cases) * 100

print("\n===== CRIME PERCENTAGE ANALYSIS =====")
print(crime_percentage.round(2))

plt.figure(figsize=(8, 6))

plt.pie(
    crime_percentage,
    labels=crime_percentage.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Crime Type Percentage Distribution")
plt.tight_layout()

plt.savefig(
    r"K:\Crime_Data_Analytics\crime_percentage.png"
)

plt.close()
# ==================================================
# 7. HIGHEST CRIME CITY + CRIME TYPE
# ==================================================

city_crime_top = df.loc[
    df["Cases"].idxmax()
]

print("\n===== HIGHEST CRIME CITY + CRIME TYPE =====")
print("Year       :", city_crime_top["Year"])
print("City       :", city_crime_top["City"])
print("Crime Type :", city_crime_top["Crime_Type"])
print("Cases      :", city_crime_top["Cases"])
# ==================================================
# 8. YEAR-OVER-YEAR CRIME CHANGE
# ==================================================

year_total = df.groupby("Year")["Cases"].sum()

year_change = year_total.pct_change() * 100

print("\n===== YEAR-OVER-YEAR CRIME CHANGE =====")

result = pd.DataFrame({
    "Total Cases": year_total,
    "Change (%)": year_change.round(2)
})

print(result)

# Graph
plt.figure(figsize=(10, 6))

plt.plot(
    result.index,
    result["Change (%)"],
    marker="o"
)

plt.axhline(y=0, linestyle="--")

plt.xlabel("Year")
plt.ylabel("Change (%)")
plt.title("Year-over-Year Crime Change")

plt.xticks(result.index)
plt.grid(True)

plt.tight_layout()

plt.savefig(
    r"K:\Crime_Data_Analytics\year_over_year_change.png"
)

plt.close()# ==================================================
# 9. FINAL DATA INSIGHTS
# ==================================================

highest_city = city_total.idxmax()
highest_city_cases = city_total.max()

highest_crime = crime_type.idxmax()
highest_crime_cases = crime_type.max()

highest_year = year_crime.idxmax()
highest_year_cases = year_crime.max()

highest_growth_year = year_change.idxmax()
highest_growth = year_change.max()

print("\n========================================")
print("          FINAL DATA INSIGHTS")
print("========================================")

print(f"\n1. Highest crime city: {highest_city}")
print(f"   Total cases: {highest_city_cases}")

print(f"\n2. Most common crime type: {highest_crime}")
print(f"   Total cases: {highest_crime_cases}")

print(f"\n3. Highest crime year: {highest_year}")
print(f"   Total cases: {highest_year_cases}")

print(f"\n4. Highest year-over-year increase: {highest_growth_year}")
print(f"   Increase: {highest_growth:.2f}%")

print("\n5. Crime percentage distribution:")
for crime, percentage in crime_percentage.items():
    print(f"   {crime}: {percentage:.2f}%")

print("\n========================================")
print("       PROJECT ANALYSIS COMPLETED")
print("========================================")