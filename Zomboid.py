import csv


class CSVReader:
    """
    A class to read items from a CSV file.
    """

    def load_items(self, file_path: str) -> list:
        """
        Load items from a CSV file and return a list of dictionaries.

        Parameters:
        - file_path (str): Path to the CSV file.

        Returns:
        - list of dict: List of item dictionaries.
        """
        items = []
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                items.append(row)
        return items


class ItemManager:
    """
    A class to manage items loaded from a file.
    Provides functionality to get items by ID, search by name, 
    and display paginated results.
    """

    def __init__(self, items=None):
        self.items = items if items is not None else []

    def get_item_by_id(self, item_id: str) -> dict:
        """
        Retrieve an item by its ID.

        Parameters:
        - item_id (str): The ID of the item.

        Returns:
        - dict: The item with the specified ID, or None if not found.
        """
        return next((item for item in self.items if item['ID'] == item_id), None)

    def search_by_name(self, name: str) -> list:
        """
        Search items by name.

        Parameters:
        - name (str): The name of the item to search.

        Returns:
        - list: List of items that match the given name.
        """
        return [item for item in self.items if item['Name'].lower() == name.lower()]

    def display_items(self, page_size: int = 10, page_number: int = 1) -> None:
        """
        Display items in a paginated format.

        Parameters:
        - page_size (int): Number of items per page.
        - page_number (int): The page number to display.

        Returns:
        - None
        """
        start = (page_number - 1) * page_size
        end = start + page_size
        items_to_display = self.items[start:end]

        if not items_to_display:
            print("No items to display.")
            return

        # Define column widths
        column_widths = {
            'ID': 5,
            'Name': 15,
            'Type': 12,
            'Condition': 10,
            'Amount': 8
        }

        # Print headers
        headers = list(self.items[0].keys())
        header_row = " | ".join(f"{header:<{column_widths[header]}}" for header in headers)
        print(header_row)
        print("-" * len(header_row))

        # Print each item in a formatted row
        for item in items_to_display:
            row = " | ".join(f"{item[key]:<{column_widths[key]}}" for key in headers)
            print(row)

        print(f"Page {page_number}")


class CSVSurvivorItems:
    """
    Main class to manage loading and accessing items from a CSV file.
    """

    def __init__(self, file_path: str):
        """
        Initialize the CSVSurvivorItems with a file path.

        Parameters:
        - file_path (str): Path to the CSV file containing items.
        """
        self.reader = CSVReader()
        self.items = self.reader.load_items(file_path)
        self.manager = ItemManager(self.items)


# Example usage of the program
if __name__ == "__main__":
    # Initialize the CSVSurvivorItems with a path to a CSV file
    csv_items = CSVSurvivorItems('items.csv')

    # Display items in pages
    print("Displaying page 1:")
    csv_items.manager.display_items(page_size=5, page_number=1)

    # Retrieve an item by ID
    item = csv_items.manager.get_item_by_id('1')
    print("\nItem with ID 1:", item)

    # Search for items by name
    nails = csv_items.manager.search_by_name('Nails')
    print("\nItems with name 'Nails':")
    for nail in nails:
        print(nail)
