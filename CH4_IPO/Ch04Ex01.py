# This program keeps a running total of the number of bugs collected during a span of a week

total_bugs = 0
bugs_collected = 0

for day in range(1, 8):
    bugs_collected = int(input(f"Enter the number of bugs collected on day {day}: "))
    total_bugs += bugs_collected
print(f"You collected a total of {total_bugs} bugs.")