import subprocess


def get_subprocess_output(command):
    """
    Will get the output of a command that has been ran
    :param command: the command that was recorded.
    :return: the command's output
    """



def list_Images():
    """
    Will list all of the photos in the current directory and the subdirectories.
    :return: array listing all the paths of the images (Files in the current directory will will be listed with just their file name).
    """
    raw_subprocess_output = subprocess.run(['ls', '-R'], capture_output=True)
    raw_output_section = raw_subprocess_output.split(",")[3]
    complete_output = raw_output_section[8:]
    raw_output_items = complete_output.split("\n")
    out_put_items = []  # Removes blank instances
    for i in range(raw_output_items):
        if len(raw_output_items[i]) < 1:
            raw_output_items.pop(i)
        elif "/"





    CompletedProcess(args=['ls', '-R'], returncode=0, stdout=b'child_folder\npython.py\nscript.sh\n\n./child_folder:\nchild_file.txt\n', stderr=b'')
