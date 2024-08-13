/*
Write an SQL query that reports the average experience years of all the employees for each project, rounded to 2 digits.
Return the result table in any order.
*/
# Write your MySQL query statement below

select project_id  , round(avg(experience_years),2) as average_years
from Project p left join Employee e using(employee_id)
group by project_id