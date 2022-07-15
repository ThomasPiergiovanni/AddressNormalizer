import csv
import os
import re

from normalizer.config.env import (
    INPUT_DIR,
    OUTPUT_DIR,
    INPUT_FILE_NAME,
    INPUT_FILE_DELIMITER,
    INPUT_FILE_QUOTECHAR,
    INPUT_FILE_TARGET_COLUMN,
    OUTPUT_FILE,
    UNWANTED_CHARACTERS
)

class Controller:

    def __init__(self):
        self.input_data = None
        self.column_index = None

    def normalization(self):
        self.input_data = self.__import_data(
            directory=INPUT_DIR,
            filename=INPUT_FILE_NAME,
            delimiter=INPUT_FILE_DELIMITER,
            quotechar=INPUT_FILE_QUOTECHAR
        )
        self.column_index = self.__get_column_index(INPUT_FILE_TARGET_COLUMN)
        self.column_values = self.__get_column_value()
        self.column_values = self.__get_remove_characters()


    def __import_data(
            self, directory, filename,delimiter, quotechar
    ):
        full_path = os.path.join(directory, filename)
        with open(full_path, 'r', newline='', encoding='utf8') as file:
            read_file = csv.reader(
                file, delimiter=delimiter, quotechar=quotechar
            )
            data = []
            for row in read_file:
                data.append(row)
            return data

    def __get_column_index(self, column_name):
        index = self.input_data[0].index(column_name)
        return index

    def __get_column_value(self):
        data = []
        counter = 0
        for row in self.input_data:
            if counter >= 1:
                data.append(row[self.column_index])
            counter += 1
        return data
    
    def __remove_characters(self):
        data = []
        for row in self.column_values:
            for unwanted_character in UNWANTED_CHARACTERS:
                row = row.replace(unwanted_character, ' ')
            data.append(row)
        return data
    
    def __remove_xtra_blanks(self):
        data = []
        for row in self.column_values:
            row = re.sub(' +',' ',row)
            row = row.strip()
            data.append(row)
        return data

    def __lower_chars(self):
        data = []
        for row in self.column_values:
            row = row.lower()
            data.append(row)
        return data
    
    def __splits_words(self):
        data = []
        for row in self.column_values:
            row = row.split()
            data.append(row)
        return data

