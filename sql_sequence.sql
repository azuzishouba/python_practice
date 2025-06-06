CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    department_id INT,
    salary DECIMAL(10,2),
    hire_date DATE
);

CREATE TABLE departments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100)
);

CREATE TABLE projects (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    employee_id INT
);
--查询所有员工的姓名和工资
select *
from employees
--查询工资高于 8000 的员工信息
select name,salary,hire_date
from employees
where salary>8000
--查询在 2022 年之后入职的员工
select name,salary,hire_date
from employees
where hire_date>2022
--查询姓名中包含字母 'a' 的员工
select name,salary
from employees
where name REGEXP 'a'
--将所有员工按工资从高到低排序
select name,salary
from employees
order by salary desc
--查询公司员工的平均工资
select avg(salary) as avg_salary
from employees
--按部门分组，统计每个部门的员工数量
select count(*) as employees_count
from employees
group by department_id
--查询工资最高的员工
select name,salary
from employees
order by salary desc
limit 1
--按部门分组，找出每个部门工资最高的员工（挑战！）
select name,salary,department_id
from employees e
where salary=(
    select max(salary)
    from employees
    where department_id=e.department_id
)
--查询每个员工所在的部门名称（员工表联 department）
select name,department_name
from employees e
left join department d
    on e.department_id=d.department_id
--查询参与项目的员工姓名和对应项目名称
select name,p.name
from employees e
join projects p
    on e.employee_id=p.employee_id
--查询没有参与任何项目的员工
select name,p.name
from employees e
left join projects p
    on e.employee_id=p.employee_id
where p.name is null
--查询工资高于公司平均工资的员工
select name,salary
from employees e
where salary>(
    select avg(salary)
    from employees
)
--查询每个部门中工资最高的员工
select name,salary
from employees e
where salary=(
    select max(salary)
    from employees e
    where department_id=e.department
)

Employee (
  Id INT,
  Name VARCHAR,
  Salary INT,
  DepartmentId INT
)

Department (
  Id INT,
  Name VARCHAR
)

--每个部门中薪水最高的员工（可能有多个）
select id,name,salary
from employee
where salary=(
    select max(salary)
    from employee e
    where e.employee_id=employee_id
)

Customers (
  CustomerId INT,
  Name VARCHAR
)

Orders (
  OrderId INT,
  CustomerId INT,
  Amount DECIMAL
)
--查找累计订单金额前 3 的客户
select CustomerId,name,sum(Amount) as total_amout
from Customers c
left join Orders o
    on c.CustomerId=o.CustomerId
group by CustomerId
order by total_amout desc
limit 3

--表 students(id, name) 与 scores(student_id, subject, score)。
--查询每个学生的语文成绩（subject = 'Chinese'），包括学生姓名。
select ss.id,ss.name,sc.subject,sc.score
from ss
left join sc
    on  pn ss.id=sc.student_id
where sc.subject='Chinese'

--表 sales(order_id, region, amount)
--按 region 分组，查询每个地区的订单总金额和订单数量。
select sum(amount)as total_amout,count(*) as order_amout
from sales
group by region

--表 employees(id, name, salary)
--查询所有工资高于公司平均工资的员工姓名和工资。
select id,name,salary
from employees 
where salary>(
    select avg(salary)
    from employees
)

--表 users(id, status) 与 logins(user_id, last_login)
--把 30 天内没有登录的用户状态改为 inactive。
update users
set status='inactive'
where id=(
    select u.id
    from users u
    join logins l
        on u.id=l.user_id
    where now() - l.last_login>30
)
| id | name    | age | department | salary |
| -- | ------- | --- | ---------- | ------ |
| 1  | Alice   | 30  | HR         | 8000   |
| 2  | Bob     | 24  | IT         | 10000  |
| 3  | Charlie | 29  | IT         | 9500   |
--表名：employees
--查询每个部门的平均工资，按平均工资降序排序。
select avg(salary) as avg_salary
from employees
group by department
order by avg_salary desc

题目 3:多表连接

表1:orders
order_id	customer_id	amount
101	1	300
102	2	500

表2:customers
id	name
1	John Doe
2	Jane Smith
查询每个订单的客户姓名和订单金额。

select o.id,c.name,amout
from orders o
left join customers c
    on o.customer_id=c.id

