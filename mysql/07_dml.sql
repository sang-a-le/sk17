# DML

use menudb ;

select menu_code, menu_name, menu_price, category_code, orderable_status
from tbl_menu ; 

# insert
-- insert into 테이블명 values (컬럼순으로, 들어갈, 데이터, 나열, ,,)
insert	into tbl_menu values (null, '회냉면', 12000, 4, 'Y' );   -- 하나의 로우로 생성, insert / update / delete 의 경우, 전체 값이 아닌 몇개의 로우가 영향을 받았는지가 보임. 
                                                                -- 테이블 구조를 정확히 알아야함. 일일이 해석해야함. 
																-- menu_code가 pk이고, AUTO_INCREMENT 설정으로 자동 입력됨. 
insert into tbl_menu(menu_code, menu_name, menu_price, orderable_status, category_code)
	values (null, '직화불고기', 17000, 'Y', 4) ;                   -- 나열된 컬럼의 순서와 동일하게 입력됨. 자료 식별에 편리하여 선호하는 방법

insert into tbl_menu(menu_name, menu_price, orderable_status, category_code)
	values ('카페라떼', 4500, 'Y', 7) ;                            

insert into tbl_menu
	values 
    (null, '화이트머쉬룸버거', 12000, 12, 'Y'), 
    (null, '프렌치프라이', 2500, 12, 'Y'),
    (null, '코울슬로', 1200, 12, 'Y') ;                             -- 여러개의 데이터 입력 
    
insert into tbl_menu values (100, '한방능이100숙', 1000000, 4, 'Y') ;    -- pk 임의 조작 가능, 다음 인서트시에는 마지막 값의 설정값에 +1 해서 부여. 임의 삽입은 지양

# update
-- update 테이블명
-- 	set 컬럼명1 = 수정할 데이터1, 컬럼명2 = 수정할 데이터2, ...
-- [ where 수정대상 데이터의 조건 ] ;    블럭잡고, ctrl, +,  / : 전체 주석

update	tbl_menu
	set menu_name = '100번이었던 음식' ,
		menu_price = 19000 
	where menu_code = 100 ;


# delete
-- delete from 테이블명 [ where 삭제 조건 ] ;

delete from tbl_menu
	where menu_code = 101 ;                        -- AUTO_INCREMENT 설정으로 인해 다음변수 부여시 102으로 pk 사용 (delete 됐어도 동일)
    
delete from tbl_menu                                -- just mysql에서만 사용
	order by menu_code desc
    limit 3 ;

# replace	
-- 중복값에 대해서는 데이터를 덮어 쓰고, 중복값이 없다면 insert (중복값 판단의 기준은 pk)
-- INTO 키워드는 생략가능
insert into tbl_menu values (100, '한방능이100숙', 1000000, 4, 'Y') ; 
replace into tbl_menu values (100, '한방능이백숙', 1000000, 4, 'Y') ;    -- 2rows affected : 존재하는 값을 없애고, 값 insert
replace tbl_menu values (120, '새로운120번메뉴', 20000, 4, 'Y') ;        -- 1rows affected : insert 처럼 작용