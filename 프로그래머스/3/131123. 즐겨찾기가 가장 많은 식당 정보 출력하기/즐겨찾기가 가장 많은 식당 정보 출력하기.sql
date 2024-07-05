-- 코드를 입력하세요
SELECT info.FOOD_TYPE, info.REST_ID, info.REST_NAME, FAVORITES
from REST_INFO as info
join
(SELECT FOOD_TYPE, REST_ID, max(FAVORITES) as MAX_FAVORITES
from REST_INFO
group by FOOD_TYPE) as max_FAVORITES
on info.FOOD_TYPE=max_FAVORITES.FOOD_TYPE and info.FAVORITES=max_FAVORITES.MAX_FAVORITES
order by 1 desc