-- 코드를 입력하세요
SELECT a.PRODUCT_CODE, sum(a.PRICE*b.SALES_AMOUNT) as SALES
from PRODUCT a left join OFFLINE_SALE b on a.PRODUCT_ID = b.PRODUCT_ID
group by 1
order by 2 desc,1