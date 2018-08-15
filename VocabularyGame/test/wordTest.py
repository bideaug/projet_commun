import unittest
from classes.word import Word

class TestWord(unittest.TestCase):
    def setUp(self):
        self.word = Word("stellen", "mettre")

    def test_word1_creation(self):
        self.assertEqual("stellen", self.word.spelling["de"])
        self.assertEqual("mettre", self.word.spelling["fr"])

    def test_word1_as_no_options(self):
        self.assertEqual(3, len(self.word.options))
        self.assertEqual("", self.word.options["comment"])
        self.assertEqual("", self.word.options["inflection"])
        self.assertEqual("", self.word.options["plural"])

    def test_adding_an_option(self):
        self.word.setAnOption("comment","comment")
        self.assertEqual("comment", self.word.options["comment"])
        self.word.setAnOption("inflection","inflection")
        self.assertEqual("inflection", self.word.options["inflection"])
        self.word.setAnOption("plural","plural")
        self.assertEqual("plural", self.word.options["plural"])

    def test_trying_to_add_option_with_wrong_key_value(self):
        self.word.setAnOption("test","comment")
        self.assertRaises(KeyError)

    def test_semanticity_of_entity(self):
        copy = Word("stellen", "mettre")
        self.assertEqual(copy, self.word)
        self.assertNotEqual(copy, "coucou")

    def test_should_raise_exception_if_constructed_from_empty_string(self):
        with self.assertRaises(Exception) as context:
            Word("", "mettre")
        self.assertTrue("Cannot build a word from an empty data" in str(context.exception))


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestWord)



if __name__ == '__main__':
    unittest.main()
