# This program collects data and calculates the average rainfall over a period of years.abs

rainfall_years = int(input("Enter the number of rainfall years to record: "))
total_rainfall = 0
rainfall_amount = 0
for year in range(1,rainfall_years + 1):
    print("\n**************")
    print(f"*** Year {year} ***")
    print("**************")
    for month in range(1, 13):
        rainfall_amount = int(input(f"Enter the rainfall amount for (year {year}/month {month}): "))
        total_rainfall += rainfall_amount
total_months_of_rain = rainfall_years * 12
avg_rainfall = total_rainfall / total_months_of_rain
print(f"\nFor {rainfall_years * 12} months, there was a total rainfall of {total_rainfall:.1f} inches with an average monthly rainfall of {avg_rainfall:.1f} inches.")