# SUBQUERIES
-- 메인쿼리에서 from, where 절에서 사용

use menudb ;

-- 서브쿼리1
select category_code 
  from tbl_menu 
  where menu_name = '열무김치라떼' ;
  
-- 메인쿼리1
select menu_code, menu_name, menu_price, category_code, orderable_status
  from tbl_menu ;

-- 메뉴명이 열무김치라떼인 메뉴의 카테고리와 동일한 카테고리의 메뉴 정보 조회
select menu_code, menu_name, menu_price, category_code, orderable_status
  from tbl_menu 
  where category_code = ( select category_code 
						  from tbl_menu 
					      where menu_name = '열무김치라떼') ;
                          
select menu_code, menu_name, menu_price, category_code, orderable_status
  from tbl_menu 
  where category_code in ( select category_code 
						  from tbl_menu 
					      where menu_name like '%김치%') ;    -- where category_code = 로 사용하면 하나의 row만 반환해야함. 각 조건에 맞게 =, in 으로 구별하여 사용해야함. 
                          
-- 서브쿼리2
select count(*) as 'count'
  from tbl_menu
  group by category_code ;

-- 메인쿼리2
-- select max()
--  from () ;

-- 가장 많은 메뉴가 포함된 카테고리의 메뉴 개수 조회                                 ** join이나 파생테이블에는 반드시 별칭이 붙어야함.
select max(count)
  from (select count(*) as 'count'
		from tbl_menu
		group by category_code) as countmenu ;


# 상관 서브커리
-- 메인쿼리가 서브커리의 결과에 영향을 주는 경우
-- 서브쿼리가 메인쿼리와 떨어져있으면 동작을 안하는 쿼리 (단독동작 x)
select menu_code, menu_name, menu_price, category_code, orderable_status
  from tbl_menu a
  where menu_price > ( select avg(menu_price)
						from tbl_menu
                        where category_code = a.category_code         -- 한건만 반환하기 위한 조건
                        group by category_code ) ;
                        

# exists
-- 조회 결과가 bool 값 반환 
-- 서브쿼리 검색결과가 없는 것은 f 반환 및 결과에 반환 x (inner join 유사)
select category_code, category_name
  from tbl_category a
  where exists (
                 select 1
                 from tbl_menu b
                 where b.category_code = a.category_code
			   ) ;

