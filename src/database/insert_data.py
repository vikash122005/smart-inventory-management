
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