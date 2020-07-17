import unittest
import API_translatior


class TestAPI(unittest.TestCase):

    def test_API_connect(self):
        self.assertIn('200', str(API_translatior.translate_it('hello', 'en')))

    def test_translaton_from_en(self):
        self.assertIn('привет', str(API_translatior.translate_it('hello', 'en')))

    def test_translaton_fail_lang_ru_to_ru(self):
        self.assertNotIn('привет', str(API_translatior.translate_it('hello', 'ru')))

    def test_translaton_from_en_to_de(self):
        self.assertIn('Hallo', str(API_translatior.translate_it('hello', 'en', 'de')))
