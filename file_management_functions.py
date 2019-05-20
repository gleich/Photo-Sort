import subprocess
import utility_functions as UF


def cd_into_drive():
    """
    Will change the current directory into the directory of the drive that will be used.
    :param name: the name of the drive that will be used.
    """
    UF.run_command(["cd", ["photos"]], False)
    current_directory = UF.get_subprocess_output(UF.run_command(["pwd"], True))
    return current_directory


# Testing:
print(cd_into_drive())
