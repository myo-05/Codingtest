-- 코드를 입력하세요
SELECT B.APNT_NO, P.PT_NAME, P.PT_NO, B.MCDP_CD, B.DR_NAME, B.APNT_YMD as APNT_YMD
from PATIENT P join
(
    select A.APNT_NO, A.MCDP_CD, D.DR_NAME, A.APNT_YMD, PT_NO
    from APPOINTMENT A join DOCTOR D on A.MDDR_ID=D.DR_ID
    where date_format(A.APNT_YMD,'%Y-%m-%d') = '2022-04-13' and A.APNT_CNCL_YN ='N'
) as B
on P.PT_NO = B.PT_NO
order by APNT_YMD