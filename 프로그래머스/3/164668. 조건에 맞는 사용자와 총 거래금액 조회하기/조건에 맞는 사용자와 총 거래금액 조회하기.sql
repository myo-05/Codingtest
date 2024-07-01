-- 코드를 입력하세요
SELECT USER_ID, NICKNAME, sum(PRICE) TOTAL_SALES
from USED_GOODS_BOARD a left join USED_GOODS_USER b on a.WRITER_ID=b.USER_ID
where a.STATUS = 'DONE'
group by b.NICKNAME
having sum(PRICE) >= 700000
order by 3