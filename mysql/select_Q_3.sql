-- Q1.
-- 부서별 직원 급여의 총합 중 가장 큰 액수를 출력하세요.
use employeedb ;
select * from employee ;
select * from department ;

select max(sum)
from (
		select sum(salary) as sum
		from employee
		group by dept_code
		with rollup ) as sum_salary ;
        
-- Q2. 서브쿼리를 이용하여 영업부인 직원들의 사원번호, 직원명, 부서코드, 급여를 출력하세요.
-- 참고. 영업부인 직원은 부서명에 ‘영업’이 포함된 직원임
select emp_id, emp_name, dept_code, salary
from (
		select *
        from employee 
        where 