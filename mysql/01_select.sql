# select from

use menudb;


-- 단일 칼럼 조회
select menu_name 
	from tbl_menu;
    
-- 다중 컬럼 조회
select menu_code, menu_name, menu_price, category_code, orderable_status    -- 보고싶은 컬럼 이름 나열
	from tbl_menu;

-- 전체 컬럼 조회
select *
	from tbl_menu;    
    
-- 연산자 사용
select 7+4 ;
select 7-4 ;
select 7*4 ; 
select 7/4 ;
select 7%4 from dual;   -- mood 연산은 지원. 
-- mysql은 from 절 없어도 가능 (but 오라클의 경우 필수, 이런 경우에는 from dual; 작성) mysql에서도 노상관


    
