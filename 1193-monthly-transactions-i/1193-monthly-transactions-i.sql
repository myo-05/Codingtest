/*
Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.
Return the result table in any order.
*/
# Write your MySQL query statement below
select date_format(trans_date,'%Y-%m') as month ,country ,count(*) as trans_count ,count(case when state='approved'then 1 end) as approved_count ,sum(amount) as trans_total_amount, sum(if(state='approved',amount,0)) as approved_total_amount 
from Transactions
group by month,country