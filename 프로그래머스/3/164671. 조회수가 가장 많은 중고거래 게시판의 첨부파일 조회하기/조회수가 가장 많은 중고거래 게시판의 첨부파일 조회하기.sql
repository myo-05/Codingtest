/*
 조회수가 가장 높은 중고거래 게시물에 대한 첨부파일 경로를 조회
 FILE ID를 기준으로 내림차순 정렬
    기본적인 파일경로는 /home/grep/src/ 이며,
    게시글 ID를 기준으로 디렉토리가 구분되고, 
    파일이름은 파일 ID, 파일 이름, 파일 확장자로 구성
 ex) /home/grep/src/B0001/IMG_000001photo1.jpg
 조회수가 가장 높은 게시물은 하나만 존재
*/
-- 코드를 입력하세요
with BEST_VIEWS as (
    select BOARD_ID
    from USED_GOODS_BOARD
    order by VIEWS desc
    limit 1
)
SELECT CONCAT('/home/grep/src/',BOARD_ID,'/',FILE_ID,FILE_NAME,FILE_EXT) as FILE_PATH
from USED_GOODS_FILE F 
where BOARD_ID = (select BOARD_ID from BEST_VIEWS)
order by FILE_ID desc
