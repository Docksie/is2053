def main():
    total = 0
    with open("numbers.txt", 'r') as file_to_read:
        for number in file_to_read:
            total += int(number)
    print(f"The total of all the numbers in the file is {total:,.1f}")
    


if __name__ == "__main__":
    main()