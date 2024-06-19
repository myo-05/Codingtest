-- 코드를 입력하세요
SELECT a.NAME, a.DATETIME
from ANIMAL_INS as a left join ANIMAL_OUTS as b on a.ANIMAL_ID = b.ANIMAL_ID
where b.DATETIME is null # 아직 입양을 못 간 동물
order by 2
limit 3