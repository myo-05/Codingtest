/*
Write a solution to report the name and bonus amount of each employee with a bonus less than 1000.

Return the result table in any order.
*/
# Write your MySQL query statement below
select name , bonus
from Employee left join Bonus using(empId)
where coalesce(bonus,0) < 1000