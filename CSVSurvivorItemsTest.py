import unittest
from io import StringIO
import csv
from Zomboid import CSVReader, ItemManager

class TestCSVReader(unittest.TestCase):
    def setUp(self):
        self.test_csv_data = StringIO("""ID,Name,Type,Condition,Amount
1,Hammer,Tool,Mint,10
2,Nails,Fasteners,Good,450
3,Bat,Weapon,Bad,2
4,Bulb,Fasteners,Good,15""")
        self.reader = CSVReader()

    def test_load_items(self):
        with open("test_items.csv", "w") as f:
            f.write(self.test_csv_data.getvalue())
        
        items = self.reader.load_items("test_items.csv")
        
        self.assertEqual(len(items), 4)
        self.assertEqual(items[0]["Name"], "Hammer")
        self.assertEqual(items[1]["Condition"], "Good")


class TestItemManager(unittest.TestCase):
    def setUp(self):
        self.test_items = [
            {"ID": "1", "Name": "Hammer", "Type": "Tool", "Condition": "Mint", "Amount": "10"},
            {"ID": "2", "Name": "Nails", "Type": "Fasteners", "Condition": "Good", "Amount": "450"},
            {"ID": "3", "Name": "Bat", "Type": "Weapon", "Condition": "Bad", "Amount": "2"},
            {"ID": "4", "Name": "Bulb", "Type": "Fasteners", "Condition": "Good", "Amount": "15"},
        ]
        self.manager = ItemManager(self.test_items)

    def test_get_item_by_id(self):
        item = self.manager.get_item_by_id("2")
        self.assertEqual(item["Name"], "Nails")

    def test_search_by_name(self):
        items = self.manager.search_by_name("Bulb")
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["Type"], "Fasteners")

    def test_calculate_condition_percentage(self):
        percentages = self.manager.calculate_condition_percentage()
        self.assertAlmostEqual(percentages["Mint"], 25.0)
        self.assertAlmostEqual(percentages["Good"], 50.0)
        self.assertAlmostEqual(percentages["Bad"], 25.0)

if __name__ == "__main__":
    unittest.main()
