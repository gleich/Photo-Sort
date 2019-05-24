import utility_functions as UF
import file_management_functions as FMF
import json


def list_image_paths(file_types):
    """
    Will list all the photos in the current directory and in all subdirectories.
    :param file_types:
    :return: array of the photo paths
    """
    files = []
    for extension in file_types:
        command_to_run = ['find', '.', '-iname', '*' + extension + '']
        ran_command = UF.run_command(command_to_run, True)
        command_output = UF.get_subprocess_output(ran_command)
        if "\\n" in command_output:
            file_paths = command_output.split("\\n")
            for file in file_paths:
                if file != '':
                    strip_1 = file.strip("\\n")
                    files.append(strip_1)
        else:
            if command_output != '':
                files.append(command_output)
    return files


# Testing
# Please import FMF before running the command below:
# list_image_paths(FMF.pre_import_file_types())


def photo_exif_data(photo_paths):
    """
    Will get the exif data of a photo
    :param photo_path: the paths to the photos in the current directory
    :return: array of info
    """
    dictionaries = []
    for file in photo_paths:
        command_to_run = UF.run_command(["exiftool", file], True)
        ran_command = UF.get_subprocess_output(command_to_run)
        raw_elements = ran_command.split("\\n")
        elements = []
        for element in raw_elements:
            parts = element.split(":", 1)
            for part in parts:
                stripped_part = part.strip()
                elements.append(stripped_part)
        elements.pop(-1)
        raw_dict = UF.list_to_dict(elements)
        dictionary_elements = {}
        image_size_sum = 0
        for string in raw_dict["Image Size"].split("x"):
            number_form = int(string)
            image_size_sum += number_form
        dictionary_elements["Photo Path"] = file
        dictionary_elements["File Type"] = raw_dict["File Type"]
        dictionary_elements["Image Size"] = raw_dict["Image Size"]
        dictionary_elements["Image Size Sum"] = image_size_sum
        dictionary_elements["New Path"] = FMF.get_new_file_path(UF.file_creation_date(file))
        dictionary_elements["Creation Date"] = UF.file_creation_date(file)
    return dictionaries


# Testing
# print(photo_exif_data(list_image_paths(FMF.pre_import_file_types())))
