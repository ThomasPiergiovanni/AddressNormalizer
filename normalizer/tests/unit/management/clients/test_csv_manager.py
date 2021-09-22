"""Test csv manager module.
"""
from django.test import TestCase

from normalizer.management.clients.csv_manager import CsvManager


class CsvManagerTest(TestCase):
    """Test csv manager class.
    """
    def setUp(self):
        self.manager = CsvManager()
    
    @classmethod
    def emulate_imported_data(cls):
        cls.imported_data = [
            ['id', 'adresse'],
            ['1', '12 rue Ledru-Rollin'],
            ['2', '65 rue des Bas Rogers'],
            ['46', '51 allée de la pépinière'],
            ['4', '28 rue victor hugo']
        ]
    
    def test_import_data_with_source_file(self):
        path_to_file = r'C:\02_dev\AddressNormalizer\config\data\test_data'
        filename = 'bp_ok.csv'
        self.manager.import_data(path_to_file, filename)
        self.assertEqual (self.manager.imported_data[1][0], '1')
        self.assertEqual (
            self.manager.imported_data[2][1], '65 rue des Bas Rogers'
        )
