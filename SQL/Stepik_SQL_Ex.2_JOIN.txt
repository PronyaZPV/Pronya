/*
Таблица genre:
+----------+-------------+
| genre_id | name_genre  |
+----------+-------------+
| 1        | Роман       |
| 2        | Поэзия      |
| 3        | Приключения |
+----------+-------------+

Таблица author:
+-----------+------------------+
| author_id | name_author      |
+-----------+------------------+
| 1         | Булгаков М.А.    |
| 2         | Достоевский Ф.М. |
| 3         | Есенин С.А.      |
| 4         | Пастернак Б.Л.   |
| 5         | Лермонтов М.Ю.   |
+-----------+------------------+

Таблица book:
+---------+-----------------------+-----------+----------+--------+--------+
| book_id | title                 | author_id | genre_id | price  | amount |
+---------+-----------------------+-----------+----------+--------+--------+
| 1       | Мастер и Маргарита    | 1         | 1        | 670.99 | 3      |
| 2       | Белая гвардия         | 1         | 1        | 540.50 | 5      |
| 3       | Идиот                 | 2         | 1        | 460.00 | 10     |
| 4       | Братья Карамазовы     | 2         | 1        | 799.01 | 3      |
| 5       | Игрок                 | 2         | 1        | 480.50 | 10     |
| 6       | Стихотворения и поэмы | 3         | 2        | 650.00 | 15     |
| 7       | Черный человек        | 3         | 2        | 570.20 | 6      |
| 8       | Лирика                | 4         | 2        | 518.99 | 2      |
+---------+-----------------------+-----------+----------+--------+--------+

Таблица city:
+---------+-----------------+
| city_id | name_city       |
+---------+-----------------+
| 1       | Москва          |
| 2       | Санкт-Петербург |
| 3       | Владивосток     |
+---------+-----------------+

Таблица supply:
+-----------+----------------+------------------+--------+--------+
| supply_id | title          | author           | price  | amount |
+-----------+----------------+------------------+--------+--------+
| 1         | Доктор Живаго  | Пастернак Б.Л.   | 618.99 | 3      |
| 2         | Черный человек | Есенин С.А.      | 570.20 | 6      |
| 3         | Евгений Онегин | Пушкин А.С.      | 440.80 | 5      |
| 4         | Идиот          | Достоевский Ф.М. | 360.80 | 3      |
+-----------+----------------+------------------+--------+--------+
*/

-- Вывести название, жанр и цену тех книг, количество которых больше 8, в отсортированном по убыванию цены виде.
SELECT title, name_genre, price FROM book 
INNER JOIN genre USING(genre_id)
WHERE amount > 8
ORDER BY price DESC

-- Вывести все жанры, которые не представлены в книгах на складе.
SELECT name_genre FROM genre 
LEFT JOIN book USING(genre_id) 
WHERE title IS NULL

-- Другое решение без JOIN
SELECT name_genre FROM genre 
WHERE genre.genre_id NOT IN(SELECT genre_id FROM book)

-- Необходимо в каждом городе провести выставку книг каждого автора в течение 2020 года. Дату проведения выставки выбрать случайным образом. 
-- Создать запрос, который выведет город, автора и дату проведения выставки. Последний столбец назвать Дата. 
-- Информацию вывести, отсортировав сначала в алфавитном порядке по названиям городов, а потом по убыванию дат проведения выставок.
SELECT name_city, name_author,
    DATE_ADD('2020-01-01', INTERVAL FLOOR(RAND()*365) DAY) AS Дата -- добавили случайную дату в году, FLOOR-округлили до целого
FROM author CROSS JOIN city
ORDER BY name_city, Дата DESC

-- Вывести информацию о книгах (жанр, книга, автор), относящихся к жанру, включающему слово «роман» в отсортированном по названиям книг виде.
SELECT name_genre, title, name_author FROM book 
    JOIN genre USING(genre_id)
    JOIN author USING(author_id)
WHERE name_genre = 'Роман'
ORDER BY title

-- Посчитать количество экземпляров  книг каждого автора из таблицы author.  Вывести тех авторов,  количество книг которых меньше 10, в отсортированном по возрастанию количества виде. Последний столбец назвать Количество.
SELECT name_author, SUM(amount) AS Количество
FROM author LEFT JOIN book USING(author_id)
GROUP BY name_author
HAVING SUM(amount) < 10 OR COUNT(title) = 0
ORDER BY Количество;

-- Вывести в алфавитном порядке всех авторов, которые пишут только в одном жанре. Поскольку у нас в таблицах так занесены данные, что у каждого автора книги только в одном жанре,  для этого запроса внесем изменения в таблицу book. 
-- Пусть у нас  книга Есенина «Черный человек» относится к жанру «Роман», а книга Булгакова «Белая гвардия» к «Приключениям» (эти изменения в таблицы уже внесены).
SELECT name_author FROM 
    (SELECT author_id, COUNT(DISTINCT genre_id) AS genre_sum FROM book GROUP BY author_id) interim
JOIN author USING(author_id)
WHERE genre_sum = 1

-- Решение проще, без вложения
SELECT name_author FROM author 
JOIN book USING(author_id)
GROUP BY name_author
HAVING count(DISTINCT genre_id) = 1;

-- Вывести информацию о книгах (название книги, фамилию и инициалы автора, название жанра, цену и количество экземпляров книг), написанных в самых популярных жанрах, в отсортированном в алфавитном порядке по названию книг виде. 
-- Самым популярным считать жанр, общее количество экземпляров книг которого на складе максимально.
SELECT  title, name_author, name_genre, price, amount
FROM author 
    INNER JOIN book USING(author_id)
    INNER JOIN genre USING(genre_id)
WHERE genre.genre_id IN
         (SELECT query_in_1.genre_id FROM 
              (SELECT genre_id, SUM(amount) AS sum_amount FROM book
                GROUP BY genre_id
               )query_in_1
          JOIN 
              (SELECT genre_id, SUM(amount) AS sum_amount FROM book
                GROUP BY genre_id
                ORDER BY sum_amount DESC
                LIMIT 1
               ) query_in_2
          ON query_in_1.sum_amount = query_in_2.sum_amount
         )
ORDER BY title;

-- Другое решение
SELECT title, name_author, name_genre, price, amount
FROM genre 
    JOIN book USING(genre_id)
    JOIN author USING(author_id)
WHERE genre_id IN (
    SELECT genre_id FROM book GROUP BY genre_id
    HAVING SUM(amount) = (
        SELECT SUM(amount) AS sum_amount FROM book
        GROUP BY genre_id
        ORDER BY sum_amount DESC
        LIMIT 1))
ORDER BY title;

-- Если в таблицах supply  и book есть одинаковые книги, которые имеют равную цену,  вывести их название и автора, а также посчитать общее количество экземпляров книг в таблицах supply и book,  столбцы назвать Название, Автор  и Количество
SELECT book.title AS Название, name_author AS Автор, (book.amount + supply.amount) AS Количество
FROM book 
    INNER JOIN author USING (author_id)   
    INNER JOIN supply 
    ON (book.title, author.name_author, book.price) = (supply.title, supply.author, supply.price)

-- Для каждого автора из таблицы author вывести количество книг, написанных им в каждом жанре. Вывести ФИО автора, жанр, количество.
-- Отсортировать по фамилии, затем - по убыванию количества написанных книг, а затем в алфавитном порядке по названию жанра.
SELECT name_author, name_genre, COUNT(title) AS Количество
FROM author CROSS JOIN genre
            LEFT JOIN book USING(author_id,genre_id)      
GROUP BY name_genre, name_author
ORDER BY name_author, Количество DESC, name_genre