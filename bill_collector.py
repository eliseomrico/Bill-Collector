import screens as sc
from db import DB_Connection
import sys

def main():

    keep_using = True
    db_obj = DB_Connection()

    # Program loop
    while(keep_using):

        # Display Home Screen
        screen_choice = sc.display_home_screen()

        if screen_choice == '1':
            # View Bill Totals
            bills = db_obj.retreive_all_bills()
            sc.view_bill_totals(bills)
        elif screen_choice == '2':
            bill_info = sc.add_a_bill()
            db_obj.add_bill(bill_info)
            print('\nBill has been added!')
            input()    
        elif screen_choice == '3':
            
            bills = db_obj.retreive_all_bills()
            sc.delete_a_bill(bills)
            # Confirm bill deletion

            # Delete bill

            # Notify bill was deleted
        elif screen_choice == 'q':
            keep_using = False

        print()
        keep_using = input('Return to home screen (y/n)?: ')

        if keep_using == 'n':
            keep_using = False

    # Print newline at the end of the program
    print()

if __name__ == '__main__':
    main()