/*
Write a solution to find the average selling price for each product. 
    average_price should be rounded to 2 decimal places.
Return the result table in any order.
*/
# Write your MySQL query statement below
select p.product_id , coalesce(round(sum(price*units)/sum(units),2),0) as average_price 
from Prices p left join UnitsSold u on p.product_id=u.product_id
and purchase_date between start_date and end_date
group by p.product_id