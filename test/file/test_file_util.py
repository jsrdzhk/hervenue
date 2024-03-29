# !/usr/bin/env python3
# -*-coding:utf-8 -*-

"""
# File       : test_file_util.py
# Time       ：2020/8/19 15:53
# Author     ：Rodney Cheung
"""
import os
import unittest

from test.testdata.test_util import TestUtil
from hervenue.file.file import FileUtil


class TestFileUtil(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.test_data_path = os.path.join(TestUtil.get_test_data_path(), 'file', 'file_reader')

    def test_last_line(self):
        line = FileUtil.last_line(os.path.join(self.test_data_path, 'mitmproxy-ca-cert.pem'))
        self.assertEqual(line, '-----END CERTIFICATE-----')

    def test_read_file_by_encoding(self):
        print(FileUtil.read_file_by_encoding(os.path.join(self.test_data_path, 'mitmproxy-ca-cert.pem')))

    def test_first_line(self):
        line = FileUtil.first_line(os.path.join(self.test_data_path, 'mitmproxy-ca-cert.pem'))
        self.assertEqual(line, '-----BEGIN CERTIFICATE-----')


if __name__ == '__main__':
    unittest.main()
