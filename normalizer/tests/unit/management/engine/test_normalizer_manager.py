"""Test normalizer manager  module.
"""
from django.test import TestCase

from normalizer.management.engine.normalizer_manager import NormalizerManager
from normalizer.tests.unit.management.clients.test_csv_manager import CsvManagerTest


class NormalizerManagerTest(TestCase):
    """Test normalizer manager class.
    """
    def setUp(self):
        self.manager =NormalizerManager()
        self.data = None
        self.ref_address = None
    
    @classmethod
    def emulate_raw_data(cls):
        raw_data = [
            ['id', 'adresse'],
            ['1', '12 rue Ledru-Rollin'],
            ['2', '65 rue des Bas Rogers'],
            ['46', '51 allée de la pépinière'],
            ['3', '28 rue victor hugo']
        ]
        return raw_data

    def test_get_raw_data(self):
        csv_manager_test = CsvManagerTest()
        csv_manager_test.emulate_imported_data()
        self.manager._NormalizerManager__get_raw_data()
        self.assertEqual(
            self.manager.raw_data[2],
            csv_manager_test.imported_data[2]
        )
    
    def test_set_attributes(self):
        self.manager.raw_data = self.emulate_raw_data()
        self.manager._NormalizerManager__set_attributes()
        self.assertEqual(
            self.manager.data[0]['id'], '1'
        )
