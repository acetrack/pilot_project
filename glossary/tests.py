import unittest
from .views import text_tokenize


class ViewsTest(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://localhost:8080'

    def tearDown(self):
        pass

    def test_append_article(self):
        src = "Bring Bootstrap to life with our optional JavaScript plugins built on jQuery. Learn about each plugin, our data and programmatic API options, and more."
        result = text_tokenize(src)
        self.assertIsNone(result, 'result is None!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')