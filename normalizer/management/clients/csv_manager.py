"""CSV manager module
"""
import csv
import os


class CsvManager:
    def __init__(self):
        self.imported_data = []
    
    def import_data(self, path_to_file, filename):
        data_file = os.path.join(path_to_file, filename)
        with open(data_file, 'r', newline='', encoding='utf8') as file:
            read_file = csv.reader(file, delimiter=";")
            for row in read_file:
                self.imported_data.append(row)
