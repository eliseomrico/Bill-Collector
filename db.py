import mysql.connector as msc
from decimal import Decimal

class DB_Connection:

    def __init__(self):
        # Establish the connection
        self.conn = msc.connect(
            host="localhost",      # Replace with your MySQL server host
            user="root",           # Replace with your MySQL username
            password="",           # Replace with your MySQL password
            database="bills_db"    # Replace with your MySQL database name
        )

        # Check if the connection was successful
        if self.conn.is_connected():
            print("Connected to MySQL database")

        # Create a cursor object to interact with the database
        self.cursor = self.conn.cursor()

    def add_bill(self,bill_info):

        query = "INSERT INTO bills (bill_name, bill_amount, bill_due_date) VALUES (%s, %s, %s)"

        # Example query: retrieving data
        self.cursor.execute(query,bill_info)
        #result = self.cursor.fetchall()

        self.conn.commit()
        self.retreive_all_bills()

    def retreive_all_bills(self):
        # Example query: retrieving data
        self.cursor.execute("SELECT * FROM bills")
        result = self.cursor.fetchall()
        return result

    def close_db_connection(self):
        # Close the connection when done
        self.cursor.close()
        self.conn.close()

    def delete_bill(self, bill_id):
        query = "DELETE FROM bills WHERE id = %s"
        try:
            self.cursor.execute(query, (bill_id,))  # Use a tuple for a single parameter
            self.conn.commit()
            print('Bill has been deleted successfully')
        except:
            print('Something went wrong bill not deleted.')