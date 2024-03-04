# test_pdf.py
import unittest
import os

def is_pdf(filename):
    return filename.lower().endswith('.pdf')
class TestIsPDF(unittest.TestCase):

    def test_pdf(self):
        relative_path = os.getcwd()
        if relative_path[len(relative_path) - 5:] == 'tests':
            directory = '../work/dataset'
        else:
            directory = './work/dataset'
        for filename in os.listdir(directory):
            self.assertTrue(is_pdf(filename), f"{filename} is not recognized as a PDF file")

if __name__ == '__main__':
    unittest.main()
