/*
Write a solution to report the product_name, year, and price for each sale_id in the Sales table.
Return the resulting table in any order.
*/
# Write your MySQL query statement below

select product_name , year, price
from Sales join Product using(product_id)