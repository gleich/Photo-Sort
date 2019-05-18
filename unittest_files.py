import unittest
import photo_functions
import utility_functions


class TestExifData(unittest.TestCase):
    """
    Will test all the function in the file photo_functions.py
    """

    ###############################################
    #Testing the functions in utility_functions.py#
    ###############################################

    # Subprocess functions:
    def test_run_command(self):
        """
        Tests the run_command function
        """
        result = utility_functions.run_command(["pwd"], True)
        self.assertEqual(str(type(result)), "<class 'subprocess.CompletedProcess'>")


    # Subprocess functions:
    def test_get_subprocess_output(self):
        """
        Tests the get_subprocess_output function
        """
        result = utility_functions.get_subprocess_output(utility_functions.run_command(["pwd"], True))
        self.assertEqual(str(type(result)), "<class 'str'>")


    def test_list_to_dict(self):
        """
        Tests the list_to_dict function
        """
        result = utility_functions.list_to_dict(["a", "b", "c", "d"])
        self.assertEqual(str(type(result)), "<class 'dict'>")
        self.assertEqual(len(result), 2)
        self.assertEqual(result["a"], "b")
        self.assertEqual(result["c"], "d")


    def test_get_file_creation_date(self):
        """
        Tests the get_file_creation_date funtion
        """
        result = utility_functions.file_creation_date('./photos/test_image.jpg')
        self.assertEqual(str(type(result)), "<class 'list'>")
        self.assertEqual(str(type(result[0])), "<class 'int'>")
        self.assertEqual(str(type(result[1])), "<class 'int'>")
        self.assertEqual(str(type(result[2])), "<class 'int'>")
        self.assertEqual(str(type(result[0])), 5)
        self.assertEqual(str(type(result[0])), 13)
        self.assertEqual(str(type(result[0])), 2019)


    ###############################################
    #Testing the functions in photo_functions.py#
    ###############################################

    def test_list_image_paths(self):
        """
        Tests the list_image_paths function
        """
        result = photo_functions.list_image_paths()
        self.assertEqual(str(type(result)), "<class 'list'>")


if __name__ == '__main__':
    unittest.main()
