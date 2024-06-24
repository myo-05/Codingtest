-- 코드를 입력하세요
SELECT a.ANIMAL_ID, a.ANIMAL_TYPE, a.NAME
from ANIMAL_INS a left join ANIMAL_OUTS b on a.ANIMAL_ID=b.ANIMAL_ID
where a.SEX_UPON_INTAKE regexp 'Intact' and b.SEX_UPON_OUTCOME regexp 'Spayed|Neutered'
order by 1