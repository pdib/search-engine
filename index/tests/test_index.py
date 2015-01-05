import unittest
import os
from index.index import Index
from index.index_config import IndexConfig
from index.utility import tf_idf
from index.constants import *


class IndexTests(unittest.TestCase):

    def test_InvertedIndex(self):
        '''
        Test the counts in the inverted index.
        Does not test the weights.
        '''
        index = Index(
            os.path.dirname(os.path.realpath(__file__)) + "/test_data", IndexConfig())
        expected = {
            'subtractions': [{COUNT: 1, NORM_COUNT: 1.0, DOCID: 2, TFIDF: tf_idf(1, 1, 2), NORM_TFIDF: 1.0}],
            'language': [
                {COUNT: 1, NORM_COUNT: 0.5, DOCID: 1,
                 TFIDF: tf_idf(1, 2, 2), NORM_TFIDF: 0.0},
                {COUNT: 1, NORM_COUNT: 1.0, DOCID: 2,
                 TFIDF: tf_idf(1, 2, 2), NORM_TFIDF: 0.0}
            ],
            'extraction': [{COUNT: 1, NORM_COUNT: 1.0, DOCID: 2, TFIDF: tf_idf(1, 1, 2), NORM_TFIDF: 1.0}],
            'of': [{COUNT: 1, NORM_COUNT: 1.0, DOCID: 2, TFIDF: tf_idf(1, 1, 2), NORM_TFIDF: 1.0}],
            'computers': [{COUNT: 1, NORM_COUNT: 1.0, DOCID: 2, TFIDF: tf_idf(1, 1, 2), NORM_TFIDF: 1.0}],
            'for': [{COUNT: 1, NORM_COUNT: 1.0, DOCID: 2, TFIDF: tf_idf(1, 1, 2), NORM_TFIDF: 1.0}],
            'algebraic': [{COUNT: 1, NORM_COUNT: 0.5, DOCID: 1, TFIDF: tf_idf(1, 1, 2), NORM_TFIDF: 1.0}],
            'repeated': [{COUNT: 1, NORM_COUNT: 1.0, DOCID: 2, TFIDF: tf_idf(1, 1, 2), NORM_TFIDF: 1.0}],
            'digital': [{COUNT: 1, NORM_COUNT: 1.0, DOCID: 2, TFIDF: tf_idf(1, 1, 2), NORM_TFIDF: 1.0}],
            'preliminary': [{COUNT: 2, NORM_COUNT: 1.0, DOCID: 1, TFIDF: tf_idf(2, 1, 2), NORM_TFIDF: 1.0}],
            'report': [{COUNT: 1, NORM_COUNT: 0.5, DOCID: 1, TFIDF: tf_idf(1, 1, 2), NORM_TFIDF: 1.0}],
            'international': [{COUNT: 1, NORM_COUNT: 0.5, DOCID: 1, TFIDF: tf_idf(1, 1, 2), NORM_TFIDF: 1.0}],
            'by': [{COUNT: 1, NORM_COUNT: 1.0, DOCID: 2, TFIDF: tf_idf(1, 1, 2), NORM_TFIDF: 1.0}],
            'roots': [{COUNT: 1, NORM_COUNT: 1.0, DOCID: 2, TFIDF: tf_idf(1, 1, 2), NORM_TFIDF: 1.0}]
        }
        self.assertEqual(expected, index._invertedIndex)

    def test_InvertedIndex_withstop_words(self):
        '''
        Test the counts in the inverted index with stop words.
        Does not test the weights.
        '''
        config = IndexConfig()
        config.stop_words = ['of', 'by', 'for']
        index = Index(
            os.path.dirname(os.path.realpath(__file__)) + "/test_data", config)
        expected = {
            'subtractions': [{COUNT: 1, DOCID: 2, NORM_COUNT: 1.0, TFIDF: tf_idf(1, 1, 2), NORM_TFIDF: 1.0}],
            'language': [
                {COUNT: 1, NORM_COUNT: 0.5, DOCID: 1,
                 TFIDF: tf_idf(1, 2, 2), NORM_TFIDF: 0.0},
                {COUNT: 1, NORM_COUNT: 1.0, DOCID: 2,
                 TFIDF: tf_idf(1, 2, 2), NORM_TFIDF: 0.0}
            ],
            'extraction': [{COUNT: 1, NORM_COUNT: 1.0, DOCID: 2, TFIDF: tf_idf(1, 1, 2), NORM_TFIDF: 1.0}],
            'computers': [{COUNT: 1, NORM_COUNT: 1.0, DOCID: 2, TFIDF: tf_idf(1, 1, 2), NORM_TFIDF: 1.0}],
            'algebraic': [{COUNT: 1, NORM_COUNT: 0.5, DOCID: 1, TFIDF: tf_idf(1, 1, 2), NORM_TFIDF: 1.0}],
            'repeated': [{COUNT: 1, NORM_COUNT: 1.0, DOCID: 2, TFIDF: tf_idf(1, 1, 2), NORM_TFIDF: 1.0}],
            'digital': [{COUNT: 1, NORM_COUNT: 1.0, DOCID: 2, TFIDF: tf_idf(1, 1, 2), NORM_TFIDF: 1.0}],
            'preliminary': [{COUNT: 2, NORM_COUNT: 1.0, DOCID: 1, TFIDF: tf_idf(2, 1, 2), NORM_TFIDF: 1.0}],
            'report': [{COUNT: 1, NORM_COUNT: 0.5, DOCID: 1, TFIDF: tf_idf(1, 1, 2), NORM_TFIDF: 1.0}],
            'international': [{COUNT: 1, NORM_COUNT: 0.5, DOCID: 1, TFIDF: tf_idf(1, 1, 2), NORM_TFIDF: 1.0}],
            'roots': [{COUNT: 1, NORM_COUNT: 1.0, DOCID: 2, TFIDF: tf_idf(1, 1, 2), NORM_TFIDF: 1.0}]
        }
        self.assertEqual(expected, index._invertedIndex)

    def test_Search(self):
        expected = [
            {COUNT: 1, DOCID: 1, NORM_COUNT: 0.5, TFIDF: 0.0, NORM_TFIDF: 0},
            {COUNT: 1, DOCID: 2, NORM_COUNT: 1.0, TFIDF: 0.0, NORM_TFIDF: 0}
        ]
        index = Index(
            os.path.dirname(os.path.realpath(__file__)) + "/test_data", IndexConfig())
        self.assertEqual([], index.search('thereShouldBeNoDocument'))
        self.assertEqual(expected, index.search('Language'))

    def test_IndexByDocId(self):
        data_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "test_data")
        index = Index(data_path, IndexConfig())
        expected = {
            END: 44,
            FILE: data_path,
            START: 0,
            WORDS: {
                'algebraic': {COUNT: 1, NORM_COUNT: 0.5, TFIDF: tf_idf(1, 1, 2), NORM_TFIDF: 1.0},
                'international': {COUNT: 1, NORM_COUNT: 0.5, TFIDF: tf_idf(1, 1, 2), NORM_TFIDF: 1.0},
                'language': {COUNT: 1, NORM_COUNT: 0.5, TFIDF: tf_idf(1, 2, 2), NORM_TFIDF: 0.0},
                'preliminary': {COUNT: 2, NORM_COUNT: 1.0, TFIDF: tf_idf(2, 1, 2), NORM_TFIDF: 1.0},
                'report': {COUNT: 1, NORM_COUNT: 0.5, TFIDF: tf_idf(1, 1, 2), NORM_TFIDF: 1.0}
            }
        }
        self.assertEqual({}, index.indexByDocId(404))
        self.assertEqual(expected, index.indexByDocId(1))
