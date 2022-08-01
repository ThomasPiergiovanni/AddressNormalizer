# import unittest
from unittest import TestCase
from unittest.mock import patch

from normalizer.controller import Controller


class TestController(TestCase):

    def setUp(self):
        self.controller = Controller()
        self.emulate_input_data = [
            ['nom', 'adresse', 'quartier'],
            ['', '20 bis, rue Ledru-Rollin', 'centre ville'],
            ['', '24, rue Carnot', 'centre ville'],
            ['', '12, rue Ledru Rollin', 'centre ville']
        ]
        self.emulate_column_values = [
            '20 bis, rue Ledru-Rollin',
            '24, rue Carnot',
            '12, rue Ledru Rollin',
            '2 ter,* rue (Ledru\Rollin)',
            'A quaTER, rue Ledru Rollin'
        ]
    
    def tearDown(self):
        self.controller = None
        self.emulate_input_data = None
        self.emulate_column_values = None

    def mock_import_data(*args, **kwargs):
        data = [
                    ['nom', 'adresse', 'quartier'],
                    ['', '20 bis, rue Ledru-Rollin', 'centre ville'],
                    ['', '24, rue Carnot', 'centre ville'],
                    ['', '12, rue Ledru Rollin', 'centre ville'],
                    ['', '45bis, rue Gambetta', 'centre ville']
                ]
        return data


    def mock_get_column_index(*args, **kwargs):
        index = 1 
        return index
    
    def test_import_data(self):
        data = self.controller._Controller__import_data(
            directory=r'C:\02_dev\AddressNormalizer\data\input',
            filename='test_file.csv',
            delimiter=',',
            quotechar='"'
        )
        self.assertEqual(data[0][0], 'nom')
        self.assertEqual(data[2][1], '24, rue Carnot')

    @patch(
        'normalizer.controller.Controller._Controller__import_data',
        side_effect=mock_import_data
    )
    @patch(
        'normalizer.controller.Controller._Controller__get_column_index',
        side_effect=mock_get_column_index
    )       
    def test_normalize(
            self, mock_import_data, mock_get_column_index
    ):
        self.controller.normalize()
        self.assertEqual(
            self.controller.address_dict[0]['rep'], 'bis'
        )
        self.assertEqual(
            self.controller.address_dict[0]['name'], 'rue ledru-rollin'
        )
        self.assertEqual(
            self.controller.address_dict[3]['hnr'], '45'
        )
        self.assertEqual(
            self.controller.address_dict[3]['rep'], 'bis'
        )
        self.assertEqual(
            self.controller.address_dict[3]['name'], 'rue gambetta'
        )


    def test_get_column_index(self):
        column_name = 'adresse'
        self.controller.input_data = self.emulate_input_data
        index = self.controller._Controller__get_column_index(column_name)
        self.assertEqual(index, 1)

    def test_get_column_value(self):
        self.controller.input_data = self.emulate_input_data
        self.controller.column_index = 1
        data = self.controller._Controller__get_column_value()
        self.assertEqual(
            data[2], '12, rue Ledru Rollin'
        )

    def test_remove_characters(self):
        self.controller.column_values = self.emulate_column_values
        data = self.controller._Controller__remove_characters()
        self.assertEqual(data[0], '20 bis  rue Ledru-Rollin')
        self.assertEqual(data[2], '12  rue Ledru Rollin')
        self.assertEqual(data[3], '2 ter   rue  Ledru Rollin ')

    def test_remove_xtra_blanks(self):
        self.controller.column_values = [
            'This string   has  space', '    This  one too'
        ]
        data = self.controller._Controller__remove_xtra_blanks()
        self.assertEqual(data[0], 'This string has space')
        self.assertEqual(data[1], 'This one too')

    def test_lower_chars(self):
        self.controller.column_values = self.emulate_column_values
        data = self.controller._Controller__lower_chars()
        self.assertEqual(data[0], '20 bis, rue ledru-rollin')
        self.assertEqual(data[2], '12, rue ledru rollin')

    def test_splits_words(self):
        self.controller.column_values = [
            '20 bis rue ledru-rollin',
            '12 rue ledru rollin'
        ]
        data = self.controller._Controller__splits_in_words()
        self.assertEqual(data[0][0], '20')
        self.assertEqual(data[0][3], 'ledru-rollin')
        self.assertEqual(data[1][2], 'ledru')
    
    def test_parser(self):
        self.controller.address_list = [
            ['20','ter','rue', 'ledru-rollin'],
            ['12','rue','ledru', 'rollin'],
            ['84bis','rue','ledru', 'rollin'],
        ]
        data = self.controller._Controller__parser()
        self.assertEqual(data[0]['hnr'], '20')
        self.assertEqual(data[0]['rep'], 'ter')
        self.assertEqual(data[0]['name'], 'rue ledru-rollin')
        self.assertEqual(data[1]['hnr'], '12')
        self.assertEqual(data[1]['rep'], None)
        self.assertEqual(data[1]['name'], 'rue ledru rollin')
        self.assertEqual(data[2]['hnr'], '84')
        self.assertEqual(data[2]['rep'], 'bis')
        self.assertEqual(data[2]['name'], 'rue ledru rollin')

    def test_isolate_hnr(self):
        data = self.controller._Controller__isolate_hnr('20')
        self.assertEqual(data[0], '20')
        self.assertEqual(data[1], '')
        data = self.controller._Controller__isolate_hnr('84bis')
        self.assertEqual(data[0], '84')
        self.assertEqual(data[1], 'bis')

    def test_isolate_rep_name(self):
        data = self.controller._Controller__isolate_rep('bis')
        self.assertEqual(data[0], 'bis')
        self.assertEqual(data[1], None)
        data = self.controller._Controller__isolate_rep('ter')
        self.assertEqual(data[0], 'ter')
        self.assertEqual(data[1], None)
        data = self.controller._Controller__isolate_rep('quater')
        self.assertEqual(data[0], 'quater')
        self.assertEqual(data[1], None)
        data = self.controller._Controller__isolate_rep('tamer')
        self.assertEqual(data[0], None)
        self.assertEqual(data[1], 'tamer')

    def test_build_name(self):
        data = self.controller._Controller__build_name([])
        self.assertIsNone(data)
        data = self.controller._Controller__build_name(['ledru'])
        self.assertEqual(data, 'ledru')
        data = self.controller._Controller__build_name(['ledru-rolin'])
        self.assertEqual(data, 'ledru-rolin')
        data = self.controller._Controller__build_name(['ledru', 'rolin'])
        self.assertEqual(data, 'ledru rolin')
        data = self.controller._Controller__build_name(
            ['rue','ledru', 'rolin']
        )
        self.assertEqual(data, 'rue ledru rolin')
    
    def test_clean_name(self):
        data = self.controller._Controller__clean_name('al')
        self.assertEqual(data, 'allée')
        data = self.controller._Controller__clean_name('all')
        self.assertEqual(data, 'allée')
        data = self.controller._Controller__clean_name('av')
        self.assertEqual(data, 'avenue')
        data = self.controller._Controller__clean_name('ave')
        self.assertEqual(data, 'avenue')
        data = self.controller._Controller__clean_name('r')
        self.assertEqual(data, 'rue')
        data = self.controller._Controller__clean_name('bd')
        self.assertEqual(data, 'boulevard')
        data = self.controller._Controller__clean_name('boul')
        self.assertEqual(data, 'boulevard')
        data = self.controller._Controller__clean_name('imp')
        self.assertEqual(data, 'impasse')
        data = self.controller._Controller__clean_name('pro')
        self.assertEqual(data, 'promenade')
        data = self.controller._Controller__clean_name('prom')
        self.assertEqual(data, 'promenade')
        data = self.controller._Controller__clean_name('qu')
        self.assertEqual(data, 'quai')
        data = self.controller._Controller__clean_name('res')
        self.assertEqual(data, 'résidence')
        data = self.controller._Controller__clean_name('sen')
        self.assertEqual(data, 'sente')
        data = self.controller._Controller__clean_name('sq')
        self.assertEqual(data, 'square')
        data = self.controller._Controller__clean_name('squ')
        self.assertEqual(data, 'square')
        data = self.controller._Controller__clean_name('vil')
        self.assertEqual(data, 'villa')
        data = self.controller._Controller__clean_name('tamer')
        self.assertEqual(data, 'tamer')

    def test_clean_build_name(self):
        data = self.controller._Controller__clean_build_name(
            'avenue des bas rogers'
        )
        self.assertEqual(data, 'rue des bas rogers')

    def test_build_low_address(self):
        self.controller.address_dict = [
            {'hnr': '20', 'rep': 'bis', 'name': 'rue ledru-rollin'},
            {'hnr': '24', 'rep': None, 'name': 'rue carnot'}
        ]
        data = self.controller._Controller__build_low_address()
        self.assertEqual(data[0], '20 bis rue ledru-rollin')
        self.assertEqual(data[1], '24 rue carnot')

    def test_build_upp_address(self):
        self.controller.address_dict = [
            {'hnr': '20', 'rep': 'bis', 'name': 'rue ledru-rollin'},
            {'hnr': '24', 'rep': None, 'name': 'rue carnot'}
        ]
        data = self.controller._Controller__build_upp_address()
        self.assertEqual(data[0], '20 BIS RUE LEDRU-ROLLIN')
        self.assertEqual(data[1], '24 RUE CARNOT')

    def test_build_cap_address(self):
        self.controller.address_dict = [
            {'hnr': '20', 'rep': 'bis', 'name': 'rue ledru-rollin'},
            {'hnr': '20', 'rep': 'bis', 'name': 'rue des bas rogers'},
            {'hnr': '24', 'rep': None, 'name': 'rue carnot'}
        ]
        data = self.controller._Controller__build_cap_address()
        self.assertEqual(data[0], '20 Bis Rue Ledru-rollin')
        self.assertEqual(data[1], '20 Bis Rue des Bas Rogers')
        self.assertEqual(data[2], '24 Rue Carnot')


    def test_check_determiner(self):
        data = self.controller._Controller__check_determiner('de')
        self.assertTrue(data)
        data = self.controller._Controller__check_determiner('chemin')
        self.assertFalse(data)

    def test_add_name(self):
        data = self.controller._Controller__add_name(
            name='un', adr_len=2, data='', counter=1
        )
        self.assertEqual(data, 'un ')
        data = self.controller._Controller__add_name(
            name='Chemin', adr_len=2, data='', counter=2
        )
        self.assertEqual(data, 'Chemin')

    def test_create_output_structure(self):
        self.controller.column_values = [
            '20 bis, rue Ledru-Rollin', '24, Rue Carnot'
        ]
        self.controller.n_adr_low_list = [
            '20 bis rue ledru-rollin', '24 rue carnot'
        ]
        self.controller.n_adr_upp_list = [
            '20 BIS RUE LEDRU-ROLLIN', '24 RUE CARNOT'
        ]
        self.controller.n_adr_cap_list = [
            '20 Bis Rue Ledru-rollin', '24 Rue Carnot'
        ]
        data = self.controller._Controller__create_output_structure()
        self.assertEqual(data[1][0], 2)
        self.assertEqual(data[1][1], '24, Rue Carnot')
        self.assertEqual(data[1][2], '24 rue carnot')
        self.assertEqual(data[1][3], '24 RUE CARNOT')
        self.assertEqual(data[1][4], '24 Rue Carnot')

    






# if __name__ == '__main__':
#     unittest.main()
