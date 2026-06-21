import time as t
class main:
    def display_menu(self):
        print("----------------Typing-Practice-------------------")
        print("---------------1.Practice a word------------------")
        print("----2.Practice a word saved(still developing)-----")
        print("-------------------3.Exit-------------------------")
        menu_choice =  input("Choose ethier 1 nor 2 nor 3:")
        return menu_choice
    def practice_a_word(self, word, times):
        times = times+1
        for i in range(1, times):
            a = input(f"Enter {word}: ")
            while a==word:
                print("Succesfull")
                a = input(f"Enter {word}: ")
            else:
                print(f"You entered wrong word:{a}")
                print("Retrying")
                t.sleep(5)
                a = input(f"Enter {word}: ")
        print("Completed")
    def practice_a_word_saved(self):
        print("Still not implemented")
    
