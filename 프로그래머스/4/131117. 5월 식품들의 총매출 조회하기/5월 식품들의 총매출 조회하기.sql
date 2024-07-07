-- 코드를 입력하세요
SELECT a.PRODUCT_ID, PRODUCT_NAME, PRICE*Total_AMOUNT TOTAL_SALES
from FOOD_PRODUCT a
join
(select PRODUCT_ID, sum(AMOUNT) Total_AMOUNT
 from FOOD_ORDER
 where DATE_FORMAT(PRODUCE_DATE,'%Y-%m') = '2022-05'
 group by 1
) b
on a.PRODUCT_ID=b.PRODUCT_ID
order by 3 desc, 1