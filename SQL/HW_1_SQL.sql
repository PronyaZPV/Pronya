-- 1. Создать две БД
create database base_2;
create database base_3;

-- 2. Показать все БД
show databases;

-- 3. Удалить одну БД
drop database base_3;

-- 4. Войти в БД
use base_2;

-- 5. Создать таблицу сотрудников с полями id(3 знака), имя(60 знаков), отдел(20 знаков), грейд, дата трудоустройства
create table employee (id int(3) primary key, name char(60), department char(20), grid char(6), date_of_employment date);

-- 6. Проверить параметры таблицы 
desc employee;

-- 7. Добавить 5 сотрудников в таблицу c разными датами трудоустройства, где есть два джуна
insert into employee values(1, "Ivan", "QA", "junior","2022-07-01");
insert into employee values(2, "Inna", "QA", "junior","2022-05-25");
insert into employee values(3, "Alex","programmer", "middle","2021-02-25");
insert into employee values(4, "Vadim","programmer", "senior","2017-02-25");
insert into employee values(5, "Sergo","analyst", "middle","2019-08-25");

-- 8. Показать итоговую таблицу
select * from employee;

-- 9. Удалить одного джуна
delete from employee where name="Ivan";

-- 10. Сделать джуна мидлом
update employee set grid="middle" where grid="junior" and  name="Inna";

-- 11. Удалить колонку с датой трудоустройства
alter table employee drop column date_of_employment;

-- 12. Добавить колоку с количеством детей у сотрудников и заполнить поля
alter table employee add column child int(2);
update employee set child=0 where id=2;
update employee set child=1 where id=3;
update employee set child=2 where id=4;
update employee set child=2 where id=5;

-- 13. Вывести вервые 3 строки
select * from employee limit 3;

-- 13. вывести имена всех мидлов
select name from employee where grid="middle";

-- 14. вывести имена и грид сотрудников, у которых есть дети
select name,grid from employee where child > 0;

-- 15. Добавить и заполнить после грейда колонку с датой рождения сотрудников
alter table employee add column bd date after grid;
update employee set bd="1990-02-05" where id=2;
update employee set bd="1999-02-05" where id=3;
update employee set bd="1986-05-20" where id=4;
update employee set bd="1987-03-03" where id=5;

-- 16. Вывести сотрудников возрастом 20-30 лет
select * from employee where date(bd) between "1992-08-01" and "2002-08-01";

-- 17. Отсортировать по алфавиту по имени
select * from employee order by name;

-- 18. Вывести среднее количество детей по сотрудникам
select avg(child) from employee;

-- 19. Вывести количество всех детей всех мидлов
select avg(child) from employee;