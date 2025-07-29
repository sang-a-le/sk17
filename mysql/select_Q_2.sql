-- Q1. 재직 중이고 휴대폰 마지막 자리가 2인 직원 중 입사일이 가장 최근인 직원 3명의 사원번호, 직원명, 전화번호, 입사일, 퇴직여부를 출력하세요.
-- - 참고. 퇴사한 직원은 퇴직여부 컬럼값이 ‘Y’이고, 재직 중인 직원의 퇴직여부 컬럼값은 ‘N’
use employeedb ;
select * from employee ;

select emp_id, emp_name, phone, hire_date, ent_yn
  from employee
  where phone like '%2' and ent_yn = 'N'
  order by hire_date desc 
  limit 3 ; 
  
-- Q2. 재직 중인 ‘대리’들의 직원명, 직급명, 급여, 사원번호, 이메일, 전화번호, 입사일을 출력하세요.
-- 단, 급여를 기준으로 내림차순 출력하세요.
select * from job ;
select * from employee ;

select e.emp_name, j.job_name, e.salary, e.emp_id, e.email, e.phone, e.hire_date as data_q2                
  from employee e
  left join job j using (job_code)
  order by e.salary ;
  
-- Q3. 재직 중인 직원들을 대상으로 부서별 인원, 급여 합계, 급여 평균을 출력하고, 마지막에는 전체 인원과 전체 직원의 급여 합계 및 평균이 출력되도록 하세요.
-- 단, 출력되는 데이터의 헤더는 컬럼명이 아닌 ‘부서명’, ‘인원’, ‘급여합계’, ‘급여평균’으로 출력되도록 하세요.
select * from department ;
select * from employee ;

select d.dept_title as '부서명', count(e.emp_id) as '인원' , sum(e.salary) as '그룹합계', avg(e.salary) as '급여평균'
  from employee e 
  left join department d on e.dept_code = d.dept_id
  group by d.dept_title 
  with rollup ;
  
-- Q4. 전체 직원의 직원명, 주민등록번호, 전화번호, 부서명, 직급명을 출력하세요.
-- 단, 입사일을 기준으로 오름차순 정렬되도록 출력하세요.
select * from employee ;
select * from department ;
select * from job ;

select e.emp_name, e.emp_no, e.phone, d.dept_title, j.job_name
  from employee e 
  left join department d on e.dept_code = d.dept_id 
  left join job j on e.job_code = j.job_code
  order by e.hire_date ; 
  
-- Q5. <1단계> 전체 직원 중 연결된 관리자가 있는 직원의 인원을 출력하세요.
-- 참고. 연결된 관리자가 있다는 것은 관리자사번이 NULL이 아님을 의미함
