"""Normalizer manager app module.
"""
from normalizer.management.client.csv_manager import CsvManager


class NormalizerManager():
    """Normalizer manager app class
    """
    def _import_csv_data(self):
        csv_manager = CsvManager()
        csv_manager.import_data()
