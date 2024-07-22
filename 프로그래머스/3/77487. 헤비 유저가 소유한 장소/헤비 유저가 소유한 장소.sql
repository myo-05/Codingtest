-- 코드를 입력하세요
with heavy_users as (
    select *
    from PLACES
    group by HOST_ID
    having count(*)>=2
)
SELECT *
from PLACES
where HOST_ID in (select HOST_ID from heavy_users)
order by ID