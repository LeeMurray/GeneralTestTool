import csv
from tkinter import simpledialog
from faker import Faker
from bin import DOBGen
from bin import Message

fake = Faker()


def create_csv_file():
    record_count = simpledialog.askinteger(title="number", prompt="Enter Number : ")
    with open('./files/Data.csv', 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name', 'DOB', 'email', 'address', 'city', 'postcode']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(record_count):
            writer.writerow(
                {
                    'first_name': fake.name(),
                    'last_name': fake.name(),
                    'DOB': DOBGen.get_date(),
                    'email': fake.email(),
                    'address': str(fake.building_number() + " " + fake.street_name()),
                    'city': fake.city(),
                    'postcode': fake.postcode(),
                }
            )

    Message.process_complete()

'''
def get_totals():
    qty_total = 0
    amount_total = 0
    with open('./files/Data.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if row[4] != 'qty':
                qty = int(row[4])
                qty_total += qty

                amount = float(row[5])
                amount_total += amount
    return qty_total, amount_total


if __name__ == '__main__':
    start = time()
    create_csv_file()
    elapsed = time() - start
    messagebox.showinfo("Info", "created csv file time: {}".format(elapsed))

    start = time()
    qty_total, amount_total = get_totals()
    elapsed = time() - start
    messagebox.showinfo("Info", "got totals time: {}".format(elapsed))

    messagebox.showinfo("Info", "qty: {}".format(elapsed))
    messagebox.showinfo("Info", "amount: {}".format(elapsed))
    '''

