# main.py

from transaction import Transaction
import menu

def main():
    """
    Main function to run the transaction application.
    It creates a Transaction object and displays a menu for user interaction.
    """
    # Create a Transaction object
    trnsct_123 = Transaction()

    # Infinite loop to keep the application running until the user chooses to exit
    while True:
        # Display the menu options to the user
        menu.display_menu()

        # Get the user's choice
        choice = input("Select an option: ")

        # Handle the user's choice and break the loop if the user chooses to exit
        if not menu.handle_choice(choice, trnsct_123):
            break

if __name__ == "__main__":
    # Entry point of the script
    main()
