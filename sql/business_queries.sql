-- Monthly Revenue Trend
SELECT
  DATE_TRUNC('month', order_date) AS month,
  SUM(revenue) AS total_revenue
FROM sales
GROUP BY 1
ORDER BY 1;

-- Customer Order Frequency
SELECT
  customer_id,
  COUNT(order_id) AS total_orders
FROM orders
GROUP BY customer_id
ORDER BY total_orders DESC;
