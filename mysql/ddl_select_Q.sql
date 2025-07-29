-- DDL
-- 조건
-- TEAM_INFO 테이블의 PRIMARY KEY와 MEMBER_INFO 테이블의 PRIMARY KEY는 AUTO_INCREMENT 설정을 해 값이 자동 채번되도록 한다.
-- TEAM_INFO 테이블의 USE_YN 컬럼의 기본값은 ‘Y’이며, ‘Y’또는 ‘N’의 데이터만 삽입할 수 있다.
-- MEMBER_INFO 테이블의 ACTIVE_STATUS 컬럼의 기본값은 ‘Y’이며, 활동 중을 의미하는 ‘Y’, 휴식 중을 의미하는 ‘N’, 잠정적 활동 상태인 ‘H’만 삽입할 수 있다.
CREATE TABLE IF NOT EXISTS team_info (
    pk INT AUTO_INCREMENT PRIMARY KEY,
    fk INT,
    col1 VARCHAR(3),
    CHECK(col1 IN ('Y', 'N'))
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS member_info (
    pk INT AUTO_INCREMENT PRIMARY KEY,
    fk INT,
    col1 VARCHAR(3),
    CHECK(col1 IN ('Y', 'N', 'H'))
) ENGINE=INNODB;

insert into team_info value (null, 10, 'y');
select * from team_info;

insert into member_info value (null, 10, 'h');
select * from member_info;

-- select 
-- Q1. 상위 카테고리 코드가 null이 아닌 카테고리의 카테고리 코드와 카테고리명을 출력하세요. 단, 카테고리명을 기준으로 내림차순 정렬하여 출력하세요.
select *
	from tbl_category
	where category_code is not null
    order by category_name desc ;
    
-- Q2.메뉴명에 '밥'이 포함되고, 가격이 20,000원 이상 30,000원 이하인 메뉴의 메뉴명과 가격을 출력하세요.
select menu_name, menu_price
	from tbl_menu
    where menu_name like '%밥%'
		and menu_price between 20000 and 30000 ;
        
-- Q3. 가격이 10,000원 미만이거나, 메뉴명에 김치가 포함되는 메뉴의 모든 컬럼을 출력하세요.
-- 단, 가격을 기준으로 오름차순 정렬하고, 추가로 메뉴명을 기준으로 내림차순 정렬하여 출력하세요.
select *
	from tbl_menu
    where menu_price < 10000
		or menu_name like '%김치%'
	order by menu_name ;
    
-- Q4. Q1에서 출력한 카테고리명 결과를 참고하여, 카테고리가 기타, 쥬스, 커피에 해당하지 않는 메뉴 중 메뉴 가격이 13,000원인 메뉴의 모든 컬럼을 출력하세요.
-- 단, 주문이 불가능한 상품은 출력하지 않습니다.
select * 
	from tbl_menu
    where category_code not in (8, 9, 10)
		and menu_price = 13000
        and orderable_status != 'N' ;