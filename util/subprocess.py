import subprocess


def get_subprocess_output(command):
    """
    Will get the output of a subprocess command that has been ran.
    :param command: the command that was recorded.
    :return: the command's output
    """
    raw_output_section = raw_subprocess_output.split(",")[3]
    complete_output = raw_output_section[8:]
    return complete_output


# Testing:
print(get_subprocess_output(subprocess.run(['ls', '-R'], capture_output=True)))
