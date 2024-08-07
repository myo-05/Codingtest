/*
Write a solution to find the number of times each student attended each exam.

Return the result table ordered by student_id and subject_name.
*/
# Write your MySQL query statement below
select student_id , student_name ,subject_name ,count(S.subject_name=E.subject_name) as attended_exams
from Students cross join Subjects S left join Examinations E using(student_id,subject_name)
group by 1, 3
order by 1, 3