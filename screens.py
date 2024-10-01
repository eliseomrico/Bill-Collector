import os

def display_home_screen():
    os.system('clear')
    print()
    print('\t\t\tBill Collector\t\t\t')
    print()
    print('(1) - View Bill Totals')
    print('(2) - Add a bill')
    print('(3) - Delete a bill')
    print()
    return input('Please enter the screen number you wish to see:\n')

def view_bill_totals(bills):
    os.system('clear')
    print('{:17s}{}'.format('','View Bill Totals'))
    print()
    # Header Line
    print('   {:12s}{:5s} {:12s}{:5s}  {}'.format('NAME','|','AMOUNT','|','DUE DATE'))
    print('======================================================')

    # Example Items
    for bill in bills:
        print('{:15s}{:5s}${:12s}{:5s}{}'.format(str(bill[1]),'|',str(bill[2]),'|',str(bill[3])))

def add_a_bill():
    os.system('clear')
    print('{:19s}{}'.format('','Add A Bill'))
    print()
    bill_name = input('Name: ')
    bill_amount = input('Amount: ')
    bill_due_date = input('Due Date: ')
    return (bill_name,bill_amount,bill_due_date)

def delete_a_bill(bills):
    os.system('clear')
    id = 1
    print('{:19s}{}'.format('','Delete A Bill'))
    print()
    # Header Line
    print('   {:12s}{:5s} {:12s}{:5s}  {}'.format('ID #','|','AMOUNT','|','DUE DATE'))
    print('======================================================')

        # Example Items
    for bill in bills:
        print('{:5s}{:10s}{:5s}${:12s}{:5s}{}'.format('',str(id),'|',str(bill[2]),'|',str(bill[3])))
        id += 1

    print()

    # Get bill number to delete
    bill_number = input('Enter the bill number you want to delete: ')


    # Confirm bill exists

    # If bill does not exist request bill number again

    # If it does return bill number