import screens as sc
from db import DB_Connection
import sys
import csv_lib as clib

def main():

    # keep_using variable is assigned true while the user is using the program,
    # and set to False which exits the main program loop when the user is done.
    keep_using = True

    # max_option_choice is assigned the total number of options on the home menu. 
    max_option_choice = 4

    db_obj = DB_Connection()

    # Program loop
    while(keep_using):

        # Display Home Screen
        sc.display_home_screen()
        screen_choice = input('Please enter the screen number you wish to see:\n')
        
        # Check if exit command q is entered
        if (screen_choice == 'q'):
            print()
            exit()

        # Input validation
        while (not screen_choice.isdigit()) or (int(screen_choice) < 0 or int(screen_choice) > max_option_choice):
            sc.display_home_screen()
            print('===================================================')
            print(f'Error: Selection must be a number between 1 and {max_option_choice}')
            print('===================================================\n')
            screen_choice = input('Please enter the screen number you wish to see:\n')
            if (screen_choice == 'q'):
                print()
                exit()

        # Determine selected home screen option
        if screen_choice == '1':

            # View Bill Totals
            bills = db_obj.retreive_all_bills()
            bill_total = 0
            for bill in bills:
                bill_total += bill[2]
            sc.view_bill_totals(bills)
            print('======================================================')
            print('Bill Total: ${:.2f}'.format(bill_total))
        elif screen_choice == '2':
            add_more = True
            while add_more:
                bill_info = sc.add_a_bill()
                db_obj.add_bill(bill_info)
                print('\nBill has been added!\n')
                if not input('Would you like to add another bill (y/n)? ') == 'y':
                    add_more = False
        elif screen_choice == '3':
            
            bills = db_obj.retreive_all_bills()

            # Display delete bill screen and retrieve bill number
            sc.delete_a_bill_screen(bills)

            # Get bill id
            bill_id = sc.get_selected_bill_id(bills)

            if bill_id != -1:
                # Confirm bill deletion
                deletion_confirmed = input('Are you sure you want to delete this bill (y/n)?: ')

                if str.lower(deletion_confirmed) == 'y':
                    db_obj.delete_bill(bill_id)
                else:
                    print('Bill deletion canceled!')
        elif screen_choice == '4':
            bills = db_obj.retreive_all_bills()
            clib.export_to_csv(bills)

        print()
        keep_using = input('Return to home screen (y/n)?: ')

        if str.lower(keep_using) == 'n' or str.lower(keep_using) == 'q':
            keep_using = False

    # Print newline at the end of the program
    print()

if __name__ == '__main__':
    main()