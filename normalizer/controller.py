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
    UNWANTED_CHARACTERS,
    REPETITION,
    WRONG_NAMES,
    WRONG_PREFIXS,
    DETERMINERS
)

class Controller:

    def __init__(self):
        self.input_data = None
        self.column_index = None
        self.column_values = None
        self.address_list = None
        self.address_dict = None
        self.n_adr_low_list = None
        self.n_adr_upp_list = None
        self.n_adr_cap_list = None
        self.ouput_data = None

    def normalize(self):
        self.input_data = self.__import_data(
            directory=INPUT_DIR,
            filename=INPUT_FILE_NAME,
            delimiter=INPUT_FILE_DELIMITER,
            quotechar=INPUT_FILE_QUOTECHAR
        )
        self.column_index = self.__get_column_index(INPUT_FILE_TARGET_COLUMN)
        self.column_values = self.__get_column_value()
        self.column_values = self.__remove_characters()
        self.column_values = self.__remove_xtra_blanks()
        self.column_values = self.__lower_chars()
        self.address_list = self.__splits_in_words()
        self.address_dict = self.__parser()
        self.n_adr_low_list = self.__build_low_address()
        self.n_adr_upp_list = self.__build_upp_address()
        self.n_adr_cap_list = self.__build_cap_address()
        self.ouput_data = self.__create_output_structure()
        self.__export_data(
            directory=OUTPUT_DIR,
            filename=OUTPUT_FILE,
            data=self.ouput_data
        )


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
    
    def __splits_in_words(self):
        data = []
        for row in self.column_values:
            word = row.split()
            data.append(word)
        return data

    def __parser(self):
        data = []
        for words in self.address_list:
            address = {
                'hnr': None,
                'rep':  None,
                'name' : None,
            }
            counter = 0
            name_list = []
            for word in words:
                if counter == 0 :
                    hnr, rep = self.__isolate_hnr(word)
                    if hnr:
                        address['hnr'] = hnr
                    if rep:
                        address['rep'] = rep
                else:
                    rep, name = self.__isolate_rep(word)
                    name = self.__clean_name(name)
                    if address['rep'] is None:
                        if rep:
                            address['rep'] = rep
                        if name:
                            name_list.append(name)
                    else:
                        name_list.append(name)
                    address['name'] = self.__build_name(name_list)
                    address['name'] = self.__clean_build_name(address['name'])
                counter += 1
            data.append(address)
        return data

    def __isolate_hnr(self, word):
        hnr = []
        rep = []
        for letter in list(word):
            try:
                if int(letter):
                    hnr.append(letter)
                elif letter == '0':
                    hnr.append(letter)
                else:
                    pass   
            except Exception:
                rep.append(letter)
        hnr = "".join(hnr)
        rep = "".join(rep)
        return hnr, rep

    def __isolate_rep(self, word):
        rep = None
        name = None
        for repetition in REPETITION:
            if word == repetition:
                rep = True
        if rep:
            rep = word
        else:
            name = word
        return rep, name

    def __build_name(self, name_list):
        name_list_len = len(name_list)
        if name_list_len > 0:
            data = ''
            counter = 1
            for name in name_list: 
                if name and name_list_len > counter:
                    data += name + ' '
                if name and name_list_len == counter:
                    data += name
                counter += 1
            return data
            

    def __clean_name(self, name):
        if name:
            for w_prefix in WRONG_PREFIXS:
                if name in w_prefix['wrong']:
                    return w_prefix['good']
            return name

    def __clean_build_name(self, name):
        if name:
            for w_name in WRONG_NAMES:
                if name in w_name['wrong']:
                    return w_name['good']
            return name
    
    def __build_low_address(self):
        n_address_list = []
        for address in self.address_dict:
            n_address = ''
            if address['hnr']:
                n_address += address['hnr']
            if address['rep']:
                n_address += ' ' + address['rep']
            if address['name']:
                n_address += ' ' + address['name']
            n_address_list.append(n_address)
        return n_address_list

    def __build_upp_address(self):
        n_address_up_list = []
        for address in self.address_dict:
            n_address = ''
            if address['hnr']:
                n_address += address['hnr']
            if address['rep']:
                n_address += ' ' + address['rep'].upper()
            if address['name']:
                n_address += ' ' + address['name'].upper()
            n_address_up_list.append(n_address)
        return n_address_up_list

    def __build_cap_address(self):
        n_address_cap_list = []
        for address in self.address_dict:
            n_address = ''
            if address['hnr']:
                n_address += address['hnr']
            if address['rep']:
                n_address += ' ' + address['rep'].capitalize()
            if address['name']:
                address_name = self.__custom_capitalize(address['name'])
                n_address += ' ' + address_name
            n_address_cap_list.append(n_address)
        return n_address_cap_list
    
    def __custom_capitalize(self, address_name):
        adr_len = len(re.split('\'| ', address_name))
        if adr_len > 0:
            data = ''
            counter = 1
            for name in re.split('\'| ', address_name):
                is_determiner = self.__check_determiner(name=name)
                if is_determiner:
                    data = self.__add_name(
                        name=name, adr_len=adr_len, data=data, counter=counter
                    )
                    counter += 1
                else:
                    c_name = name.capitalize()
                    data = self.__add_name(
                        name=c_name, adr_len=adr_len, data=data, counter=counter
                    )
                    counter += 1
            data = data.replace(' d ',' d\'')
            data = data.replace(' l ',' l\'')
            return data
    
    def __check_determiner(self, name):
        for determiner in DETERMINERS:
            if name == determiner:
                return True
    
    def __add_name(self, name, adr_len, data, counter):
        if name and adr_len > counter:
            data += name + ' '
        if name and adr_len == counter:
            data += name
        return data
    
    def __create_output_structure(self):
        col_val_len = len(self.column_values)
        n_adr_low_list_len = len(self.n_adr_low_list)
        n_adr_upp_list_len = len(self.n_adr_upp_list)
        n_adr_cap_list_len = len(self.n_adr_cap_list)
        if (
                col_val_len == n_adr_low_list_len == n_adr_upp_list_len == n_adr_cap_list_len
        ):
            output_structure = []
            for counter in range(col_val_len):
                line = []
                line.append(counter + 1)
                line.append(self.column_values[counter])
                line.append(self.n_adr_low_list[counter])
                line.append(self.n_adr_upp_list[counter])
                line.append(self.n_adr_cap_list[counter])
                output_structure.append(line)
            return output_structure
        else:
            pass

    def __export_data(self, directory, filename, data):
        data_file = os.path.join(directory, filename)
        with open(data_file, 'w', newline='',  encoding='utf8') as file:
            filewriter = csv.writer(
                file, delimiter=';',
                quotechar='"',
                quoting=csv.QUOTE_MINIMAL
            )
            filewriter.writerow(
                [
                    "id",
                    "input_adr",
                    "low_adr",
                    "upp_adr",
                    "cap_adr"
                ]
            )
            for item in data:
                filewriter.writerow(
                    [
                        item[0],
                        item[1],
                        item[2],
                        item[3],
                        item[4],
                    ]
                )


