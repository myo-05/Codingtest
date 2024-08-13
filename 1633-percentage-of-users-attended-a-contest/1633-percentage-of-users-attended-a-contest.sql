/*
Write a solution to find the percentage of the users registered in each contest rounded to two decimals.
Return the result table ordered by percentage in descending order. In case of a tie, order it by contest_id in ascending order.
*/
# Write your MySQL query statement below

select contest_id , round(count(user_id)/total*100,2) as percentage
from Register r cross join (select count(*) as total from Users) u
group by contest_id
order by percentage desc , contest_id