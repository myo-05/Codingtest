-- 코드를 입력하세요
SELECT BOOK_ID, AUTHOR_NAME, substr(PUBLISHED_DATE,1,10)
from BOOK a left join AUTHOR b on a.AUTHOR_ID = b.AUTHOR_ID
where a.CATEGORY = "경제"
order by 3