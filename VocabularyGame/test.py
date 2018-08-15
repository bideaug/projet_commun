import unittest
import test.wordTest as wordTests
import test.wordLoaderTest as wordLoaderTests
import test.levelManagerTest as levelManagerTests

allWordTests = unittest.TestSuite(wordTests.suite())
allWordLoadersTests = unittest.TestSuite(wordLoaderTests.suite())
allLevelManagerTests = unittest.TestSuite(levelManagerTests.suite())

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(allWordTests)
    unittest.TextTestRunner(verbosity=2).run(allWordLoadersTests)
    unittest.TextTestRunner(verbosity=2).run(allLevelManagerTests)
