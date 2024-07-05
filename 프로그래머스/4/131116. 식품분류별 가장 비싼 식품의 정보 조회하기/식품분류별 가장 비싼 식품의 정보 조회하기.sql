-- 코드를 입력하세요
SELECT CATEGORY, PRICE, PRODUCT_NAME
from FOOD_PRODUCT
where PRICE = (select max(price) from FOOD_PRODUCT a where a.CATEGORY=FOOD_PRODUCT.CATEGORY)
group by CATEGORY
having CATEGORY in ('과자', '국', '김치', '식용유')
order by 2 desc