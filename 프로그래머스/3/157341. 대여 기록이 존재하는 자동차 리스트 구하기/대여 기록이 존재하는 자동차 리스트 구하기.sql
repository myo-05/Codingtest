-- 코드를 입력하세요
SELECT a.CAR_ID
from CAR_RENTAL_COMPANY_CAR a left join CAR_RENTAL_COMPANY_RENTAL_HISTORY b on a.CAR_ID=b.CAR_ID
where a.CAR_TYPE = '세단' and month(b.START_DATE) = 10
group by 1
order by 1 desc