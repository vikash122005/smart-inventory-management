--- 1. Total number of products

SELECT COUNT(*) AS total_products
FROM products;

--- 2. Total number of sales

SELECT COUNT(*) AS total_sales
FROM sales;

--- 3. Total quantity sold

SELECT SUM(quantity_sold) AS total_quantity_sold
FROM sales;


--- 4. Current stock by product

SELECT
    p.product_id,
    p.product_name,
    i.current_stock
FROM products p
JOIN inventory i
    ON p.product_id = i.product_id
ORDER BY i.current_stock DESC;

--- 5. Find low-stock products

SELECT
    p.product_id,
    p.product_name,
    i.current_stock,
    p.reorder_level
FROM products p
JOIN inventory i
    ON p.product_id = i.product_id
WHERE i.current_stock <= p.reorder_level;

--- 6. Calculate stock status

SELECT
    p.product_id,
    p.product_name,
    i.current_stock,
    p.reorder_level,
    CASE
        WHEN i.current_stock <= p.reorder_level THEN 'LOW STOCK'
        ELSE 'OK'
    END AS stock_status
FROM products p
JOIN inventory i
    ON p.product_id = i.product_id;


--- 7. Quantity sold per product

SELECT
    p.product_id,
    p.product_name,
    SUM(s.quantity_sold) AS total_quantity_sold
FROM products p
JOIN sales s
    ON p.product_id = s.product_id
GROUP BY
    p.product_id,
    p.product_name
ORDER BY total_quantity_sold DESC;


--- 8. Best-selling products

SELECT
    p.product_id,
    p.product_name,
    SUM(s.quantity_sold) AS total_quantity_sold
FROM products p
JOIN sales s
    ON p.product_id = s.product_id
GROUP BY
    p.product_id,
    p.product_name
ORDER BY total_quantity_sold DESC
LIMIT 5;


--- 9. Sales by category

SELECT
    p.product_category,
    SUM(s.quantity_sold) AS total_quantity_sold
FROM products p
JOIN sales s
    ON p.product_id = s.product_id
GROUP BY p.product_category
ORDER BY total_quantity_sold DESC;


--- 10. Products that need restocking

SELECT
    p.product_id,
    p.product_name,
    i.current_stock,
    p.reorder_level,
    p.lead_time_days
FROM products p
JOIN inventory i
    ON p.product_id = i.product_id
WHERE i.current_stock <= p.reorder_level
ORDER BY i.current_stock ASC;


--- 11. High-stock but low-selling products

SELECT
    p.product_id,
    p.product_name,
    i.current_stock,
    COALESCE(SUM(s.quantity_sold), 0) AS total_quantity_sold
FROM products p
JOIN inventory i
    ON p.product_id = i.product_id
LEFT JOIN sales s
    ON p.product_id = s.product_id
GROUP BY
    p.product_id,
    p.product_name,
    i.current_stock
ORDER BY
    i.current_stock DESC,
    total_quantity_sold ASC;


--- 12. Revenue per product

SELECT
    p.product_id,
    p.product_name,
    SUM(s.quantity_sold) AS quantity_sold,
    SUM(s.quantity_sold * p.unit_price) AS total_revenue
FROM products p
JOIN sales s
    ON p.product_id = s.product_id
GROUP BY
    p.product_id,
    p.product_name
ORDER BY total_revenue DESC;


--- 13. Revenue by category

SELECT
    p.product_category,
    SUM(s.quantity_sold * p.unit_price) AS total_revenue
FROM products p
JOIN sales s
    ON p.product_id = s.product_id
GROUP BY p.product_category
ORDER BY total_revenue DESC;


--- 14. Overall inventory value

SELECT
    SUM(i.current_stock * p.unit_price) AS total_inventory_value
FROM products p
JOIN inventory i
    ON p.product_id = i.product_id;


---15. Low stock alert

SELECT
    p.product_id,
    p.product_name,
    p.product_category,
    i.current_stock,
    p.reorder_level,
    p.lead_time_days,
    CASE
        WHEN i.current_stock <= p.reorder_level
            THEN 'LOW STOCK'
        WHEN i.current_stock <= p.reorder_level * 1.5
            THEN 'REORDER SOON'
        ELSE 'OK'
    END AS stock_status
FROM products p
JOIN inventory i
    ON p.product_id = i.product_id
ORDER BY i.current_stock ASC;

---16. Products requiring attention

-- Products requiring attention
SELECT
    p.product_id,
    p.product_name,
    p.product_category,
    i.current_stock,
    p.reorder_level,
    p.lead_time_days,
    CASE
        WHEN i.current_stock <= p.reorder_level
            THEN 'LOW STOCK'
        ELSE 'REORDER SOON'
    END AS stock_status
FROM products p
JOIN inventory i
    ON p.product_id = i.product_id
WHERE i.current_stock <= p.reorder_level * 1.5
ORDER BY i.current_stock ASC;