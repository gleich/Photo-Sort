import photo_functions
import file_management_functions


def main():
    """
    Runs main
    """
    types = file_management_functions.pre_import_file_types()
    file_management_functions.cd_into_drive()
    print(photo_functions.list_image_paths(types))


main()
