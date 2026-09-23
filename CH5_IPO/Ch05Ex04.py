# This program displays a latter grade for each score and the average test score in a table format

# calc_average function - accept 8 test scores as arguments and return the average of the scores
def calc_average(score_one: int, score_two: int, score_three: int, score_four: int, score_five: int, score_six: int, score_seven:int, score_eight: int) -> float:
    return (score_one + score_two + score_three + score_four + score_five + score_six + score_seven + score_eight) / 8

# determine_grade - accept a test score as an argument and return a letter grade for the score
def determine_grade(test_score: int | float) -> str:
    if test_score < 60:
        return "F"
    elif test_score < 62:
        return "D-"
    elif test_score < 68:
        return "D"
    elif test_score < 70:
        return "D+"
    elif test_score < 72:
        return "C-"
    elif test_score < 78:
        return "C"
    elif test_score < 80:
        return "C+"
    elif test_score < 82:
        return "B-"
    elif test_score < 88:
        return "B"
    elif test_score < 90:
        return "B+"
    elif test_score < 92:
        return "A-"
    elif test_score < 98:
        return "A"
    else:
        return "A+"


def main() -> None:
    score_one = int(input("Enter score 1: "))
    score_two = int(input("Enter score 2: "))
    score_three = int(input("Enter score 3: "))
    score_four= int(input("Enter score 4: "))
    score_five = int(input("Enter score 5: "))
    score_six = int(input("Enter score 6: "))
    score_seven = int(input("Enter score 7: "))
    score_eight = int(input("Enter score 8: "))
    avg = calc_average(score_one, score_two, score_three, score_four, score_five, score_six, score_seven, score_eight)
    overall_letter_grade = determine_grade(avg)
    
    

    print(f"\nScore\t\tNumeric Grade\tLetter Grade")
    print(f"----------------------------------------------------")
    print(f"score 1:\t\t{score_one:.1f}\t\t\t{determine_grade(score_one)}")
    print(f"score 2:\t\t{score_two:.1f}\t\t\t{determine_grade(score_two)}")
    print(f"score 3:\t\t{score_three:.1f}\t\t\t{determine_grade(score_three)}")
    print(f"score 4:\t\t{score_four:.1f}\t\t\t{determine_grade(score_four)}")
    print(f"score 5:\t\t{score_five:.1f}\t\t\t{determine_grade(score_five)}")
    print(f"score 6:\t\t{score_six:.1f}\t\t\t{determine_grade(score_six)}")
    print(f"score 7:\t\t{score_seven:.1f}\t\t\t{determine_grade(score_seven)}")
    print(f"score 8:\t\t{score_eight:.1f}\t\t\t{determine_grade(score_eight)}")
    print(f"----------------------------------------------------")
    print(f"Average of all the scores for the course is a {avg:.1f} %.")
    print(f"The letter grade for the course is a '{overall_letter_grade}'.")



if __name__ == "__main__":
    main()
