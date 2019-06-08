import utility_functions as UF
import file_management_functions as FMF


def list_image_paths(file_types):
    """
    Will list all the photos in the current directory and in all subdirectories.
    :param file_types: array of the supported file types
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
# print(list_image_paths(FMF.pre_import_file_types()))


def photo_exif_data(photo_paths):
    """
    Will get the exif data of a photo
    :param photo_path: the paths to the photos in the current directory
    :return: array of info
    """
    dictionaries = []
    for file in photo_paths:
        dictionary_elements = {}
        dictionary_elements["Current Path"] = file
        dictionary_elements["File Name"] = UF.get_subprocess_output(UF.run_command(["basename", file], True)).strip("\\n")
        dictionary_elements["New Path"] = FMF.new_file_path(UF.file_creation_date(file))
        dictionary_elements["Creation Date"] = UF.file_creation_date(file)
        dictionaries.append(dictionary_elements)
    return dictionaries