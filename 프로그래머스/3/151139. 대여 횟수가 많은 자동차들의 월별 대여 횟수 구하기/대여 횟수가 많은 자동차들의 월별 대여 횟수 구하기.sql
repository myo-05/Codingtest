/*
 대여 시작일을 기준으로 2022년 8월부터 2022년 10월까지 총 대여 횟수가 5회 이상인 자동차들에 대해서 
 해당 기간 동안의 월별 자동차 ID 별 총 대여 횟수(컬럼명: RECORDS) 리스트를 출력하는 SQL문을 작성해주세요. 
    결과는 월을 기준으로 오름차순 정렬하고, 월이 같다면 자동차 ID를 기준으로 내림차순 정렬해주세요. 
    특정 월의 총 대여 횟수가 0인 경우에는 결과에서 제외해주세요.
*/

-- 2022년 8월부터 2022년 10월까지 총 대여 횟수가 5회 이상인 자동차
with car as (
    select CAR_ID 
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where date_format(START_DATE,'%Y-%m') between '2022-08' and '2022-10'
    group by 1
    having count(*) >= 5
)
SELECT date_format(START_DATE,'%m') as MONTH, CAR_ID, count(*) RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where CAR_ID in (select * from car) and (date_format(START_DATE,'%Y-%m') between '2022-08' and '2022-10')
group by 1, 2
having count(*) > 0
order by 1, 2 desc