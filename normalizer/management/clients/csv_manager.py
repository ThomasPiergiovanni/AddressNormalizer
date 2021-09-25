"""CSV manager module
"""
import csv
import os


class CsvManager:
   
    def import_data(
            self, path_to_file, filename, delimiter, quotechar
    ):
        data_file = os.path.join(path_to_file, filename)
        with open(data_file, 'r', newline='', encoding='utf8') as file:
            read_file = csv.reader(
                file, delimiter=delimiter, quotechar=quotechar
            )
            data = []
            for row in read_file:
                data.append(row)
            return data
