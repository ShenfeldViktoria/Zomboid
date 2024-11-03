import csv

class ReaderFile:
    """
    Клас ReaderFile відповідає за зчитування CSV-файлів та повернення даних
    у вигляді списку словників, де кожен словник представляє рядок CSV-файлу.
    """
    def read_csv(self, file_path):
        """
        Зчитує CSV-файл за вказаним шляхом і повертає дані у вигляді списку словників.

        Параметри:
            file_path (str): Шлях до CSV-файлу.

        Повертає:
            list[dict]: Список рядків файлу, представлених як словники.
                        Ключі - це назви колонок, значення - дані в комірках.
        """
        with open(file_path) as file:
            reader = csv.DictReader(file)
            return list(reader)

class CSVSurvivorItems:
    """
    Основний клас для роботи з предметами виживальника з CSV-файлу.
    Дозволяє завантажувати дані, фільтрувати їх та виводити на екран.

    Атрибути:
        file_path (str): Шлях до CSV-файлу з даними.
        items (list): Список предметів, завантажених з файлу.
        reader (ReaderFile): Об'єкт для зчитування CSV-файлу.
        ItemManager (ItemManager): Вкладений клас для керування предметами.
    """
    def __init__(self, file_path):
        """
        Ініціалізація об'єкта CSVSurvivorItems.

        Параметри:
            file_path (str): Шлях до CSV-файлу з даними.
        """
        self.file_path = file_path
        self.items = []  # Список для зберігання всіх предметів після завантаження
        self.reader = ReaderFile()  # Створюємо об'єкт для зчитування CSV
        self.ItemManager = self.ItemManager(self)  # Створюємо об'єкт для керування предметами

    class ItemManager:
        """
        Вкладений клас для керування предметами: завантаження, пошук за ID та за ім'ям.
        Дозволяє обробляти дані та фільтрувати їх за критеріями.
        """
        def __init__(self, csv_survivor):
            """
            Ініціалізація об'єкта ItemManager.

            Параметри:
                csv_survivor (CSVSurvivorItems): Зовнішній об'єкт CSVSurvivorItems для доступу до його даних.
            """
            self.csv_survivor = csv_survivor

        def load_items(self):
            """
            Завантажує всі предмети з CSV-файлу та зберігає їх в атрибут items
            зовнішнього об'єкта CSVSurvivorItems. Дублікати рядків не видаляються.
            """
            self.csv_survivor.items = self.csv_survivor.reader.read_csv(self.csv_survivor.file_path)

        def get_item_by_id(self, item_id):
            """
            Шукає предмети за вказаним ID.

            Параметри:
                item_id (str): Ідентифікатор предмета для пошуку.

            Повертає:
                list[dict]: Список всіх предметів з вказаним ID.
            """
            return [item for item in self.csv_survivor.items if item['ID'] == str(item_id)]

        def search_by_name(self, name):
            """
            Виконує пошук предметів за назвою.

            Параметри:
                name (str): Назва або частина назви предмета для пошуку.

            Повертає:
                list[dict]: Список всіх предметів, які містять вказану назву або її частину.
            """
            return [item for item in self.csv_survivor.items if name.lower() in item['Name'].lower()]

    def display_items(self, page_size=10, page_number=1, filter_by=None, filter_value=None):
        """
        Виводить предмети посторінково з можливістю фільтрації за ID або назвою.

        Параметри:
            page_size (int): Кількість предметів на сторінці (за замовчуванням 10).
            page_number (int): Номер сторінки для відображення.
            filter_by (str): Поле для фільтрації ('ID' або 'Name').
            filter_value (str): Значення для фільтрації (наприклад, '2' для ID або 'Nails' для Name).
        """
        
        # Фільтрація предметів, якщо задані критерії
        if filter_by and filter_value:
            items_to_display = [
                item for item in self.items
                if str(item.get(filter_by, "")).lower() == str(filter_value).lower()
            ]
        else:
            # Визначаємо діапазон даних для відображення на вказаній сторінці
            start = (page_number - 1) * page_size
            end = start + page_size
            items_to_display = self.items[start:end]
        
        if items_to_display:
            # Налаштування ширини колонок для форматованого виводу
            column_widths = {
                'ID': 5,
                'Name': 20,
                'Type': 15,
                'Condition': 10,
                'Amount': 7
            }
            
            # Друк заголовків таблиці
            header = f"{'ID'.ljust(column_widths['ID'])} | {'Name'.ljust(column_widths['Name'])} | {'Type'.ljust(column_widths['Type'])} | {'Condition'.ljust(column_widths['Condition'])} | {'Amount'.ljust(column_widths['Amount'])}"
            print(header)
            print('-' * len(header))

            # Друк рядків з даними
            for item in items_to_display:
                row = f"{item['ID'].ljust(column_widths['ID'])} | {item['Name'].ljust(column_widths['Name'])} | {item['Type'].ljust(column_widths['Type'])} | {item['Condition'].ljust(column_widths['Condition'])} | {item['Amount'].ljust(column_widths['Amount'])}"
                print(row)
        else:
            print("Немає предметів для відображення за заданими критеріями.")

# Приклад використання програми
file_path = 'items.csv'
csv_items = CSVSurvivorItems(file_path)

# Завантажуємо предмети з файлу
csv_items.ItemManager.load_items()

# Виводимо предмети з фільтрацією за ID
csv_items.display_items(filter_by='ID', filter_value='2')

# Виводимо предмети з фільтрацією за назвою
csv_items.display_items(filter_by='Name', filter_value='Nails')

# Виводимо предмети посторінково (без фільтрації)
csv_items.display_items(page_size=10, page_number=1)
