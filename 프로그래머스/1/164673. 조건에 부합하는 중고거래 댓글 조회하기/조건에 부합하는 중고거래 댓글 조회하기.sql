/*
USED_GOODS_BOARD b, USED_GOODS_REPLY r 
2022년 10월에 작성된 게시글 제목, 게시글 ID, 댓글 ID, 댓글 작성자 ID, 댓글 내용, 댓글 작성일을 조회하는 SQL문을 작성해주세요. 
    결과는 댓글 작성일을 기준으로 오름차순 정렬해주시고, 댓글 작성일이 같다면 게시글 제목을 기준으로 오름차순 정렬해주세요.
*/
-- 코드를 입력하세요
SELECT TITLE, b.BOARD_ID, REPLY_ID, r.WRITER_ID, r.CONTENTS, date_format(r.CREATED_DATE,'%Y-%m-%d') as CREATED_DATE
from USED_GOODS_REPLY r join USED_GOODS_BOARD b using (BOARD_ID)
where date_format(b.CREATED_DATE,'%Y-%m') = '2022-10'
order by CREATED_DATE, TITLE