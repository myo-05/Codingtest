/*
USER_INFO UI
ONLINE_SALE OS
2021년에 가입한 전체 회원들 중 상품을 구매한 회원수와 상품을 구매한 회원의 비율
(=2021년에 가입한 회원 중 상품을 구매한 회원수 / 2021년에 가입한 전체 회원 수)을 년, 월 별로 출력하는 SQL문을 작성해주세요. 
    상품을 구매한 회원의 비율은 소수점 두번째자리에서 반올림하고, 
    전체 결과는 년을 기준으로 오름차순 정렬해주시고 
    년이 같다면 월을 기준으로 오름차순 정렬해주세요.
*/

-- 코드를 입력하세요
with joined_2021 as (
    SELECT count(*) as total_user
    from USER_INFO
    where year(joined) = '2021'
)
select YEAR(sales_date) as YEAR, MONTH(sales_date) as MONTH, count(distinct USER_ID) as PURCHASED_USERS,
    round(count(distinct USER_ID)/(select total_user from joined_2021),1)as PUCHASED_RATIO
from ONLINE_SALE join USER_INFO using(USER_ID)
where year(joined) = '2021'
group by YEAR,MONTH
order by 1,2