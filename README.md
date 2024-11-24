# Zomboid

**CSV Survivor Items Library**

A library for managing survivor items from CSV files. This library allows for loading, searching, and displaying items with filtering and pagination, along with additional functionality for calculating condition percentages.

## Features:
1. Load item data from CSV files.
2. Search for items by ID and name.
3. Display items in a paginated format.
4. Calculate percentage distribution of items based on their condition (Mint, Good, Average, Bad).
5. Filter items by name and calculate condition percentage for a specific item name.

## CSV File Structure:
The CSV file should have the following columns:

| ID | Name   | Type      | Condition | Amount |
|----|--------|-----------|-----------|--------|
| 1  | Hummer | Tool      | Mint      | 10     |
| 2  | Nails  | Fasteners | Good      | 450    |
| 2  | Nails  | Fasteners | Bad       | 100    |
| 3  | Bat    | Weapon    | Bad       | 2      |
| 4  | Bulb   | Fasteners | Good      | 15     |

## Installation:
Prerequisites:
1.Python 3.6 or higher
2.A CSV file formatted as described in the CSV File Structure section.

## Usage:
Run the program from the command line using:
``` bash
python Zomboid.py <file_path> [OPTIONS]
```

## Arguments:
file_path (Required): Path to the CSV file containing items.

## Options:
1. --get-item <item_id>: Retrieve a single item by its ID.
2. --search-name <name>: Search for items with a specific name.
3. --display <page_size> <page_number>: Display items paginated by page_size and page_number.
4. --condition-percentage: Display the percentage distribution of items by their condition.
5. --condition-percentage-name <name>: Display the condition percentage distribution for items with a specific name.

## Example Usage:
1. Load a CSV File and Retrieve an Item by ID
``` bash
python Zomboid.py items.csv --get-item 1
```
Output :
``` markdown
Item with ID 1: {'ID': '1', 'Name': 'Hummer', 'Type': 'Tool', 'Condition': 'Mint', 'Amount': '10'}
```
2. Search for Items by Name
 ``` bash
python Zomboid.py items.csv --search-name "Nails"
```
Output :
``` markdown
Items with name 'Nails':
{'ID': '2', 'Name': 'Nails', 'Type': 'Fasteners', 'Condition': 'Good', 'Amount': '450'}
{'ID': '2', 'Name': 'Nails', 'Type': 'Fasteners', 'Condition': 'Bad', 'Amount': '100'}
```
3. Display Items Paginated
``` bash
python Zomboid.py items.csv --display 2 1
```
Output :
``` markdown
ID    | Name           | Type        | Condition | Amount
---------------------------------------------------------
1     | Hummer         | Tool        | Mint      | 10    
2     | Nails          | Fasteners   | Good      | 450   
Page 1
```
4. Analyze Item Conditions
``` bash
python Zomboid.py items.csv --condition-percentage
```
Output :
``` markdown
Percentage distribution by condition for all items:
Mint — 25.00%
Good — 50.00%
Bad — 25.00%
```
5. Analyze Conditions by Name
``` bash
python Zomboid.py items.csv --condition-percentage-name "Nails"
```
Output :
``` markdown
Percentage distribution by condition for items named 'Nails':
Good — 81.82%
Bad — 18.18%
```
## Error Handling
1. If the provided file_path is invalid or the file is not formatted correctly, the program will terminate with an error message.
2. Searches and calculations return appropriate messages if no matches are found.

## Future Enhancements
Adding support for other file formats, such as JSON, will not be a problem. The current architecture is modular, and additional file readers (e.g., JSONReader) can be easily integrated alongside the existing CSVReader. This ensures scalability and flexibility for future data handling requirements.

## Author 
Shenfeld Victoria Denisovna

``` mermaid
classDiagram
    class CSVReader {
        +load_items(file_path: str) list
    }

    class ItemManager {
        -items: list
        +__init__(items: list)
        +get_item_by_id(item_id: str) dict
        +search_by_name(name: str) list
        +display_items(page_size: int=10, page_number: int=1) void
        +calculate_condition_percentage() dict
        +calculate_condition_percentage_by_name(name: str) dict
    }

    class CSVSurvivorItems {
        -reader: CSVReader
        -items: list
        -manager: ItemManager
        +__init__(file_path: str)
    }

    CSVReader --> ItemManager : loads items
    CSVSurvivorItems --> CSVReader : uses
    CSVSurvivorItems --> ItemManager : manages
```
