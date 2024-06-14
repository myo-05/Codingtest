-- 코드를 입력하세요
SELECT MCDP_CD 진료과코드, count(*) 5월예약건수
from APPOINTMENT
where substr(APNT_YMD,1,7) = '2022-05'
group by MCDP_CD
order by 2,1