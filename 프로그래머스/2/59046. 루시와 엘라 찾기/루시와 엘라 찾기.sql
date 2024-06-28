-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
from ANIMAL_INS
WHERE NAME REGEXP '\\b(Lucy|Ella|Pickle|Rogan|Sabrina|Mitty)\\b'
order by 1