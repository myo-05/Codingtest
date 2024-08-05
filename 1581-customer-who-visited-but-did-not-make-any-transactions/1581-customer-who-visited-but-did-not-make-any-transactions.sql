/*
Write a solution to find the IDs of the users who visited without making any transactions
    and the number of times they made these types of visits.
Return the result table sorted in any order.
*/
# Write your MySQL query statement below

select customer_id , count(visit_id) as count_no_trans
from Visits left join Transactions using(visit_id)
where transaction_id is null
group by customer_id