import unittest
import Clerc
from unittest.mock import patch

from Documentation import directories, documents


class TestClerc(unittest.TestCase):

    def test_user_number_doc(self):
        with patch('Clerc.input', return_value = '777'):
            Clerc.user_number_doc()

    def test_add_new_user(self):
        with patch('Clerc.input', return_value = '777'):
            Clerc.user_number_doc()
        with patch('Clerc.input', side_effect = ['invoice', 'Ivan Ivanov', '3']):
            self.assertNotIn('Ivan Ivanov', Clerc.list_all_names(documents))
            Clerc.add_new_user(documents, directories)
            self.assertIn('777', Clerc.directories['3'])

    def test_user_service(self):
        with patch('Clerc.input', side_effect=['p', 's', 'l', 'd', 'ln', 'q']):
            with patch('Clerc.input', return_value = '11-2'):
                self.assertIn('11-2', Clerc.directories['1'])
                Clerc.user_number_doc()
                Clerc.username_by_doc(documents)
                Clerc.shelf_number_by_doc(directories)
                Clerc.list_all_doc(documents)
                Clerc.del_user_list(documents)
                Clerc.del_user_shelf(directories)
                Clerc.list_all_names(documents)
