import unittest
from classes.levelManager import LevelManager

class TestLevelManager(unittest.TestCase):
    def setUp(self):
        self.levelManager = LevelManager()

    def test_object_created_as_expected(self):
        self.assertEqual(self.levelManager.availableLevelList, self.levelManager.getAvailableLevelList())
        self.assertEqual(self.levelManager.selectedLevel, 0)

def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestLevelManager)

if __name__ == '__main__':
    unittest.main()
