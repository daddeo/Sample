# Duck typing, mock objects and Monkey patching
# http://www.voidspace.org.uk/python/articles/introduction-to-unittest.shtml

import unittest
from mock import Mock, patch, sentinel

from reader import Reader


class TestReader(unittest.TestCase):
    def setUp(self):
        self.myReader = Reader()

    def test_Constructor(self):
        "Test the default state"
        self.assertEqual(self.myReader.data, None)

    def test_ReadData(self):
        source = Mock()
        source.read.return_value = "some data"

        self.myReader.readData(source)

        self.assertEqual(self.myReader.data, "some data")
        self.assertTrue(source.read.called)
        self.assertTrue(source.close.called)

    def test_Mock1(self):
        mock = Mock()
        mock.method.return_value = "foo"

        self.assertTrue(mock.method(1, 2, 3, 4), "foo")
        self.assertTrue(mock.method.called)
        with self.assertRaises(AssertionError):
            mock.method.assert_called_with(8, 6)

    def test_Mock2(self):
        mock = Mock()
        mock.side_effect = Exception("Boom!")

        with self.assertRaises(Exception):
            mock()

        results = [1, 2, 3]

        def side_effect(*args, **kwargs):
            return results.pop()

        mock.side_effect = side_effect
        self.assertEqual(mock(), 3)
        self.assertEqual(mock(), 2)
        self.assertEqual(mock(), 1)

    def test_Synchronise(self):
        # put the monkey patching in place
        self.myReader.getDataSource = Mock()
        self.myReader.getDataSource.return_value = sentinel.DataSource

        self.myReader.readData = Mock()
        self.myReader.store = Mock()

        # make the call
        self.myReader.synchronise()

        # assertions
        self.assertTrue(self.myReader.getDataSource.called)
        self.myReader.readData.assert_called_with(sentinel.DataSource)
        self.assertTrue(self.myReader.store.called)

    @patch("reader.DataSource")
    def test_Sychronise2(self, MockDataSource):
        MockDataSource.return_value = sentinel.DataSource
        source = self.myReader.getDataSource()
        self.assertEquals(source, sentinel.DataSource)
