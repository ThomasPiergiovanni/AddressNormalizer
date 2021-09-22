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
    

    def test_get_raw_data(self):
        csv_manager_test = CsvManagerTest()
        csv_manager_test.emulate_imported_data()
        self.manager._NormalizerManager__get_raw_data()
        self.assertEqual(
            self.manager.raw_data[2],
            csv_manager_test.imported_data[2]
        )
