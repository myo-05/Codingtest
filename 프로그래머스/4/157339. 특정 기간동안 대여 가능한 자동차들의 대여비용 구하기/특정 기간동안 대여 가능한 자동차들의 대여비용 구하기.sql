/*
CAR_RENTAL_COMPANY_CAR CR
CAR_RENTAL_COMPANY_RENTAL_HISTORY CH
CAR_RENTAL_COMPANY_DISCOUNT_PLAN CD
자동차 종류가 '세단' 또는 'SUV' 인 자동차 중 
2022년 11월 1일부터 2022년 11월 30일까지 대여 가능하고 
30일간의 대여 금액이 50만원 이상 200만원 미만인 자동차에 대해서 
자동차 ID, 자동차 종류, 대여 금액(컬럼명: FEE) 리스트를 출력하는 SQL문을 작성해주세요. 
    결과는 대여 금액을 기준으로 내림차순 정렬하고, 
    대여 금액이 같은 경우 자동차 종류를 기준으로 오름차순 정렬, 
    자동차 종류까지 같은 경우 자동차 ID를 기준으로 내림차순 정렬해주세요.
*/

-- 코드를 입력하세요
SELECT car_id, car_type, round(daily_fee*30*(1-0.01*discount_rate),0) as FEE
from CAR_RENTAL_COMPANY_RENTAL_HISTORY CH
left join CAR_RENTAL_COMPANY_CAR CR using(CAR_ID)
join CAR_RENTAL_COMPANY_DISCOUNT_PLAN CD using(CAR_TYPE)
where car_type in ('세단','SUV')
    and duration_type like '30일%'
group by car_id
having max(end_date) < '2022-11-01'
    and FEE between 500000 and 2000000-1
order by 3 desc, 2, 1 desc