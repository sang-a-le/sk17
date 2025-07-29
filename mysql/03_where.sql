# WHERE
-- 1) 비교 연산자 
-- 같음 : == (python), = (sql)
select menu_name, menu_price, orderable_status
	from tbl_menu
    where orderable_status = 'y' ;     -- order by 가 젤 끝에 작성. 해석순서 : from > where > select > order
    
-- 같지 않음 : != (python. sql도 가능), <>를 더 많이 씀
select menu_name, menu_price, orderable_status
	from tbl_menu
    where orderable_status <> 'y' ; 
  
-- 대소 비교 : >, <, >=, <=
select menu_name, menu_price, orderable_status
	from tbl_menu
    where menu_price <= 20000 ;                   -- 10000 < menu_price <= 20000 : 오류는 발생하지 않으나 정상 결과를 현출하지 않음. 


-- 2) and
select menu_name, menu_price, orderable_status
	from tbl_menu
    where 10000 < menu_price 
		and menu_price <= 20000 ; 
  
  
-- 3) or
-- 메뉴 가격이 30000원 초과이거나 메뉴 이름이 '열무김치라떼'인 메뉴
select menu_name, menu_price, orderable_status
	from tbl_menu
    where menu_price > 30000
		or menu_name = '열무김치라떼' ;         -- and, or 은 where 안에 써야함!! 우선순위는 괄호 안에 부여할 수 있음. 
 
 
-- 4) between
select menu_name, menu_price, orderable_status
	from tbl_menu
    where menu_price between 10000 and 20000 ;    -- between and , and 혼동 주의 (where and 조건을 한 줄로 정리 가능)

select menu_name, menu_price, orderable_status
	from tbl_menu
    where menu_price not between 10000 and 20000 ;  -- 초과, 미만


-- 5) like
select menu_name, menu_price, orderable_status
	from tbl_menu
    where menu_name like '%김치%' ;                   -- like 뒤에 원하는 포함자 뿐아니라 %붙여야함. 무조건 % 포함. 

select menu_name, menu_price, orderable_status
	from tbl_menu
    where menu_name not like '%김치%' ;               -- 하나의 값에 포함된 여부를 체크


-- 6) in
select menu_name, menu_price, orderable_status, category_code
	from tbl_menu
    where category_code = 4
		or category_code = 5
		or category_code = 6 ;
    
select menu_name, menu_price, orderable_status, category_code
	from tbl_menu
    where category_code in (4, 5, 6) ;               -- in 뒤의 소괄호 중 하나의 값을 포함하는지? 
    
select menu_name, menu_price, orderable_status, category_code
	from tbl_menu
    where category_code not in (4, 5, 6) ; 


-- 7) is null
select category_code, category_name, ref_category_code
	from tbl_category 
    where ref_category_code is null ; 
    
select category_code, category_name, ref_category_code
	from tbl_category 
    where ref_category_code is not null ; 
