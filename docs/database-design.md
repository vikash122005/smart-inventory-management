For the V1 smart inventory managemt the Data base mainly contains 3 Tables

1) Products
    product_id (Primary key and foreign key on Sales and Inventory table)
    product_name (Name of each products)
    product_category (Category of the product Ex: Electronics,House hold,Snacks and Beverages etc..)
    unit_price (Price/Cost per unit)
    reorder_level (minimum stock level)
    lead_time_days (This will give estimated days for delivery of products)

2) Sales
    sale_id (Primary key in sales table)
    product_id (Primary key and foreign key on Products and Inventory table)
    sale_date (sold date of each product with time stamp)
    quantity_sold (Quantity of each product that has been sold)

3) Inventory
    product_id (Primary key and foreign key on Sales and Products table)
    current_stock  (available stock as of now)

