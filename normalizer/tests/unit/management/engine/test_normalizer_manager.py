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
    
    def test_create_data(self):
        self.manager.imported_data = CsvManagerTest.emulate_imported_data()
        self.manager._NormalizerManager__create_data()
        self.assertEqual(self.manager.data[0]['id'], 1 )
        self.assertEqual(self.manager.data[2]['name'], '65 rue des Bas Rogers')
