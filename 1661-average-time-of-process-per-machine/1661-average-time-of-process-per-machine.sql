/*
There is a factory website that has several machines each running the same number of processes. 
Write a solution to find the average time each machine takes to complete a process.

The time to complete a process is the 'end' timestamp minus the 'start' timestamp. 
The average time is calculated by the total time to complete every process on the machine divided by the number of processes that were run.

The resulting table should have the machine_id along with the average time as processing_time, which should be rounded to 3 decimal places.

Return the result table in any order.
*/
# Write your MySQL query statement below
select machine_id , round(avg(end-start),3) as processing_time
from (select machine_id, process_id, timestamp as start from Activity where activity_type ='start') a1
join (select machine_id, process_id, timestamp as end from Activity where activity_type ='end') a2
using(machine_id,process_id)
group by 1