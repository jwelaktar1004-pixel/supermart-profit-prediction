-- Basic validation
-- Why:
-- Confirms one row = one order.
select * from grocery_sales
SELECT COUNT(*) FROM grocery_sales;
SELECT COUNT(DISTINCT Order_ID) FROM grocery_sales;

-- Business aggregations
-- Why:
-- Confirms which features may influence the target variable.
SELECT Category,
       SUM(Sales) AS total_sales,
       SUM(Profit) AS total_profit
FROM grocery_sales
GROUP BY Category;

SELECT Region,
       AVG(Discount) AS avg_discount,
       SUM(Profit) AS total_profit
FROM grocery_sales
GROUP BY Region;

-- Discount vs profit logic
-- Why:
-- Builds business intuition before ML.

SELECT
  CASE
    WHEN Discount < 0.15 THEN 'Low'
    WHEN Discount < 0.30 THEN 'Medium'
    ELSE 'High'
  END AS discount_bucket,
  AVG(Profit) AS avg_profit
FROM grocery_sales
GROUP BY discount_bucket;

