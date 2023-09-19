# mindbox_tasks
Задание на стажировку.
## Задание 1. 
Напишите на C# или Python библиотеку для поставки внешним клиентам, которая умеет вычислять площадь круга по радиусу и треугольника по трем сторонам. Дополнительно к работоспособности оценим:
* Юнит-тесты
* Легкость добавления других фигур
* Вычисление площади фигуры без знания типа фигуры в compile-time
* Проверку на то, является ли треугольник прямоугольным
Решение:
1. Нахождение площади круга по радиусу:\
<code>circle = Circle(10) # Задание радиуса\
circle.area() # Возвращает площадь круга</code>
2. Нахождение площади треугольника по трём сторонам:\
<code>triangle = Triangle(3, 5, 4) # Задание сторон
triangle.area() # Возвращает площадь треугольника</code>\
3. Является ли треугольник прямоугольным:\
<code>triangle.is_rectangular()</code>
## Задание 2.
В датафреймах (pyspark.sql.DataFrame) заданы продукты, категории и связь между ними. Одному продукту может соответствовать много категорий, в одной категории может быть много продуктов. Напишите метод с помощью PySpark, который вернет все продукты с их категориями (датафрейм с набором всех пар «Имя продукта – Имя категории»). В результирующем датафрейме должны также присутствовать продукты, у которых нет категорий.

Решение:

Пусть даны таблицы:

Таблица продуктов (название, идентификатор)
|       name| id|
|-----------|---|
|     'milk'|  0|
|'chocolate'|  1|
|      'car'|  2|
|   'cheese'|  3|

Таблица категорий (категория, идентификатор)
|name_id|category_id|
|-------|-----------|
|      0|          0|
|      1|          1|
|      1|          2|
|      2|       null|
|      3|          0|
|      3|          3|

