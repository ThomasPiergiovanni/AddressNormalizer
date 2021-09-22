"""CSV manager module
"""
import csv
import os

from config.custom_settings.app_variables import INPUT_DIR, INPUT_FILE


class CsvManager:
    def __init__(self):
        self.input_folder = INPUT_DIR
        self.input_file = INPUT_FILE
        self.imported_data = []

    def import_data(self):
        data_file = os.path.join(self.input_folder, self.input_file)
        with open(data_file, 'r', newline='', encoding='utf8') as file:
            read_file = csv.reader(file, delimiter=";")
            for row in read_file:
                self.imported_data.append(row)
