from Database_for_main.main_controls import code
while True:
    user_input = code.display_menu()
    if user_input == 1:
        word = input("Write a word:")
        times = int(input("How many times:"))
        code.practice_a_word(word, times)
    elif user_input == 2:
        code.practice_a_word_saved()
    elif user_input == 3:
        code.exit()
    else:
        print("Try again")