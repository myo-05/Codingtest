/*
BOOK b , AUTHOR a , BOOK_SALES s
2022년 1월의 도서 판매 데이터를 기준으로
저자 별, 카테고리 별 매출액(TOTAL_SALES = 판매량 * 판매가) 을 구하여,
저자 ID(AUTHOR_ID), 저자명(AUTHOR_NAME), 카테고리(CATEGORY), 매출액(SALES) 리스트를 출력하는 SQL문을 작성해주세요.
    결과는 저자 ID를 오름차순으로, 저자 ID가 같다면 카테고리를 내림차순 정렬해주세요.
*/

-- 2022년 1월 BOOK_ID 별 판매량
with book_sale_2022_01 as (
    select BOOK_ID , sum(sales) sales_amount, SALES_DATE
    from BOOK_SALES
    where date_format(SALES_DATE,'%Y-%m') = '2022-01'
    group by 1
), -- BOOK + AUTHOR
    book_info as (
    select b.BOOK_ID, b.CATEGORY, b.AUTHOR_ID, b.PRICE, a.AUTHOR_NAME 
    from BOOK b join AUTHOR a on b.AUTHOR_ID=a.AUTHOR_ID
)

-- (BOOK_ID 별 판매량 * BOOK_ID 별 가격) = BOOK_ID 별 매출액
SELECT AUTHOR_ID, AUTHOR_NAME, CATEGORY, sum(PRICE*sales_amount) as TOTAL_SALES
from (select * from book_info) bi
join (select * from book_sale_2022_01) s
on bi.BOOK_ID=s.BOOK_ID
group by 1,3
order by 1,3 desc