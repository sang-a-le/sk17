# JOIN 
-- 별칭 (alias 필수)

# alias (별칭)
select menu_code as 'code' , 
	   menu_name as name , 
	   menu_price as '메뉴의 가격'
from tbl_menu ;            -- colimns 별칭

select m.menu_code, m.menu_name, m.menu_price
from tbl_menu as m ;            -- table 별칭

select m.menu_code, m.menu_name, m.menu_price
from tbl_menu m ;              -- as 생략 가능


# inner join  (join의 기본 형태. inner 생략 가능)
select m.menu_code, m.menu_name, c.category_name                       -- 어떤 테이블에서 온건지 명시하기 위해 별칭. 형태로 사용
  from tbl_menu m
  join tbl_category c on m.category_code = c.category_code ;           -- 각 테이블에서 식별자 지정

select m.menu_code, m.menu_name, c.category_name                    
  from tbl_menu m
  join tbl_category c using (category_code) ; -- 식별자의 컬럼명이 동일할 시 컬럼이름 하나만 사용해서 작성 가능

  
# outer join 
-- left join 
select m.menu_code, m.menu_name, c.category_name                    
  from tbl_category c
  left join tbl_menu m on m.category_code = c.category_code ;           -- category table 기준 join 

-- right join 
select m.menu_code, m.menu_name, c.category_name                    
  from tbl_menu m
  right join tbl_category c on m.category_code = c.category_code ;      
  
  
  -- inner join = 교집합 개념. 테이블 상호 값이 있을 때 반환
  -- outer join = 합집합 개념. 테이블 상호 값이 없어도 둘 중 한 테이블에만 있어도 반환. 
      -- left, right : join 에서 기준 테이블 선정. 기준테이블에서의 값이 다른 테이블에 없어도 반환(null값 처리)
	  -- left : from 절, right : join 절 의 변수 기준
  
# cross join
select a.menu_name, b.category_name
  from tbl_menu a
  cross join tbl_category b ;                        -- 각 테이블 별 대상 로우의 모든 조합 반환 (on, using 키워드 없음). 실질적인 사용은 거의 없음

# self join 
-- 모델링 중 재귀 참조 관계에서 사용
select a.category_name, b.category_name as '상위 카테고리명'
  from tbl_category a
  join tbl_category b on a.ref_category_code = b.category_code ;   -- inner join 에서 재귀관계에 있을 때 사용. null 값 반환 x. 
  
select a.category_name, b.category_name as '상위 카테고리명'
  from tbl_category a
left join tbl_category b on a.ref_category_code = b.category_code ;  -- 카테고리명이 없더라도 category_name 반환 (재귀관계)

