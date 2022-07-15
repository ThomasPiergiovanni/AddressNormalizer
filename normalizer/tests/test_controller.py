# import unittest
from unittest import TestCase

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
    
    def test_import_data(self):
        data = self.controller._Controller__import_data(
            directory=r'C:\02_dev\AddressNormalizer\data\input',
            filename='test_file.csv',
            delimiter=',',
            quotechar='"'
        )
        counter = 0
        self.assertEqual(data[0][0], 'nom')
        self.assertEqual(data[2][1], '24, rue Carnot')
    
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
        data = self.controller._Controller__splits_words()
        self.assertEqual(data[0][0], '20')
        self.assertEqual(data[0][3], 'ledru-rollin')
        self.assertEqual(data[1][2], 'ledru')
        



# if __name__ == '__main__':
#     unittest.main()
