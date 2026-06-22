import time as t
class main:
    def display_menu(self):
        print("----------------Typing-Practice-------------------")
        print("---------------1.Practice a word------------------")
        print("----2.Practice a word saved(still developing)-----")
        print("-------------------3.Exit-------------------------")
        menu_choice =  int(input("Choose ethier 1 nor 2 nor 3:"))
        return menu_choice
    def practice_a_word(self, word, times):
        count = 1
        for i in range(times):
            while True:
                a = input(f"Enter {word}: ")
                if word == a:
                    if count == times:
                        print("Your have completed the practice section")
                        exit()
                    else:
                        count += 1
                        print("Succesfull")
                else:
                    pass
                    
                
        print("Completed")
    def practice_a_word_saved(self):
        print("--------------Still not implemented--------------")
        print("---------------Bye-bye---------------------------")
        exit()
    def exit(self):
        print("---------Thank you for using this program!-------")
        print("------------------Bye Bye------------------------")
        exit()

code = main()