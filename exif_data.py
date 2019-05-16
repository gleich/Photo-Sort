import json
import utility_functions as UF


def list_image_paths():
    """
    Will list all the photos in the current directory and in all subdirectories.
    :return: array of the photo paths
    """
    files = []
    with open("supported_file_types.json") as supported_file_types:
        file_types = json.load(supported_file_types)
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
# list_image_paths()
