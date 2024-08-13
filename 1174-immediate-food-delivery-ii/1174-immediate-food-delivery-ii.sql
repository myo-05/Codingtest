/*
If the customer's preferred delivery date is the same as the order date, 
    then the order is called immediate; otherwise, it is called scheduled.
The first order of a customer is the order with the earliest order date that the customer made.
    It is guaranteed that a customer has precisely one first order.
Write a solution to find the percentage of immediate orders in the first orders of all customers, rounded to 2 decimal places.
*/
# Write your MySQL query statement below
with immediate as (
    select customer_id, order_date, 'immediate' as called
    from Delivery
    where order_date=customer_pref_delivery_date
), first_order as(
    select customer_id, min(order_date) as order_date
    from Delivery
    group by customer_id
)
select round(count(case when called = 'immediate' then 1 end)/count(*)*100,2) as immediate_percentage 
from first_order left join immediate using(order_date,customer_id)