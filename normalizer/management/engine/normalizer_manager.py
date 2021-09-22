"""Normalizer manager app module.
"""
from normalizer.management.clients.csv_manager import CsvManager

from config.custom_settings.app_variables import INPUT_DIR, INPUT_FILE

class NormalizerManager():
    """Normalizer manager app class
    """
    def __init__(self):
        self.raw_data = None 
        self.data = None

    def __get_raw_data(self):
        csv_manager = CsvManager()
        csv_manager.import_data(INPUT_DIR, INPUT_FILE)
        self.raw_data = csv_manager.imported_data
    
    def __set_attributes(self):
        counter = 0
        for raw in self.raw_data:
            for item in raw:

