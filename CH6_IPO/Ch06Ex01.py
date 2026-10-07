def main():
    try:
        with open("numbers.txt", 'r') as file_to_read:
            print(file_to_read.read())
    except FileNotFoundError:
        print("File doesn't exist.")

if __name__ == "__main__":
    main()