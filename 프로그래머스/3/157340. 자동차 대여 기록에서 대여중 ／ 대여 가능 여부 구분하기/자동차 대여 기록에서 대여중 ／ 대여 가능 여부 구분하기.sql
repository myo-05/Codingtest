-- 코드를 입력하세요
with car_AVAILABILITY as(
    SELECT CAR_ID
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where '2022-10-16' between START_DATE and END_DATE
)
SELECT CAR_ID,
        case
            when CAR_ID in (select CAR_ID from car_AVAILABILITY) then '대여중'
            else '대여 가능'
        end as AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by 1
order by 1 desc