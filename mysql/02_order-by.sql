# ORDER BY

-- 오름차순 정렬 (asc를 명시하지 않아도 기본 정렬 방식)
select menu_code, menu_name, menu_price
	from tbl_menu
    order by menu_name asc;   -- asc: 어샌딩(오릅차순), 기준값 / 
    
-- 내림차순 정렬 (desc를 명시적으로 작성해야 내림차순 정렬)
select menu_code, menu_name, menu_price
	from tbl_menu
    order by menu_name desc;  -- desc: 디샌딩(내림차순)
    
-- 다중조건 정렬 (order by 1차 정렬, 2차정렬)
select menu_code, menu_name, menu_price
	from tbl_menu
    order by menu_price desc, menu_name ;
    
-- select 절에서의 연산, 컬럼의 연산 결과로 정렬
select menu_code, menu_name, menu_price, menu_price*menu_code
	from tbl_menu
    order by menu_code*menu_price ;
    
-- 별칭을 사용한 정렬
select menu_code, menu_name, menu_price, menu_price*menu_code as '연산결과'    -- 한글이나 띄어쓰기 포함시 따움표 작성
	from tbl_menu
    order by '연산결과' ;
    
-- 오릅차순 정렬 시 기본적으로 (default) Null이 맨처음
-- is null을 붙이면 NULL을 맨끝으로 보냄 (IS NULL ASC)
select category_code, category_name, ref_category_code    -- ref : 재귀적 용법
	from tbl_category 
	order by ref_category_code is null ;

-- 내림차순 정렬 시 기본적으로 (default) Null 이 맨끝
-- IS NULL을 붙이면 NULL 을 맨처음으로 보낸 (is null desc) : DESC 생략 불가 
select category_code, category_name, ref_category_code  
	from tbl_category 
	order by ref_category_code is null desc, ref_category_code desc ;  -- is null desc 사용 시 : null을 제외한 코드는 내림차순 정렬이 안일어남. 따라서 해당 변수도 조건 부여 필요
    
