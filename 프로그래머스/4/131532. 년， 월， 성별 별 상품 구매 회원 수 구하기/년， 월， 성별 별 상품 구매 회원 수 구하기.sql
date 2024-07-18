-- 코드를 입력하세요
SELECT date_format(SALES_DATE,'%Y') YEAR, date_format(SALES_DATE,'%m') MONTH, GENDER, count(distinct os.USER_ID) USERS
from USER_INFO ui right join ONLINE_SALE os on ui.USER_ID=os.USER_ID
where ui.GENDER is not Null
group by date_format(SALES_DATE,'%Y'), date_format(SALES_DATE,'%m'), GENDER
order by 1,2,3