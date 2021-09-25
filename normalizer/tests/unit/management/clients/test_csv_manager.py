"""Test csv manager module.
"""
from django.test import TestCase

from config.custom_settings.app_variables import (
    TEST_INPUT_DIR, TEST_INPUT_FILE, TEST_REF_FILE
)
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
    
    def test_import_data_with_adress_file(self):
        data = self.manager.import_data(
            TEST_INPUT_DIR,
            TEST_INPUT_FILE,
            ';',
            None
        )
        self.assertEqual(data[1][0], '1')
        self.assertEqual(data[2][1], '65 rue des Bas Rogers')

    def test_import_data_with_ref_adress_file(self):
        data = self.manager.import_data(
            TEST_INPUT_DIR,
            TEST_REF_FILE,
            ';',
            '"'
        )
        self.assertEqual(data[1][0], 'lieu')
        self.assertEqual(data[2][2], '5')
        self.assertEqual(data[2][1], '')
    
