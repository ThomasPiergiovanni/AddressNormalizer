"""Test normalizer manager  module.
"""
from django.test import TestCase

from normalizer.management.engine.normalizer_manager import NormalizerManager
from normalizer.tests.unit.management.clients.test_csv_manager import CsvManagerTest


class NormalizerManagerTest(TestCase):
    """Test normalizer manager class.
    """
    def setUp(self):
        self.manager =NormalizerManager()
        self.data = None
        self.ref_address = None
    
    @classmethod
    def emulate_raw_address_list(cls):
        raw_address_list = [
            ['id', 'adresse'],
            ['1', '12 rue Ledru-Rollin'],
            ['2', '65 rue des Bas Rogers'],
            ['46', '51 allée de la pépinière'],
            ['3', '28 rue victor hugo']
        ]
        return raw_address_list

    @classmethod
    def emulate_raw_ref_address_list(cls):
        raw_ref_address_list = [
            ['objectid','categorie', 'sous_categorie', 'numero', 'type_voie', 'determinant', 'nom', 'code_postal', 'ville', 'adresse_complete', 'source', 'id_origin', 'qualite', 'indice_repetition', 'libelle', 'nom_voie', 'quartier', 'shape'],
            ['1','lieu', '', '13', 'RUE', '', 'BERTHELOT', '92150', 'SURESNES', '13 RUE BERTHELOT', 'BANO', '920730665H-13', '0.60000002', '', '13', 'RUE BERTHELOT', 'CENTRE VILLE', '2400000001000000010004006D0F00000C000000010000009080C2BCFF1488'],
            ['2','lieu', '', '5', 'RUE', '', 'BERTHELOT', '92150', 'SURESNES', '5 BIS RUE BERTHELOT', 'BANO', '920730665H-5B', '0.60000002', 'BIS', '5 BIS', 'RUE BERTHELOT', 'CENTRE VILLE', '2400000001000000010004006D0F00000C000000010000009080C2BCFF1488']
        ]
        return raw_ref_address_list
    
    @classmethod
    def emulate_address_list(cls):
        address_list = [
            {
                'id': '1',
                'address': '51 allée de la pépinière'
            },
            {
                'id': '4',
                'address': '51 allée de la pépinière 92500 SUresnes'
            },
            {
                'id': '5',
                'address': '51 allée de la pépinière 92500SUresnes'
            },
            {
                'id': '6',
                'address': '51 allée de la pépinière92500SUresnes'
            }
        ]
        return address_list

    def test_set_address_attributes(self):
        self.manager.raw_address = self.emulate_raw_address_list()
        self.manager._set_address_attributes()
        self.assertEqual(self.manager.address_list[0]['id'], '1')
        self.assertEqual(
            self.manager.address_list[2]['address'],
            '51 allée de la pépinière'
        )

    def test_set_ref_address_attributes(self):
        self.manager.raw_ref_address = self.emulate_raw_ref_address_list()
        self.manager._set_ref_address_attributes()
        self.assertEqual(self.manager.ref_address_list[0]['id'], '1')
        self.assertEqual(
            self.manager.ref_address_list[1]['address'],
            '5 BIS RUE BERTHELOT'
        )

    def test_remove_zip(self):
        self.manager.address_list = self.emulate_address_list()
        self.manager._remove_zip()
        self.assertEqual(
            self.manager.address_list[0]['address'],
            '51 allée de la pépinière' 
        )
        self.assertEqual(
            self.manager.address_list[1]['address'],
            '51 allée de la pépinière  SUresnes' 
        )
        self.assertEqual(
            self.manager.address_list[2]['address'],
            '51 allée de la pépinière SUresnes' 
        )
        self.assertEqual(
            self.manager.address_list[3]['address'],
            '51 allée de la pépinièreSUresnes' 
        )
    
    def test_remove_unwanted_characters(self):
        self.manager.address_list = [
            {
                'id': '1',
                'address': '51, allée! de la pépinière'
            }
        ]
        self.manager._remove_unwanted_characters()
        self.assertEqual(
            self.manager.address_list[0]['address'],
            '51  allée  de la pépinière' 
        )
    
    def test_lower_string(self):
        self.manager.address_list = self.emulate_address_list()
        self.manager._lower_string()
        self.assertEqual(
            self.manager.address_list[1]['address'],
            '51 allée de la pépinière 92500 suresnes' 
        )

    def test_remove_accent(self):
        self.manager.address_list = self.emulate_address_list()
        self.manager._remove_accent()
        self.assertEqual(
            self.manager.address_list[0]['address'],
            '51 allee de la pepiniere' 
        )

    def test_remove_city_name(self):
        self.manager.address_list = [
            {
                'id': '1',
                'address': '51 allée de la pépinière 92500 suresnes'
            }
        ]
        self.manager._remove_city_name()
        self.assertEqual(
            self.manager.address_list[0]['address'],
            '51 allée de la pépinière 92500 ' 
        )

    def test_strip_and_trim(self):
        self.manager.address_list = [
            {
                'id': '1',
                'address': '51 allée de la  pépinière 92500 suresnes !'
            },
            {
                'id': '2',
                'address': ' 51 allée     de la  pépinière 92500 suresnes!'
            }
        ]
        self.manager._strip_and_trim()
        self.assertEqual(
            self.manager.address_list[0]['address'],
            '51 allée de la pépinière 92500 suresnes' 
        )
        self.assertEqual(
            self.manager.address_list[1]['address'],
            '51 allée de la pépinière 92500 suresnes' 
        )
    def test_set_adress_component(self):
        self.manager.address_list = [
            {
                'id': '1',
                'address': '51 allée de la pépinière 92500 suresnes'
            }
        ]
        self.manager._set_address_components()
        self.assertEqual(self.manager.address_list[0]['comp_1'], '51')
        self.assertEqual(self.manager.address_list[0]['comp_2'], 'allée')
        self.assertEqual(self.manager.address_list[0]['comp_3'], 'de')
        self.assertEqual(self.manager.address_list[0]['comp_4'], 'la')
        self.assertEqual(self.manager.address_list[0]['comp_5'], 'pépinière')
        self.assertEqual(self.manager.address_list[0]['comp_6'], '92500')
        self.assertEqual(self.manager.address_list[0]['comp_7'], 'suresnes')
    
    def test_remove_incorrect_prefix(self):
        self.manager.address_list = [
            {
                'id': '1',
                'address': '51 allée de la pépinière 92500 suresnes',
                'comp_1': '51',
                'comp_2': 'av',
                'comp_3': 'de',
                'comp_4': 'la',
                'comp_5': 'pépinière',
                'comp_6': '92500',
                'comp_7': 'suresnes'
            }
        ]
        self.manager._replace_prefixes()
        self.assertEqual(self.manager.address_list[0]['comp_1'], '51')
        self.assertEqual(self.manager.address_list[0]['comp_2'], 'avenue')
    

    def test__set_prefix(self):
        item = {
            'id': '1',
            'address': '51 allée de la pépinière 92500 suresnes',
            'comp_1': '51',
            'comp_2': 'av',
            'comp_3': 'de',
            'comp_4': 'la',
            'comp_5': 'pépinière',
            'comp_6': '92500',
            'comp_7': 'suresnes'
        }
        component = item['comp_2']
        component_name = 'comp_2'
        perfix_list = [
            {
                'correct_name': "allee",
                'incomformities': ["ALL", "All", "all"]
            },
            {
                'correct_name': "avenue",
                'incomformities': ["AV", "Av", "av"]
            }
        ]
        method_output = self.manager._NormalizerManager__set_prefix(
            item, component, component_name, perfix_list
        )
        self.assertEqual(method_output['comp_2'], 'avenue')
    
    def test__upper_components(self):
        self.manager.address_list = [
            {
                'id': '1',
                'address': '51 allée de la pépinière 92500 suresnes',
                'comp_1': '51',
                'comp_2': 'avenue',
                'comp_3': 'de',
                'comp_4': 'la',
                'comp_5': 'pépinière',
                'comp_6': '92500',
                'comp_7': 'suresnes'
            }
        ]
        self.manager._upper_components()
        self.assertEqual(self.manager.address_list[0]['comp_1'], '51')
        self.assertEqual(self.manager.address_list[0]['comp_2'], 'AVENUE')

    def test_upper(self):
        item = {
            'id': '1',
            'address': '51 allée de la pépinière 92500 suresnes',
            'comp_1': '51',
            'comp_2': 'av',
            'comp_3': 'de',
            'comp_4': 'la',
            'comp_5': 'pépinière',
            'comp_6': '92500',
            'comp_7': 'suresnes'
        }
        component = item['comp_2']
        component_name = 'comp_2'
        method_output = self.manager._NormalizerManager__upper(
            item, component, component_name
        )
        self.assertEqual(method_output['comp_2'], 'AV')

    def test_create_new_address(self):
        self.manager.address_list = [
            {
                'id': '1',
                'address': '51 allée de la pépinière 92500 suresnes',
                'comp_1': '51',
                'comp_2': 'AVENUE',
                'comp_3': 'DE',
                'comp_4': 'LA',
                'comp_5': 'PEPINIERE'
            }
        ]
        self.manager._create_new_address()
        self.assertEqual(
            self.manager.address_list[0]['new_address'],
            '51 AVENUE DE LA PEPINIERE'
        )

    def test_matcher(self):
        self.manager.address_list = [
            {
                'id': '1',
                'address': '51 allée de la pépinière 92500 suresnes',
                'comp_1': '51',
                'comp_2': 'AVENUE',
                'comp_3': 'DE',
                'comp_4': 'LA',
                'comp_5': 'PEPINIERE',
                'new_address': '51 AVENUE DE LA PEPINIERE' 
            }, 
            {
                'id': '2',
                'address': '52 allée de la pépinière 92500 suresnes',
                'comp_1': '52',
                'comp_2': 'AVENUE',
                'comp_3': 'DE',
                'comp_4': 'LA',
                'comp_5': 'PEPINIERE',
                'new_address': '52 AVENUE DE LA PEPINIERE' 
            }
        ]
        self.manager.ref_address_list = [
            {
                'id': '1',
                'address': '51 AVENUE DE LA PEPINIERE'
            }, 
            {
                'id': '3',
                'address': '53 AVENUE DE LA PEPINIERE' 
            }
        ]
        self.manager._matcher()
        self.assertEqual(
            self.manager.address_list[0]['match'], True
        )
        self.assertEqual(
            self.manager.address_list[1]['match'], False
        )

        