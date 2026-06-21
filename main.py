from Database_for_main.main_controls import code
while True:
    user_input = code.display_menu()
    if user_input == 1:
        words = input("Write a word:")
        timess = int(input("How many times:"))
        code.practice_a_word(words, timess)
        break
    elif user_input == 2:
        code.practice_a_word_saved()
        break
    elif user_input == 3:
        code.exit()
        break
    else:
        print("Try again")