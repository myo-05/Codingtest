/*
FIRST_HALF FH : TOTAL_ORDER
JULY J : TOTAL_ORDER
7월 아이스크림 총 주문량과 상반기의 아이스크림 총 주문량을 더한 값이 
큰 순서대로 상위 3개의 맛을 조회
*/
-- 코드를 입력하세요
with FH_FLAVOR_TOTAL_ORDER as (
    select FLAVOR, sum(TOTAL_ORDER) as TOTAL_ORDERS
    from FIRST_HALF
    group by FLAVOR
),
    J_FLAVOR_TOTAL_ORDER as (
    select FLAVOR, sum(TOTAL_ORDER) as TOTAL_ORDERS
    from JULY
    group by FLAVOR
)
SELECT FH.FLAVOR
from (select * from J_FLAVOR_TOTAL_ORDER) J 
join (select * from FH_FLAVOR_TOTAL_ORDER) FH on J.FLAVOR = FH.FLAVOR
order by (FH.TOTAL_ORDERS + J.TOTAL_ORDERS) desc
limit 3
