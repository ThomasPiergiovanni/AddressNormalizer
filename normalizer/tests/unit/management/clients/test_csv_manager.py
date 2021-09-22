"""Test csv manager module.
"""
from django.test import TestCase

from normalizer.management.clients.csv_manager import CsvManager


class CsvManagerTest(TestCase):
    """Test csv manager class.
    """
    def setUp(self):
        self.manager = CsvManager()
    
    def test_import_data_with_source_file(self):
        self.manager.import_data()
        self.assertEqual (self.manager.imported_data[1][0], '1')
        self.assertEqual (
            self.manager.imported_data[2][1], '65 rue des Bas Rogers'
        )