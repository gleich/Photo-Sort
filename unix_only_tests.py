import unittest
import utility_functions


class TestUnixOnlyFunctions(unittest.TestCase):
    """
    Testing unix only functions. The reason that they are seperate from the travis_ci_tests is because travis CI runs the test in a linux enviroment, so they can't be stored there.
    """

    def test_get_file_creation_date(self):
        """
        Tests the get_file_creation_date funtion
        """
        result = utility_functions.file_creation_date('./photos/test_image.jpg')
        self.assertEqual(str(type(result)), "<class 'list'>")
        self.assertEqual(str(type(result[0])), "<class 'int'>")
        self.assertEqual(str(type(result[1])), "<class 'int'>")
        self.assertEqual(str(type(result[2])), "<class 'int'>")
        self.assertEqual(result[0], 5)
        self.assertEqual(result[1], 13)
        self.assertEqual(result[2], 2019)
