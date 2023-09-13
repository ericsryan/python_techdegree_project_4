# Store Inventory Management System

This Python application is a Store Inventory Management System that allows you to view, add, and backup product data in a database. It reads product information from a CSV file and stores it in an SQLite database. You can perform various operations on the products using a command-line menu interface.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Adding Products](#adding-products)
  - [Viewing Products](#viewing-products)
  - [Backing Up the Database](#backing-up-the-database)

## Getting Started

### Prerequisites

- Python 3.x
- `models.py` (containing SQLAlchemy models) should be present in the same directory as this script.
- A CSV file named `inventory.csv` with the product data.

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/ericsryan/python_techdegree_project_4.git
   ```

2. Navigate to the project directory:

   ```bash
   cd python_techdegree_project_4
   ```
3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```
   NOTE: It is recommended that you use a virtual environment to install the packages.
## Usage

To run the Store Inventory Management System, follow these steps:

1. Open a terminal and navigate to the project directory.

2. Run the following command to start the application:

   ```bash
   python app.py
   ```

3. You will see the main menu with the following options:

   - [V]iew a product
   - [A]dd a product to the database
   - [B]ackup the database
   - [E]xit the program

### Adding Products

To add a new product to the database:

1. Select the "A" option from the main menu.

2. Enter the product name, price (e.g., $25.99), and quantity.

3. Confirm the information and choose whether to start over or return to the menu.

### Viewing Products

To view product details:

1. Select the "V" option from the main menu.

2. You will see a list of product IDs and names. Enter the ID of the product you want to view.

3. Product details, including price, quantity, and update date, will be displayed.

### Backing Up the Database

To create a backup of the database in a CSV file:

1. Select the "B" option from the main menu.

2. The database information will be exported to a file named `backup.csv` in the project directory.