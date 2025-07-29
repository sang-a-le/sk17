# DISTINCT
-- 중복 컬럼 중 하나씩만 가져옴, select 바로 뒤
select distinct category_code
	from tbl_menu
    order by category_code ;

select distinct ref_category_code
	from tbl_category ;                               -- null도 하나만 나옴
    
select distinct category_code, orderable_status
	from tbl_menu 
    order by category_code, orderable_status ;        -- 다중컬럼에 대해 distinct를 돌렸을때 조합이 중복아닌 값을 반환
