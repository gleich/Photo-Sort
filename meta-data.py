from util import subprocess_functions


def list_Images():
    """
    Will list all of the photos in the current directory and the subdirectories.
    :return: array listing all the paths of the images (Files in the current directory will will be listed with just their file name).
    """
    raw_subprocess_output = subprocess_functions.run(['ls', '-R'], capture_output=True)
    raw_output_section = raw_subprocess_output.split(",")[3]
    complete_output = raw_output_section[8:]
    raw_output_items = complete_output.split("\n")
    out_put_items = []  # Removes blank instances
    for i in range(raw_output_items):
        if len(raw_output_items[i]) < 1:
            raw_output_items.pop(i)
        elif "/"





    
