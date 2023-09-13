import csv, datetime, os, time

from models import Base, Product, session, engine


def add_csv():
    """Add contents of inventory.csv to a database"""
    with open('inventory.csv', newline='') as csv_file:
        data = csv.reader(csv_file)
        next(data, None) # Skip the headers
        for row in data:
            product_name = row[0]
            product_price = clean_price(row[1])
            product_quantity = clean_quantity(row[2])
            date_updated = clean_date(row[3])
            new_product = Product(
                product_name=product_name,
                product_quantity=product_quantity,
                product_price=product_price,
                date_updated=date_updated
            )
            session.add(new_product)
        session.commit()


def clear_screen():
    """Clear the screen for better readablity"""
    os.system('cls' if os.name == 'nt' else 'clear')


### Cleaning functions ###
def clean_price(price):
    """Strip dollar sign from price and convert to integer"""
    try:
        price_float = float(price.strip('$'))
        price = int(price_float * 100)
    except ValueError:
        input("""
***** PRICE ERROR *****
The price should only include number characters and the '.' symbol.
Press [Enter] to continue...
""")
    else:
        return price
    

def clean_quantity(quantity):
    """Convert quantity into an integer"""
    try:
        quantity = int(quantity)
    except ValueError:
        input("""
***** QUANTITY ERROR *****
The quantity should only include number characters.
Press [Enter] to continue...
""")
    else:
        return quantity
    

def clean_date(date):
    """Convert date string into a date object"""
    try:
        date = datetime.datetime.strptime(date, '%m/%d/%Y')
    except ValueError:
        input("""
***** DATE ERROR *****
The date should be formatted MM/DD/YYYY.
Press [Enter] to continue...
""")
    else:
        return date
    

def main_menu():
    """Display program options"""
    clear_screen()
    while True:
        print("""

    ***** Store Inventory *****

    [V]iew a product
    [A]dd a product to the database
    [B]ackup the database
              
    [E]xit the program
              
""")
        choice = input("    >>> ")
        if choice.lower() == 'v':
            view_product_menu()
        elif choice.lower() == 'a':
            add_product()
        elif choice.lower() == 'b':
            backup_database()
        elif choice.lower() == 'e':
            clear_screen()
            print("The program session has ended.\n")
            break
        else:
            clear_screen()
            print("That was an invalid entry. Please select a menu option.")



def view_product_menu():
    """Allow user to select a product and view its details"""
    clear_screen()
    while True:
        print("""
    ***** View a product *****
              
    ID#  | Product name
""")
        id_options = []
        for product in session.query(Product):
            id_options.append(str(product.product_id))
            print("    " + str(product.product_id) + (' ' * (7 - len(str(product.product_id)))) + product.product_name)
        print("\n    Enter an id number to view product details or enter 'm' to return to the main menu.")
        print("    You may need to scroll up to see all options.\n")
        choice = input("    >>> ")
        if choice.lower() == 'm':
            clear_screen()
            break
        elif choice in id_options:
            view_product(int(choice))
        else:
            print("\n    That is not a valid selection, please try again...")
            time.sleep(3)
            clear_screen()


def view_product(product_id):
    """View the details of a product"""
    clear_screen()
    product = session.query(Product).filter(Product.product_id==product_id).first()
    print(f"""
    {product.product_name}

    Price: ${product.product_price / 100}
    In stock: {product.product_quantity}
    Updated: {product.date_updated}

""")
    input("    Press [Enter] to return to the selection menu...")


def add_product():
    """Add product to database"""
    inputting_data = True
    while inputting_data:
        clear_screen()
        print("    Add a product to the inventory:\n")
        product_name = input("    Product name: ")
        price_needed = True
        while price_needed:
            product_price = input("    Price (Ex: $25.99): $")
            product_price = clean_price(product_price)
            if type(product_price) == int:
                price_needed = False
        quantity_needed = True
        while quantity_needed:
            product_quantity = input("    Quantity: ")
            product_quantity = clean_quantity(product_quantity)
            if type(product_quantity) == int:
                quantity_needed = False
        choice = input("Is all the information correct? Y/n: ")
        if choice.lower() == 'n':
            choice = input("Would you like to [s]tart over or return to the [m]enu? S/m: ")
            if choice.lower() == 'm':
                clear_screen()
                return None
            else:
                continue
        else:
            session.add(Product(product_name=product_name, product_price=product_price, product_quantity=product_quantity, date_updated=datetime.date.today()))
            session.commit()
            clear_screen()
            print("    The product has been added to the database")
            break
        


def backup_database():
    """Backup the database to a new .csv file"""
    with open('backup.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["product_name", "product_price", "product_quantity", "date_updated"])
        for product in session.query(Product):
            writer.writerow([product.product_name, f"${product.product_price/100}", product.product_quantity, product.date_updated.strftime("%m/%d/%Y")])
    clear_screen()
    print("    The database has been backed up to a .csv file")



def app():
    """Application logic"""
    main_menu()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    if session.query(Product).count() == 0: # Add products to database if empty
        add_csv()
    app()

    