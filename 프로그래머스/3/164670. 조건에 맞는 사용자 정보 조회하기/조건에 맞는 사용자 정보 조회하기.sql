-- 코드를 입력하세요
SELECT USER_ID,NICKNAME,CONCAT(CITY,' ',STREET_ADDRESS1,' ',STREET_ADDRESS2) "전체주소",
REGEXP_REPLACE(TLNO, '^([0-9]{3})([0-9]{4})([0-9]{4})$','$1-$2-$3') "전화번호" 
from USED_GOODS_USER U
join
(
 select WRITER_ID
 from USED_GOODS_BOARD
 group by 1
 having count(*)>=3
) B
on U.USER_ID=B.WRITER_ID
order by 1 desc