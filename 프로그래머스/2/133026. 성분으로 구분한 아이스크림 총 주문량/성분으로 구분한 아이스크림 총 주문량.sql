-- 코드를 입력하세요
SELECT INGREDIENT_TYPE , sum(TOTAL_ORDER) as TOTAL_ORDER
from FIRST_HALF a left join ICECREAM_INFO b on a.FLAVOR=b.FLAVOR
group by 1
order by 2