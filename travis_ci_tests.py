import unittest
import photo_functions
import utility_functions


class TestTravisCI(unittest.TestCase):
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


    def test_find_index(self):
        """
        Test to the find_index function
        """
        result = utility_functions.find_index("Volume", ["Item1", "Item2", "Item3", "Volume"])
        failed_result = utility_functions.find_index("Volume", ["Item1", "Item2", "Item3"])
        self.assertEqual(str(type(result)), "<class 'int'>")
        self.assertEqual(result,3)
        self.assertEqual(result,3)
        self.assertEqual(failed_result, None)


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
