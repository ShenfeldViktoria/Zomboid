import csv
import pdb  # For debugging

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
        items = []  # List to store items
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)  # Read the CSV as a dictionary
            for row in reader:
                items.append(row)  # Append each row to the items list
        return items  # Return the list of items


class ItemManager:
    """
    A class to manage items loaded from a file.
    Provides functionality to get items by ID, search by name, 
    and display paginated results.
    """

    def __init__(self, items=None):
        """
        Initialize the ItemManager with a list of items.

        Parameters:
        - items (list): List of item dictionaries.
        """
        self.items = items if items is not None else []  # Initialize items or set to an empty list

    def get_item_by_id(self, item_id: str) -> dict:
        """
        Retrieve an item by its ID.

        Parameters:
        - item_id (str): The ID of the item.

        Returns:
        - dict: The item with the specified ID, or None if not found.
        """
        return next((item for item in self.items if item['ID'] == item_id), None)  # Search for item by ID

    def search_by_name(self, name: str) -> list:
        """
        Search items by name.

        Parameters:
        - name (str): The name of the item to search for.

        Returns:
        - list: List of items that match the given name.
        """
        return [item for item in self.items if item['Name'].lower() == name.lower()]  # Case-insensitive search by name

    def display_items(self, page_size: int = 10, page_number: int = 1) -> None:
        """
        Display items in a paginated format.

        Parameters:
        - page_size (int): Number of items per page.
        - page_number (int): The page number to display.

        Returns:
        - None
        """
        start = (page_number - 1) * page_size  # Calculate the start index for pagination
        end = start + page_size  # Calculate the end index for pagination
        items_to_display = self.items[start:end]  # Get the items for the current page

        if not items_to_display:
            print("No items to display.")  # If no items to display, print a message
            return

        # Define column widths for neat display
        column_widths = {
            'ID': 5,
            'Name': 15,
            'Type': 12,
            'Condition': 10,
            'Amount': 8
        }

        # Print the header row with column names
        headers = list(self.items[0].keys())  # Get the headers from the first item
        header_row = " | ".join(f"{header:<{column_widths[header]}}" for header in headers)
        print(header_row)
        print("-" * len(header_row))  # Print a line separating header and items

        # Print each item on a new row, formatted according to column widths
        for item in items_to_display:
            row = " | ".join(f"{item[key]:<{column_widths[key]}}" for key in headers)
            print(row)

        print(f"Page {page_number}")  # Indicate the current page number

    def calculate_condition_percentage(self):
        """
        Calculate the percentage of items by their condition.

        Returns:
        - dict: Dictionary with the percentage of each condition.
        """
        condition_counts = {'Mint': 0, 'Good': 0, 'Average': 0, 'Bad': 0}  # Initialize counters for conditions
        total_items = len(self.items)  # Get the total number of items

        for item in self.items:
            condition = item['Condition']
            if condition in condition_counts:
                condition_counts[condition] += 1  # Count items per condition

        # Calculate percentage for each condition
        percentages = {condition: (count / total_items) * 100 for condition, count in condition_counts.items()}
        return percentages  # Return the percentage distribution

    def calculate_condition_percentage_by_name(self, name: str):
        """
        Calculate the percentage of items by their condition for a specific name.

        Parameters:
        - name (str): The name of the items to filter by.

        Returns:
        - dict: Dictionary with the percentage of each condition for the specified name.
        """
        filtered_items = [item for item in self.items if item['Name'].lower() == name.lower()]  # Filter by name
        total_items = len(filtered_items)  # Get the total number of filtered items
        
        if total_items == 0:
            return {}  # Return an empty dictionary if no items were found for the given name

        condition_counts = {'Mint': 0, 'Good': 0, 'Average': 0, 'Bad': 0}  # Initialize counters for conditions
        for item in filtered_items:
            condition = item['Condition']
            if condition in condition_counts:
                condition_counts[condition] += 1  # Count items per condition

        # Calculate percentage for each condition
        percentages = {condition: (count / total_items) * 100 for condition, count in condition_counts.items()}
        return percentages  # Return the percentage distribution for the filtered items


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
        self.reader = CSVReader()  # Create an instance of CSVReader to load items
        self.items = self.reader.load_items(file_path)  # Load items from the CSV file
        self.manager = ItemManager(self.items)  # Create an instance of ItemManager to manage the loaded items


def main():
    """
    The main function to parse command-line arguments and execute the appropriate methods.
    """
    print("Program starting...")  # Inform the user that the program is starting
    import argparse
    parser = argparse.ArgumentParser(description="CLI for managing items from a CSV file.")
    parser.add_argument("file_path", help="Path to the CSV file.")  # Argument for the CSV file path
    parser.add_argument("--get-item", help="Retrieve item by ID.", type=str)  # Retrieve an item by its ID
    parser.add_argument("--search-name", help="Search items by name.", type=str)  # Search for items by name
    parser.add_argument("--display", help="Display items (provide page size and number).", nargs=2, type=int)  # Display paginated items
    parser.add_argument("--condition-percentage", help="Show percentage by condition.", action="store_true")  # Show condition percentages
    parser.add_argument("--condition-percentage-name", help="Show percentage by condition for a specific name.", type=str)  # Show condition percentages for a specific name

    try:
        args = parser.parse_args()  # Parse command-line arguments
    except SystemExit as e:
        print(f"Error: {e}")  # If an error occurs, print the error and show the help message
        parser.print_help()  # Show the help message
        return

    # Initialize the CSVSurvivorItems with the provided file path
    csv_items = CSVSurvivorItems(args.file_path)

    # Check each argument and execute the corresponding method
    if args.get_item:
        item = csv_items.manager.get_item_by_id(args.get_item)
        print(f"\nItem with ID {args.get_item}: {item}")

    if args.search_name:
        items = csv_items.manager.search_by_name(args.search_name)
        print(f"\nItems with name '{args.search_name}':")
        for item in items:
            print(item)

    if args.display:
        page_size, page_number = args.display
        print(f"\nDisplaying page {page_number}:")
        csv_items.manager.display_items(page_size=page_size, page_number=page_number)

    if args.condition_percentage:
        percentages = csv_items.manager.calculate_condition_percentage()
        print("\nPercentage distribution by condition for all items:")
        for condition, percent in percentages.items():
            print(f"{condition} — {percent:.2f}%")

    if args.condition_percentage_name:
        percentages = csv_items.manager.calculate_condition_percentage_by_name(args.condition_percentage_name)
        print(f"\nPercentage distribution by condition for items named '{args.condition_percentage_name}':")
        for condition, percent in percentages.items():
            print(f"{condition} — {percent:.2f}%")


if __name__ == "__main__":
    main()  # Run the main function
