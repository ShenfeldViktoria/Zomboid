# Zomboid
*Бібліотека CSV Survivor Items*
Бібліотека для роботи з CSV-файлами, розроблена для виживальників, щоб ефективно керувати списками необхідних предметів. Дозволяє завантажувати дані з CSV-файлів, шукати предмети за ID та іменем, а також виводити їх посторінково з можливістю фільтрації.

# Функціональність:
1)Читання CSV-файлів з предметами.

2)Пошук предметів за ID та іменем.

3)Посторінковий вивід даних з можливістю фільтрації за ID та іменем.

# Структура CSV-файлу:
CSV-файл повинен мати наступні колонки:
| ID | Name    | Type       | Condition | Amount |
|----|---------|------------|-----------|--------|
| 1  | Hummer  | Tool       | Mint      | 10     |
| 2  | Nails   | Fasteners  | Good      | 450    |
| 3  | Bat     | Weapon     | Bad       | 2      |
| 4  | Bulb    | Fasteners  | Good      | 15     |
# Встановлення:
Для роботи з бібліотекою потрібен Python версії 3.6 або вище.

Завантажте код проєкту.
Переконайтесь, що файл *items.csv* знаходиться в одній папці з проєктом або вкажіть шлях до файлу в коді.

# Використання:
1)Імпортуйте та створіть екземпляр класу CSVSurvivorItems, передавши шлях до CSV-файлу:
                 -python-
*csv_items = CSVSurvivorItems('items.csv')*

2)Завантажте дані:
                 -python-
csv_items.ItemManager.load_items()

3)Виконайте вивід, пошук або фільтрацію:

*Посторінковий вивід (по 10 записів):*
```python
csv_items.display_items(page_size=10, page_number=1) 
```
*Фільтрація за ID:*
```python
csv_items.display_items(filter_by='ID', filter_value='2')
```
*Фільтрація за ім'ям:*
```python
csv_items.display_items(filter_by='Name', filter_value='Nails')
```
# Приклади використання:
Вивід предметів посторінково:
```python
csv_items.display_items(page_size=5, page_number=1)
```
Пошук предмета за ID:
```python
items = csv_items.ItemManager.get_item_by_id('1')
print(items)
```
Пошук предмета за ім'ям:
```python
items = csv_items.ItemManager.search_by_name('Nails')
print(items)
```
# Вимоги
 -Python 3.6+
 -Модуль csv (вбудований в стандартну бібліотеку Python)

# Автор
[Шенфельд Вікторія Денисівна]
