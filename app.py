import csv, datetime, os

from models import Base, Product, session, engine


def add_csv():
    """Add contents of inventory.csv to a database"""
    with open('inventory.csv', newline='') as csv_file:
        data = csv.reader(csv_file)
        next(data, None) # Skip the headers
        for row in data:
            product_name = clean_name(row[0])
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


# Cleaning functions
def clean_name(name):
    """Strip quotation marks from string"""
    return name.strip('"')


def clean_price(price):
    """Strip dollar sign from price and convert to integer"""
    try:
        price_float = float(price.strip('$'))
        price = int(price_float * 100)
    except ValueError:
        input("""
***** PRICE ERROR *****
The price should only include numbers 1-10 and the '.' symbol.
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
***** PRICE ERROR *****
The price should only include numbers 1-10 and the '.' symbol.
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



def app():
    """Application logic"""
    print("App")


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    if session.query(Product).count() == 0: # Add products to database if empty
        add_csv()
    app()

    