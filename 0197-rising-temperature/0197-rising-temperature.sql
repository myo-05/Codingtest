/*
Write a solution to find all dates' Id with higher temperatures compared to its previous dates (yesterday).
Return the result table in any order.
*/
# Write your MySQL query statement below

select id      
from Weather
left join
(select date_add(recordDate,interval 1 day) as recordDate, temperature as y_temperature
from Weather) y using(recordDate)
where temperature > y_temperature