USE zomato;


-- 1. Total Revenue

SELECT
    SUM(price * quantity) AS total_revenue
FROM order_items;


-- 2. Revenue by Item

SELECT
    i.item_name,
    SUM(oi.price * oi.quantity) AS total_revenue
FROM order_items oi
JOIN items i
    ON oi.item_id = i.item_id
GROUP BY i.item_name
ORDER BY total_revenue DESC;


-- 3. Revenue by Category

SELECT
    c.category_name,
    SUM(oi.price * oi.quantity) AS total_revenue
FROM order_items oi
JOIN items i
    ON oi.item_id = i.item_id
JOIN categories c
    ON i.category_id = c.category_id
GROUP BY c.category_name
ORDER BY total_revenue DESC;


-- 4. Revenue by Payment Method

SELECT
    payment_method,
    SUM(amount) AS total_revenue
FROM payments
GROUP BY payment_method
ORDER BY total_revenue DESC;


-- 5. Total Orders

SELECT
    COUNT(*) AS total_orders
FROM orders;


-- 6. Orders by Payment Status

SELECT
    payment_status,
    COUNT(*) AS total_orders
FROM payments
GROUP BY payment_status;


-- 7. Most Ordered Items

SELECT
    i.item_name,
    SUM(oi.quantity) AS total_quantity_ordered
FROM order_items oi
JOIN items i
    ON oi.item_id = i.item_id
GROUP BY i.item_name
ORDER BY total_quantity_ordered DESC;


-- 8. Revenue by Customer

SELECT
    c.first_name,
    c.last_name,
    c.phone_number,
    c.email,
    SUM(oi.price * oi.quantity) AS total_revenue
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id
JOIN customers c
    ON o.user_id = c.user_id
GROUP BY c.user_id
ORDER BY total_revenue DESC;


-- 9. Total Orders and Revenue by Customer

SELECT
    c.first_name,
    c.last_name,
    c.phone_number,
    c.email,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(oi.price * oi.quantity) AS total_revenue
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id
JOIN customers c
    ON o.user_id = c.user_id
GROUP BY c.user_id
ORDER BY total_revenue DESC;


-- 10. Customer Details with Orders

SELECT
    c.first_name,
    c.last_name,
    c.phone_number,
    c.email,
    o.order_id,
    o.delivery_address,
    oi.item_id,
    oi.quantity
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id
JOIN customers c
    ON o.user_id = c.user_id;


-- 11. Items Ordered by Category

SELECT
    c.category_name,
    i.item_name,
    SUM(oi.quantity) AS total_quantity_ordered
FROM order_items oi
JOIN items i
    ON oi.item_id = i.item_id
JOIN categories c
    ON i.category_id = c.category_id
GROUP BY c.category_name, i.item_name
ORDER BY total_quantity_ordered DESC;


-- 12. Revenue by Date

SELECT
    DATE(paid_at) AS date,
    SUM(amount) AS daily_revenue
FROM payments
GROUP BY DATE(paid_at)
ORDER BY date;


-- 13. Items Purchased in a Specific Order

SELECT
    oi.order_id,
    i.item_name,
    oi.quantity,
    oi.price
FROM order_items oi
JOIN items i
    ON oi.item_id = i.item_id
WHERE oi.order_id = 1;


-- 14. Customers with No Orders

SELECT
    c.user_id,
    c.first_name,
    c.last_name,
    c.email
FROM customers c
LEFT JOIN orders o
    ON c.user_id = o.user_id
WHERE o.order_id IS NULL;