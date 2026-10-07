def main():
    total = 0
    count = 0
    with open("numbers.txt", 'r') as file_to_read:
        for number in file_to_read:
            count += 1
            total += int(number)
    avg = total / count
    print(f"The average of all the numbers in the file is {avg:,.1f}")
    


if __name__ == "__main__":
    main()