-- 코드를 입력하세요
SELECT DISTINCT(b.CAR_ID),
        case
        when a.CAR_ID is Null then '대여 가능'
        else '대여중'
        end as AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY b
left join
(SELECT CAR_ID
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where '2022-10-16' between START_DATE and END_DATE
) as a
on a.CAR_ID=b.CAR_ID
order by 1 desc