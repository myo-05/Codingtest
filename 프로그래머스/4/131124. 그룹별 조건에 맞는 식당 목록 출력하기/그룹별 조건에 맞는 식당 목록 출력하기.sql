/*
MEMBER_PROFILE mp , REST_REVIEW rr
리뷰를 가장 많이 작성한 회원의 리뷰들을 조회하는 SQL문을 작성해주세요. 
회원 이름, 리뷰 텍스트, 리뷰 작성일이 출력되도록 작성해주시고, 
결과는 리뷰 작성일을 기준으로 오름차순, 리뷰 작성일이 같다면 리뷰 텍스트를 기준으로 오름차순 정렬해주세요.
*/

-- 리뷰를 가장 많이 작성한 회원
with best_reviewer as (
    select MEMBER_ID, count(*)
    from REST_REVIEW 
    group by 1
    order by 2 desc
    limit 1
)

SELECT MEMBER_NAME, REVIEW_TEXT, date_format(REVIEW_DATE,'%Y-%m-%d') as REVIEW_DATE
from MEMBER_PROFILE
join REST_REVIEW using(MEMBER_ID)
where MEMBER_ID = (select MEMBER_ID from best_reviewer)
order by 3, 2