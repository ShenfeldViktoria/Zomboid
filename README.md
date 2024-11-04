# Zomboid

**CSV Survivor Items Library**

A library for working with CSV files, developed for survivors to efficiently manage lists of necessary items. This library enables loading data from CSV files, searching items by ID and name, and paginated output with filtering options.

## Features:
1. Reading item data from CSV files.
2. Searching items by ID and name.
3. Paginated data display with filtering options by ID and name.

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
Requires Python version 3.6 or above.

1. Download the project code.
2. Ensure that the `items.csv` file is in the same directory as the project, or specify its path in the code.

## Usage:
1. Import and create an instance of the `CSVSurvivorItems` class, passing in the path to the CSV file:
   ```python
   csv_items = CSVSurvivorItems('items.csv')

2)Load the data:
```python
csv_items.ItemManager.load_items()
```
3)Display, search, or filter the items:

Paginated display (10 records per page):
```python
csv_items.display_items(page_size=10, page_number=1) 
```
Filter by ID:
```python
csv_items.display_items(filter_by='ID', filter_value='2')
```
Filter by Name:
```python
csv_items.display_items(filter_by='Name', filter_value='Nails')
```
# Examples:
Display items in pages:
```python
csv_items.display_items(page_size=5, page_number=1)
```
Search for an item by ID:
```python
items = csv_items.ItemManager.get_item_by_id('1')
print(items)
```
Search for an item by name:
```python
items = csv_items.ItemManager.search_by_name('Nails')
print(items)
```
# Requirements:
-Python 3.6+
-csv module (part of Python's standard library)

# Author
Shenfeld Victoria Denisovna

```mermaid
classDiagram
    %% CSVSurvivorItems is the main class that uses composition and aggregation to manage items

    class CSVSurvivorItems {
        +ItemManager itemManager
        +load_data(file_path: str)
        +display_items(page_size: int, page_number: int, filter_by: str, filter_value: str)
    }

    %% CSVSurvivorItems contains an ItemManager instance using composition
    CSVSurvivorItems --> ItemManager : "composition"

    %% ItemManager uses CSVReader as a helper through aggregation
    class ItemManager {
        +get_item_by_id(item_id: str)
        +search_by_name(name: str)
        +display_items(page_size: int, page_number: int, filter_by: str, filter_value: str)
    }

    ItemManager o-- CSVReader : "aggregation"

    %% CSVReader class handles reading the CSV data independently
    class CSVReader {
        +load_items(file_path: str)
    }

    %% Composition relationship shown with a solid line and filled diamond
    %% Aggregation relationship shown with an open diamond

