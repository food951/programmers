-- 코드를 입력하세요
SELECT a.animal_id, a.animal_type,a.name
from animal_ins as a
inner join animal_outs as b
on a.animal_id = b.animal_id
where (a.SEX_UPON_INTAKE  LIKE 'Intact%') and (b.SEX_UPON_OUTCOME LIKE 'Spayed%' OR b.SEX_UPON_OUTCOME LIKE 'Neutered%')
