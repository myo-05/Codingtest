/*
CAR_RENTAL_COMPANY_CAR C
CAR_RENTAL_COMPANY_RENTAL_HISTORY RH
CAR_RENTAL_COMPANY_DISCOUNT_PLAN DP
자동차 종류가 '트럭'인 자동차의 대여 기록에 대해서 
대여 기록 별로 대여 금액(컬럼명: FEE)을 구하여 
대여 기록 ID와 대여 금액 리스트를 출력하는 SQL문을 작성해주세요. 
    결과는 대여 금액을 기준으로 내림차순 정렬하고, 
    대여 금액이 같은 경우 대여 기록 ID를 기준으로 내림차순 정렬해주세요.
*/

-- 코드를 입력하세요
SELECT HISTORY_ID, round(DAILY_FEE*rental_period*(1-0.01*coalesce(DISCOUNT_RATE,0)),0) as FEE
from (
    select history_id, car_id, datediff(END_DATE,START_DATE)+1 as rental_period,
    case 
    when datediff(END_DATE,START_DATE)+1 between 7 and 29 then '7일 이상'
    when datediff(END_DATE,START_DATE)+1 between 30 and 89 then '30일 이상'
    when datediff(END_DATE,START_DATE)+1 >= 90 then '90일 이상'
end as DURATION_TYPE
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
) as RH
join CAR_RENTAL_COMPANY_CAR C using(CAR_ID)
left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN DP on C.CAR_TYPE=DP.CAR_TYPE and RH.DURATION_TYPE=DP.DURATION_TYPE
where C.CAR_TYPE = '트럭'
order by 2 desc, 1 desc