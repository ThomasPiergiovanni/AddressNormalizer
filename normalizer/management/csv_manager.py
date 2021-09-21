"""CSV manager module
"""
import csv
import os


INPUT_DIR  = r'C:\02_dev\hnr_normaliser\data\input'
INPUT_FILE = 'bp2021.csv'

class CsvManager:
    def __init__(self):
        self.raw_data = []
        self.features_class = []

    def import_data(self):
        data_file = os.path.join(INPUT_DIR, INPUT_FILE)
        with open(data_file, 'r', newline='', encoding='utf8') as file:
            read_file = csv.reader(file, delimiter=";")
            for row in read_file:
                self.raw_data.append(row)