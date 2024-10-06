import csv

def export_to_csv(bills):

    filename = 'bill_data.csv'
    with open(filename, mode='w', newline='') as file:

        writer = csv.writer(file)
        
        # Write the header if necessary
        writer.writerow(['ID','Name', 'Amount', 'Due Date'])  # Adjust as needed
        
        # Write the data
        for row in bills:
            writer.writerow(row)