def display_score_table(score_table: list[list[int]]):
    for student in score_table:
        for score in student:
            print(f"{score:4}", end="")
        print()

def calc_student_avg(score_table: list[list[int]]) -> list[float]:
    averages = []
    for student_scores in score_table:
        average = sum(student_scores) / len(student_scores)
        averages.append(average)
    return averages
def main():
    score_table = [
        [70, 45, 100],
        [97, 92, 102],
        [80, 75, 92]
    ]
    display_score_table(score_table)
    print(calc_student_avg(score_table))

if __name__ == "__main__":
    main()