secret_massage = input().split()


for word in secret_massage:
    number = ''
    for characters in word:
        if characters.isdigit():
            number += characters
    first_letter = chr(int(number))
    current_word = first_letter + word[len(number):]
    current_word = list(current_word)
    current_word[1], current_word[-1] = current_word[-1], current_word[1]
    print(f"{''.join(current_word)} ", end="")
