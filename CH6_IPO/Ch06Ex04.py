# days in each month
JAN = 31
FEB = 28
MAR = 31
APR = 30
MAY = 31
JUN = 30
JUL = 31
AUG = 31
SEP = 30
OCT = 31
NOV = 30
DEC = 31

# month name
JAN_NAME = "January"
FEB_NAME = "February"
MAR_NAME = "March"
APR_NAME = "April"
MAY_NAME = "May"
JUN_NAME = "June"
JUL_NAME = "July"
AUG_NAME = "August"
SEP_NAME = "September"
OCT_NAME = "October"
NOV_NAME = "November"
DEC_NAME = "December"

def avg_steps_in_month(file, month: str, days_in_month: int) -> None:
    total = 0
    for _ in range(days_in_month):
        total += int(file.readline())
    print(f"The average steps taken in {month} was {(total / days_in_month):,.1f}")
 
def main() -> None:
    with open("steps.txt", "r") as file_to_read:
        avg_steps_in_month(file_to_read, JAN_NAME, JAN)
        avg_steps_in_month(file_to_read, FEB_NAME, FEB)
        avg_steps_in_month(file_to_read, MAR_NAME, MAR)
        avg_steps_in_month(file_to_read, APR_NAME, APR)
        avg_steps_in_month(file_to_read, MAY_NAME, MAY)
        avg_steps_in_month(file_to_read, JUN_NAME, JUN)
        avg_steps_in_month(file_to_read, JUL_NAME, JUL)
        avg_steps_in_month(file_to_read, AUG_NAME, AUG)
        avg_steps_in_month(file_to_read, SEP_NAME, SEP)
        avg_steps_in_month(file_to_read, OCT_NAME, OCT)
        avg_steps_in_month(file_to_read, NOV_NAME, NOV)
        avg_steps_in_month(file_to_read, DEC_NAME, DEC)


if __name__ == "__main__":
    main()