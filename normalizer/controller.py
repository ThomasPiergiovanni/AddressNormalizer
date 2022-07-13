import csv
import os

from normalizer.config.env import (
    INPUT_DIR,
    OUTPUT_DIR,
    INPUT_FILE_NAME,
    INPUT_FILE_DELIMITER,
    INPUT_FILE_QUOTECHAR,
    INPUT_FILE_TARGET_COLUMN,
    OUTPUT_FILE
)

class Controller:

    def __init__(self):
        self.input_data = None

    def normalization(self):
        self.input_data = self.__import_data(
            directory=INPUT_DIR,
            filename=INPUT_FILE_NAME,
            delimiter=INPUT_FILE_DELIMITER,
            quotechar=INPUT_FILE_QUOTECHAR
        )


    def __import_data(
            self, directory, filename, delimiter, quotechar
    ):
        full_path = os.path.join(directory=directory, filename=filename)
        with open(full_path, 'r', newline='', encoding='utf8') as file:
            read_file = csv.reader(
                file, delimiter=delimiter, quotechar=quotechar
            )
            data = []
            for row in read_file:
                data.append(row)
            return data