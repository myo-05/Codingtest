/*
We define query quality as:
    The average of the ratio between query rating and its position.

We also define poor query percentage as:
    The percentage of all queries with rating less than 3.

Write a solution to find each query_name, the quality and poor_query_percentage.
Both quality and poor_query_percentage should be rounded to 2 decimal places.
Return the result table in any order.
*/
# Write your MySQL query statement below
select query_name ,round(avg(rating/position),2) as quality, round(count(case when rating<3 then 1 end)/count(rating)*100,2) as poor_query_percentage
from Queries
where query_name is not null
group by query_name