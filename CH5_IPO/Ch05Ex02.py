# This program asks the user to enter the square feet of wall space to be painted and the price of the paint per gallon.

LABOR_CHARGE_PER_HOUR = 45.00

def title() -> None:
    print("***********************")
    print("* PAINT JOB ESTIMATOR *")
    print("***********************")
    
def paint_cost(gallons: int, paint_price: float) -> float:
    return gallons * paint_price

def labor_cost(charge_per_hour: float, labor_hours: int) -> float:
    return charge_per_hour * labor_hours

def paint_job_cost(paint_cost: float, labor_cost: float) -> float:
    return paint_cost + labor_cost

def main() -> None:
    title()

    wall_space = int(input("Enter wall space in square feet: "))
    paint_price = float(input("Enter paint price per gallon: "))
    total_gallons = wall_space // 90
    if wall_space % 90 != 0:
        total_gallons += 1
    total_hours = total_gallons * 7
    total_paint_cost = paint_cost(total_gallons, paint_price)
    total_labor_cost = labor_cost(LABOR_CHARGE_PER_HOUR, total_hours)
    total_paint_job_cost = paint_job_cost(total_paint_cost, total_labor_cost)

    print(f"\nThe total gallons of paint needed for the job is {total_gallons}")
    print(f"The total of hours of labor required for the job is {total_hours}")
    print(f"The total paint cost for the job is ${total_paint_cost:,.2f}")
    print(f"The total labor cost for the job is ${total_labor_cost:,.2f}")
    print(f"**********************************************************")
    print(f"Total estimate for the paint job totals to ${total_paint_job_cost:,.2f}")

if __name__ == "__main__":
    main()


