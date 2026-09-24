
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