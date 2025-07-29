create user ohgiraffers@'%' identified by 'ohgiraffers';

create database menudb;
create database employeedb;

show databases;

grant all privileges on menudb.* to ohgiraffers@'%';
grant all privileges on employeedb.* to ohgiraffers@'%';

show grants for ohgiraffers@'%';