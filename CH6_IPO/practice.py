def main():
    # with open("scores.txt", "w") as score_file:
    #     score_file.write("95\n")
    #     score_file.write("88\n")
    #     score_file.write("91\n")
    # print("Score were written to scores.txt")

    # with open("animals.txt", "w") as animal_file:
    #     animal_file.write("Dog\n")
    # print("Wrote 'Dog' to the file")

    # with open("animals.txt", "a") as animal_file:
    #     animal_file.write("Cat\n")
    # print("Wrote 'Cat' to the file")

    # with open("animals.txt", "r") as animal_file:
    #     contents = animal_file.read()
    
    # print("Animals on our farm: ")
    # print(contents)

    # with open("animals.txt", "r") as farmlist:
    #     # contents = farmlist.read() # this reads EVERYTHING

    #     # one line at a time
    #     print(farmlist.readline())
    #     input("press enter to continue")
    #     print(farmlist.readline())
    #     input("press enter to continue")
    #     print(farmlist.readline())
    #     input("press enter to continue")
    #     print(farmlist.readline())

    # with open("animals.txt", "r") as farmlist:
    #     for animal in farmlist:
    #         print(animal)

    # TRY and EXCEPT

    
    user_input_hours = input("How many hours did you work? ")
    try:
        with open("payrate.txt", "r") as pay_rate_file:
            pay_rate = float(pay_rate_file.readline())

        hours = float(user_input_hours)
        print(f"You made: {pay_rate * hours}")

    except FileNotFoundError:
        print("file doesn't exist")
    except ValueError:
        print("must enter a number")
        

if __name__ == "__main__":
    main()