import screens as sc
from db import DB_Connection
import sys
import csv_lib as clib

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
            bill_total = 0
            for bill in bills:
                bill_total += bill[2]
            sc.view_bill_totals(bills)
            print('======================================================')
            print('Bill Total: ${:.2f}'.format(bill_total))
        elif screen_choice == '2':
            bill_info = sc.add_a_bill()
            db_obj.add_bill(bill_info)
            print('\nBill has been added!')
            input()    
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
        elif screen_choice == 'q':
            break

        print()
        keep_using = input('Return to home screen (y/n)?: ')

        if str.lower(keep_using) == 'n' or str.lower(keep_using) == 'q':
            keep_using = False

    # Print newline at the end of the program
    print()

if __name__ == '__main__':
    main()