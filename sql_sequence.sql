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
--题目 1：查询姓名为 "Tom" 的学生信息
--表名：students
--字段：id, name, age, gender, grade
select *
from students s
where s.name='Tom'
----题目 2：查询年龄大于 18 岁的所有学生，并按年龄降序排列
--表名：students
select id,name,age
from students s
where s.age>18
order by age desc
--题目 3：查询所有不重复的年级（grade）
--表名：students
select grade
from students s 
group by grade
having count(grade)=1
--题目 4：查询每个年级的学生人数
--表名：students
select count(*) as student_count
from students s 
group by grade

--题目 5：查询学生人数最多的年级
--提示：可以使用 GROUP BY + ORDER BY 或子查询
select grade
from students
group by grade
order by count(*) desc
limit 1
--题目 6：查询所有成绩高于年级平均成绩的学生
--表名：scores
--字段：student_id, subject, score, grade
select id,name,score
from students s 
left join scores sc 
    on s.id=sc.student_id
where score>(
    select avg(score)
    from scores sc
    where grade = s.grade
)

--表名：employees  
--字段：id (INT), name (VARCHAR), salary (DECIMAL)
--查询 employees 表中所有工资大于 5000 的员工姓名和工资
select name,salary
from employees e 
where salary>5000
--表名：students  
--字段：id (INT), name (VARCHAR), score (INT)
--查询 students 表中成绩最高的前 3 名学生信息
select id,name,score
from students s 
order by score desc
limit 3
--表名：products  
--字段：id (INT), name (VARCHAR), price (DECIMAL)
--向 products 表中插入一个新商品，名称为 "iPhone 99"，价格为 9999。
insert into products(name,price)
values("iPhone 99", 9999)
--表名：orders  
--字段：id (INT), user_id (INT), status (VARCHAR), total (DECIMAL)
--将 orders 表中所有状态为 "pending" 的订单状态改为 "completed"
update orders
set status='completed'
where status='pending'
--表名：orders (id, user_id, total_amount)  
--表名：users (id, name, email)
--查询订单表 orders 和用户表 users，找出每个订单对应的用户名和订单金额
select u.name,o.total_amount
from users u 
left join orders o
    on u.id=o.id
--表名：sales  
--字段：id (INT), product_id (INT), quantity (INT), sale_date (DATE)
--查询 sales 表中各产品的总销量（按 product_id 分组）
select count(quantity) as total_quantity
from sales
group by product_id
--表名：employees  
--字段：id (INT), name (VARCHAR), salary (DECIMAL)
--查询工资高于全公司平均工资的员工姓名。
select name,salary
from employees e 
where salary>(
    select avg(salary) as avg_salary
    from employees e
)
--表名：orders (id, user_id, order_date)  
--表名：order_items (id, order_id, product_id, quantity)  
--表名：users (id, name)
--查询至少购买过一次商品编号为 101 的所有用户信息
select id,name
from users u 
join orders o
    on u.id=o.users_id
join orders_items os 
    on o.id=order_id
where 101 in os.product_id
--有一个名为 employee 的表，包含字段 id 和 salary，请写出 SQL 查询第二高的薪水（若没有则返回 NULL）。

-- 示例数据:
-- id | salary
-- 1  | 5000
-- 2  | 8000
-- 3  | 5000
-- 4  | 10000
-- 输出: 8000
select distinct salary
from employee e
order by salary desc
limit 1,1
--有两个表：

    --employee(id, name, dept_id)

    --department(id, dept_name)

--请查询每个部门的员工数量（包括没有人的部门也要显示）。
select count(*) as total_count
from department d 
left join employee e 
    on d.id=e.dept_id
group by d.id