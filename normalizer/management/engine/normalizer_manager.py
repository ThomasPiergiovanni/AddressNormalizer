"""Normalizer manager app module.
"""
import os
from normalizer.management.clients.csv_manager import CsvManager

from config.custom_settings.app_variables import INPUT_DIR, INPUT_FILE

class NormalizerManager():
    """Normalizer manager app class
    """
    def __init__(self):
        self.raw_data = None
        self.address_list = []


    def __get_raw_data(self):
        csv_manager = CsvManager()
        csv_manager.import_data(INPUT_DIR, INPUT_FILE)
        self.raw_data = csv_manager.imported_data
    
    def __set_attributes(self):
        counter = 0
        for raw in self.raw_data:
            data = {
                'id': raw[0],
                'address': raw[1]
            }
            if counter >= 1:
                self.address_list.append(data)
            counter += 1

