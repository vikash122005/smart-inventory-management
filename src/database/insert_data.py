
def insert_products(connection,products):
    cursor = connection.cursor()

    query = """INSERT INTO products
    (product_id,product_name,product_category,unit_price,reorder_level,lead_time_days)
    VALUES (%s, %s, %s, %s, %s, %s)"""

    for _,row in products.iterrows():
        cursor.execute(
            query,
            (
                row["product_id"],
                row["product_name"],
                row["product_category"],
                row["unit_price"],
                row["reorder_level"],
                row["lead_time_days"]
            )
        )
    connection.commit()
    cursor.close()


def insert_sales(connection,sales):
    cursor = connection.cursor()

    query = """INSERT INTO sales
    (sale_id,product_id,sale_date,quantity_sold)
    VALUES (%s, %s, %s, %s)"""

    for _,row in sales.iterrows():
        cursor.execute(
            query,
            (
                row["sale_id"],
                row["product_id"],
                row["sale_date"],
                row["quantity_sold"]
            )
        )
    connection.commit()
    cursor.close()

def insert_inventory(connection,inventory):
    cursor = connection.cursor()

    query = """INSERT INTO inventory
    (product_id,current_stock)
    VALUES (%s, %s)"""

    for _,row in inventory.iterrows():
        cursor.execute(
            query,
            (
                row["product_id"],
                row["current_stock"]
            )
        )
    connection.commit()
    cursor.close()

def record_sale(connection, sale_id, product_id, sale_date, quantity_sold):

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT 1
        FROM sales
        WHERE sale_id = %s
        """,
        (sale_id,)
    )
    
    if cursor.fetchone() is not None:
        cursor.close()
        raise ValueError("Sale ID already exists. Please enter a different Sale ID.")

    # Check current stock
    cursor.execute(
        """
        SELECT current_stock
        FROM inventory
        WHERE product_id = %s
        """,
        (product_id,)
    )

    result = cursor.fetchone()

    if result is None:
        cursor.close()
        raise ValueError("Product does not exist in inventory")

    current_stock = result[0]

    if quantity_sold <= 0:
        cursor.close()
        raise ValueError("Quantity sold must be greater than 0")

    if quantity_sold > current_stock:
        cursor.close()
        raise ValueError("Not enough stock available")


    # Insert sale
    cursor.execute(
        """
        INSERT INTO sales
        (sale_id, product_id, sale_date, quantity_sold)
        VALUES (%s, %s, %s, %s)
        """,
        (sale_id, product_id, sale_date, quantity_sold)
    )

    # Reduce inventory
    cursor.execute(
        """
        UPDATE inventory
        SET current_stock = current_stock - %s
        WHERE product_id = %s
        """,
        (quantity_sold, product_id)
    )

    connection.commit()
    cursor.close()