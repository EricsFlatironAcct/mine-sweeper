from helpers import Display, GameBoard, Choices

    
if __name__ == '__main__':
  

    display = Display()
    display.welcome_message()
    user_logged_in = None
    while not user_logged_in:
        user_selection = input("Please enter your username: ")
        if len(user_selection)>0: user_logged_in = user_selection
    menu_option_selected = 0
    while not menu_option_selected ==4:
        menu_option_selected = Choices.main_menu(user_logged_in)
        if menu_option_selected == 1:
            Choices.show_user_results()
        if menu_option_selected == 2:
            Choices.show_recent_results
        if menu_option_selected == 3:
            Choices.play_game()
        if menu_option_selected == 4:
            print("Goodbye!")

