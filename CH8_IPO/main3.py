def display_tokens(my_str:str, delimiter:str):
    tokens = my_str.split(delimiter)
    print('=' * 30)
    for _ in range(len(tokens)):
        print(f"Token #{_}: {tokens[_]}")



def main():
    sentence = "one two three four"
    print(f"My tokens are:")
    display_tokens(sentence, " ")

    csv_text = "dan,schumacher,30,PhD Information Technology, True"
    display_tokens(csv_text, ',')

    dates = "11/26/26"
    display_tokens(dates, '/')


if __name__ == "__main__":
    main()