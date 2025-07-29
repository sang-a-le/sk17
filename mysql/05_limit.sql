# LIMIT 

select menu_code, menu_name, menu_price
	from tbl_menu
    order by menu_price desc ;

-- row count = 3
select menu_code, menu_name, menu_price
	from tbl_menu
    order by menu_price desc 
    limit 3 ;                                         -- from > where > select > order by > limit
                                                      -- 상위 조건 중 몇번째까지만 잘라오는 조건 (하나만 있을때는 ~까지 갯수 부여)
-- offset = 2, row count = 5
select menu_code, menu_name, menu_price
	from tbl_menu
    order by menu_price desc 
    limit 2, 5 ;                                      -- 위의 2개 건너띄고, 5개 가져와 (offset, 갯수)