import unittest
import exif_data


class TestExifData(unittest.TestCase):
    """
    Will test all the function in the file exif_data.py
    """

    def test_run_command(self):
        """
        Tests the run_command function
        """
        result = exif_data.run_command(["pwd"], True)
        self.assertEqual(str(type(result)), "<class 'subprocess.CompletedProcess'>")


    def test_get_subprocess_output(self):
        """
        Tests the get_subprocess_output function
        """
        result = exif_data.get_subprocess_output(exif_data.run_command(["pwd"], True))
        self.assertEqual(str(type(result)), "<class 'str'>")


    def test_list_image_paths(self):
        """
        Tests the list_image_paths function
        """
        result = exif_data.list_image_paths()
        self.assertEqual(str(type(result)), "<class 'list'>")


if __name__ == '__main__':
    unittest.main()
