# SET OPERATORS
# union
-- 합집합

# union all
-- 합집합 & 교집합 = A + B

# intersect
-- 교집합
-- mysql은 intersect를 제공하지 않음
-- 단, inner join 또는 in 을 통해 구현가능

# minus
-- 차집합
-- mysql은 minus를 제공하지 않음
-- 단, left join을 활용한 구현가능

# union
select menu_code, menu_name, menu_price, category_code
  from tbl_menu
 where category_code = 10 ;
 
 
# union all
# intersect
# minus


-- --------------------------------------------------
# SET OPERATORS
# union
-- 합집합

# union all
-- 합집합 & 교집합 = A + B

# intersect
-- 교집합
-- mysql은 intersect를 제공하지 않음
-- 단, inner join 또는 in 을 통해 구현가능

# minus
-- 차집합
-- mysql은 minus를 제공하지 않음
-- 단, left join을 활용한 구현가능


# union             -- join은 옆으로 붙임. unoin은 아래로 붙임. (▲ union은 칼럼의 수가 동일해야함) / 각 조건이 반대되는 경우, join을 사용해야하거나 하나의 where 구문에서 하기 어려운 경우 사용
select menu_code, menu_name, menu_price, category_code
  from tbl_menu
 where category_code = 10    -- ; 붙이면 안됨
union
 select menu_code, menu_name, menu_price, category_code
  from tbl_menu
 where menu_price < 9000 ;   -- 하나가 통쨰로의 쿼리 구문
 
# union all          -- 두 조건에 중복되는 경우, 두번 출력.
select menu_code, menu_name, menu_price, category_code
  from tbl_menu
 where category_code = 10    -- ; 붙이면 안됨
union all
 select menu_code, menu_name, menu_price, category_code
  from tbl_menu
 where menu_price < 9000 ; 
 
# intersect
-- 1) inner join 사용
select a.menu_code, a.menu_name, a.menu_price, a.category_code
  from tbl_menu a
  join ( 
          select menu_code, menu_name, menu_price, category_code
			from tbl_menu
		   where menu_price < 9000
		) b on a.menu_code = b.menu_code
 where a.category_code = 10 ;            -- select, where 절에서 변수가 혼동되지 않도록 별칭 지정 필요

-- 2) in 사용
select menu_code, menu_name, menu_price, category_code
  from tbl_menu
 where category_code = 10
   and menu_code in (  select menu_code, menu_name, menu_price, category_code
					     from tbl_menu
						where menu_price < 9000 ) ;

# minus
select a.menu_code, a.menu_name, a.menu_price, a.category_code
  from tbl_menu a
left join ( 
          select menu_code, menu_name, menu_price, category_code
			from tbl_menu
		   where menu_price < 9000
		  ) b on a.menu_code = b.menu_code
 where a.category_code = 10
   and b.menu_code is NULL ; 