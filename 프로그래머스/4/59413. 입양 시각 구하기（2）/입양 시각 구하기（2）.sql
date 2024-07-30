/*
보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다.
0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요.
    이때 결과는 시간대 순으로 정렬해야 합니다.
*/

-- 0~23시간 만들기
with recursive hours AS (
  SELECT 0 AS hour
  UNION ALL
  SELECT hour + 1 FROM hours
    WHERE hour < 23
)
SELECT hours.hour as HOUR, coalesce(count(ANIMAL_OUTS.DATETIME),0) as COUNT
from hours 
left join ANIMAL_OUTS on hours.hour = HOUR(ANIMAL_OUTS.DATETIME)
group by 1
order by 1