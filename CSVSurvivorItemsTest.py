import unittest
from Zomboid import CSVSurvivorItems, ItemManager

class TestCSVSurvivorItems(unittest.TestCase):
    def setUp(self):
        self.csv_items = CSVSurvivorItems('items.csv')

    def test_get_item_by_id(self):
        item = self.csv_items.manager.get_item_by_id('1')
        self.assertIsNotNone(item)
        self.assertEqual(item['ID'], '1')

    def test_search_by_name(self):
        results = self.csv_items.manager.search_by_name('Nails')
        self.assertTrue(any(item['Name'] == 'Nails' for item in results))

if __name__ == "__main__":
    unittest.main()
