-- 코드를 입력하세요
SELECT CAR_TYPE, count(*) as CARS
from CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS REGEXP '통풍시트|열선시트|가죽시트'
group by 1
order by 1