# import unittest
from unittest import TestCase

from normalizer.controller import Controller


class TestController(TestCase):

    def setUp(self):
        self.controller = Controller()

    def test_import_data(self):
        data = self.controller._Controller__import_data(
            directory=r'C:\02_dev\AddressNormalizer\data\input',
            filename='test_file.csv',
            delimiter=';',
            quotechar='"'
        )
        counter = 0
        for row in data:
            if counter == 0 :
                self.assertEqual(row[0], 'nom')
                self.assertEqual(row[1],'adresse')
                self.assertEqual(row[2],'quartier')
            elif counter == 2:
                self.assertEqual(row[0], None)
                self.assertEqual(row[1], '24, rue Carnot')
                self.assertEqual(row[2], 'centre ville')
            else:
                pass
            counter += 1

# if __name__ == '__main__':
#     unittest.main()
