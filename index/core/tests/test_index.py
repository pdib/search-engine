import unittest
import os
from ..index import Index
from ..index_config import IndexConfig
from ..constants import FILE, WORDS, START, END


class IndexTests(unittest.TestCase):

    def test_inverted_index(self):
        '''
        Test the counts in the inverted index.
        Does not test the weights.
        '''
        index = Index(
            os.path.dirname(os.path.realpath(__file__)) + "/test_data", IndexConfig())
        expected = {
            'subtract': {2:1},
            'languag': {1:1, 2:1},
            'extract': {2:1},
            'of': {2:1},
            'comput': {2:1},
            'for': {2:1},
            'algebra': {1:1},
            'repeat': {2:1},
            'digit': {2:1},
            'preliminari': {1:2},
            'report': {1:1},
            'intern': {1:1},
            'by': {2:1},
            'root': {2:1}
        }
        self.assertEqual(expected, index._inverted_index)

    def test_inverted_index_withstop_words(self):
        '''
        Test the counts in the inverted index with stop words.
        Does not test the weights.
        '''
        config = IndexConfig()
        config.stop_words = ['of', 'by', 'for']
        index = Index(
            os.path.dirname(os.path.realpath(__file__)) + "/test_data", config)
        expected = {
         'subtract': {2:1},
            'languag': {1:1, 2:1},
            'extract': {2:1},
            'comput': {2:1},
            'algebra': {1:1},
            'repeat': {2:1},
            'digit': {2:1},
            'preliminari': {1:2},
            'report': {1:1},
            'intern': {1:1},
            'root': {2:1}
        }
        self.assertEqual(expected, index._inverted_index)

    def test_search(self):
        expected = {1:1, 2:1}
        index = Index(
            os.path.dirname(os.path.realpath(__file__)) + "/test_data", IndexConfig())
        self.assertEqual({}, index.search('thereShouldBeNoDocument'))
        self.assertEqual(expected, index.search('Language'))

    def test_index_by_doc_id(self):
        data_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "test_data")
        index = Index(data_path, IndexConfig())
        expected = {
            END: 44,
            FILE: data_path,
            START: 0,
            WORDS: {
                'algebra': 1,
                'intern': 1,
                'languag': 1,
                'preliminari': 2,
                'report': 1
            }
        }
        self.assertEqual({}, index.index_by_doc_id(404))
        self.assertEqual(expected, index.index_by_doc_id(1))