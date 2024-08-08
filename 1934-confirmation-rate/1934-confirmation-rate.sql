/*
The confirmation rate of a user is the number of 'confirmed' messages divided by the total number of requested confirmation messages. 
The confirmation rate of a user that did not request any confirmation messages is 0. 
    Round the confirmation rate to two decimal places.
Write a solution to find the confirmation rate of each user.
    Return the result table in any order.
*/
# Write your MySQL query statement below
with CR as (
    select user_id, round(sum(action ='confirmed')/count(time_stamp),2) as confirmation_rate
    from Confirmations 
    group by 1
) 
select user_id , coalesce(confirmation_rate,0) as confirmation_rate
from Signups left join CR using (user_id)