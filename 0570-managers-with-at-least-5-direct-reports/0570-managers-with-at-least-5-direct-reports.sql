/*
Write a solution to find managers with at least five direct reports.

Return the result table in any order.
*/
# Write your MySQL query statement below
with target_manager as (
    select managerId
    from Employee
    group by managerId
    having count(id) >= 5
)
select name
from Employee
where id in (select managerId from target_manager)