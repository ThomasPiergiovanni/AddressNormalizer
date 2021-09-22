"""Normalizer manager app module.
"""
import os

from re import split, sub

from config.custom_settings.app_variables import (
    INPUT_DIR, INPUT_FILE, ZIP_CODE_LIST, CITY_NAME_LIST
)
from normalizer.management.clients.csv_manager import CsvManager


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

    def __remove_zip(self):
        for item in self.address_list:
            for zip_code in ZIP_CODE_LIST:
                addr = item['address']
                addr = addr.replace(zip_code, '')
                item['address'] = addr
    
    def __remove_unwanted_characters(self):
        for item in self.address_list:
            addr = item['address']
            addr = sub("[,.?!()]", " ", addr)
            item['address'] = addr
    
    def __lower_string(self):
        for item in self.address_list:
            addr = item['address']
            addr = addr.lower()
            item['address'] = addr

    def __remove_accent(self):
        for item in self.address_list:
            addr = item['address']
            addr = addr.replace("é","e")
            addr = addr.replace("ë","e")
            addr = addr.replace("ê","e")
            addr = addr.replace("è","e")
            addr = addr.replace("ì","i")
            addr = addr.replace("î","i")
            addr = addr.replace("ï","i")
            addr = addr.replace("à","a")
            addr = addr.replace("â","a")
            addr = addr.replace("â","a")
            addr = addr.replace("ù","u")
            addr = addr.replace("û","u")
            addr = addr.replace("ü","u")
            addr = addr.replace("ô","o")
            addr = addr.replace("ö","o")
            addr = addr.replace("ò","o")
            item['address'] = addr

    def __remove_city_name(self):
        for item in self.address_list:
            for city_name in CITY_NAME_LIST:
                addr = item['address']
                addr = addr.replace(city_name, '')
                item['address'] = addr

    def __strip_and_trim(self):
        for item in self.address_list:
            addr = item['address']
            addr = addr.strip(" ,.'?!")
            while "  " in addr:
                addr = addr.replace("  ", " ")
            item['address'] = addr

    def __set_address_components(self):
        for item in self.address_list:
            addr = item['address']
            comp_list = split(" ", addr)
            list_len = len(comp_list)
            counter = 1
            print(comp_list)
            for component in comp_list:
                if counter == 1:
                    item['comp_1'] = component
                    counter += 1
                elif counter == 2:
                    item['comp_2'] = component
                    counter += 1
                elif counter == 3:
                    item['comp_3'] = component
                    counter += 1
                elif counter == 4:
                    item['comp_4'] = component
                    counter += 1
                elif counter == 5:
                    item['comp_5'] = component
                    counter += 1
                elif counter == 6:
                    item['comp_6'] = component
                    counter += 1
                elif counter == 7:
                    item['comp_7'] = component
                    counter += 1
                elif counter == 8:
                    item['comp_8'] = component
                    counter += 1


