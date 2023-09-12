import csv, datetime, os

from models import Base, Product, session, engine


def add_csv():
    with open('inventory.csv', newline='') as csv_file:
        data = csv.reader(csv_file)
        next(data, None) # Skip the headers
        for row in data:
            product_in_db = session.query(
                Product
            ).filter(
                Product.product_name==row[0]
            ).one_or_none()

            if product_in_db == None:
                product_name = row[0]
                product_quantity = row[1]
                product_price = row[2]
                date_updated = row[3]
                new_product = Product(
                    product_name=product_name,
                    product_quantity=product_quantity,
                    product_price=product_price,
                    date_updated=date_updated
                )
                session.add(new_product)
        session.commit()


def app():
    print("App")


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    if not session.query(Product).one_or_none():
        print("Setting up the database...")
        add_csv()
        products = session.query(Product)
        for product in products:
            print(product.product_name)
    app()

    