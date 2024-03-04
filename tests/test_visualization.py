# test_visualization.py
import unittest
import os
from work.utils import count_figure

class test_output(unittest.TestCase):

    def test_output(self):

        filename = 'exemple_pdf1.grobid.tei.xml'
        directory = "./input_files"

        file_path = os.path.join(directory, filename)

        self.assertEqual(3, count_figure(file_path))


if __name__ == '__main__':
    unittest.main()