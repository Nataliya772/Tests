import unittest
import API_translatior

class TestFail(unittest.TestCase):

    def test_translatior_too_many_args(self):
        with self.assertRaises(TypeError):
            API_translatior.translate_it('hello', 'en', 'en', 'ru')
