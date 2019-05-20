import utility_functions as UF
import file_management_funcitons as FMF


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
# list_image_paths(FMF.pre_import_file_types())


def photo_exif_data(photo_path):
    """
    Will get the exif data of a photo
    :param photo_path: the path to the photo in the current directory
    :return: array of info
    """
    command_to_run = UF.run_command(["exiftool", photo_path], True)
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
    dictionary_elements["Photo Path"] = photo_path
    dictionary_elements["File Type"] = raw_dict["File Type"]
    dictionary_elements["Image Size"] = raw_dict["Image Size"]
    dictionary_elements["Image Size Sum"] = image_size_sum
    try:
        dictionary_elements["Creation Date"] = UF.file_creation_date(photo_path)
    except ValueError:
        pass
    return dictionary_elements


# Testing
# print(photo_exif_data('./photos/test_image.jpg'))


def write_data_to_JSON(photo_paths_lst):
    """
    Will get the exif data for a list of photos and write their data to a JSON file
    :param photo_paths_lst: List of the path to all the photos.
    """
    elements_to_dump = []
    for photo in photo_paths_lst:
        exif_data = photo_exif_data(photo)
        elements_to_dump.append(exif_data)
    with open("exif_data.json", "w") as json_file:
        json.dump(elements_to_dump, json_file)


# Testing:
# write_data_to_JSON(list_image_paths())
