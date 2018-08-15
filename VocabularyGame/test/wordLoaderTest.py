import unittest
from classes.wordLoader import WordLoader

class TestWordLoader(unittest.TestCase):
    def setUp(self):
        self.wordLoader = WordLoader("./test/sampleTestData/data.json", "json")

    def test_object_created_as_expected(self):
        self.assertEqual(self.wordLoader.pathToData, "./test/sampleTestData/data.json")
        self.assertEqual(self.wordLoader.dataFormat, "json")



def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestWordLoader)

if __name__ == '__main__':
    unittest.main()
