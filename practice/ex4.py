#This program
#   - Asks user to enter a number of hours studied per week (hours)
#       - If number is negative, print "Invalid input."
#       - Dont evaluate anything else.
#   - Otherwise, categorize study habits:
#       - 0-4 hours -> "Minimal"
#       - 5-9 hours -> "Moderate"
#       - 10-19 hours -> "Serious"
#       - 20+ hours -> "Intense"
#   - The, nested inside the "Intense" case, ask a follow up question.

hours = int(input("Enter a number of hours studied per week: "))
is_valid = False

while is_valid == False:
    if hours < 0:
        print("Invalid input")
        hours = int(input("Enter a number of hours studied per week: "))
    else:
        is_valid = True

if hours < 4:
    print("Minimal")
elif hours < 10:
    print("Moderate")
elif hours < 20:
    print("Serious")
else:
    print("Intense")
    job = input("Are you also working a job? (yes/no): ")
    if job.lower() == "yes":
        print("Consider your workload — that's a lot to balance")