-- 코드를 입력하세요
SELECT a.CATEGORY, sum(b.SALES) TOTAL_SALES
from BOOK as a left join BOOK_SALES as b on a.BOOK_ID = b.BOOK_ID
where substr(b.SALES_DATE,1,7) = '2022-01'
group by 1
order by 1