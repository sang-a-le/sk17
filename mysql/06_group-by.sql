# GROUP BY 
-- 집계함수 사용 가능 조건
-- count, sum, avg 사용
select category_code, COUNT(*)      -- category_code에 따라 합계 구하셈
	from tbl_menu 
    group by category_code ;           --  작성순서 : select > from > where > group by > order by > limit
                                       --  해석순서 : from > where > group > select > order > limit
select category_code, sum(menu_price)
	from tbl_menu                       -- category_code별로 menu_price 합계 구해
    group by category_code ;
    
select category_code, avg(menu_price)
	from tbl_menu                       
    group by category_code ;

-- 다중컬럼에 대한 group by (다중그룹)
select category_code, menu_price, COUNT(*)    
	from tbl_menu 
    group by category_code, menu_price ;

    
# having
-- group by 에 쓸 수 있는 where절로 인지 
select category_code, COUNT(*)      
	from tbl_menu 
    group by category_code 
		having category_code between 5 and 8 ;    --  해석순서 : from > where > group > having > select > order > limit
                                                  -- 조회에서의 조건 = wher, group에서의 조건 = having

# roll up
-- 소계
-- 컬럼 한 개를 활용해 GROUP BY 후 ROLLUP -> 총계 (합계)
select category_code, sum(menu_price)
	from tbl_menu                       
    group by category_code 
    with rollup ;                                -- 총합계 명시. 한 컬럼에 대해 group by 했을 경우
 
-- 컬럼 두 개를 활용해 GROUP BY 후 ROLLUP -> 중계 + 총계
-- 먼저 나온 컬럼의 총합을 구하고, 이후에 나오는 컬럼의 총합까지 구하는 방식 
select category_code, menu_price, COUNT(*)    
	from tbl_menu 
    group by category_code, menu_price 
    with rollup ;                                 -- 다중 그룹에 대한 총계 명시 