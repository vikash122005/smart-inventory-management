V1 Database — Column Purpose

For V1, the database mainly contains 3 tables:

1. Products
Column	                Why we need it
product_id (PK)	     -  Unique identifier for each product. Used to connect Products with Sales and Inventory.
product_name	     -  Stores the name of the product.
product_category	 -  Groups products into categories such as Electronics, Household, Snacks, etc. Useful for category-level analysis.
unit_price	         -  Stores the selling price/cost of one unit. Useful for calculating sales value/revenue.
reorder_level	     -  Defines the minimum stock level at which the product should be considered for reordering.
lead_time_days	     -  Estimated number of days the supplier takes to deliver the product after ordering. Useful for reorder planning.
2. Sales
Column	                Why we need it
sale_id (PK)	     -  Unique identifier for each sale transaction.
product_id (FK)	     -  Identifies which product was sold. Can appear multiple times because the same product can be sold in many transactions.
sale_date	         -  Records when the sale happened. A timestamp allows analysis by date/time.
quantity_sold	     -  Records how many units were sold in that transaction.
3. Inventory
Column	                Why we need it
product_id (PK, FK)	 -  Identifies the product whose current stock is being tracked. One inventory record per product in V1.
current_stock	     -  Stores the number of units currently available. Used to determine whether stock needs replenishment.
