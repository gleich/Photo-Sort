import photo_functions as PF
import file_management_functions as FMF


def main():
    """
    Runs main
    """
    file_types = FMF.pre_import_file_types()
    FMF.cd_into_drive()
    image_paths = PF.list_image_paths(file_types)
    exif_data = PF.photo_exif_data(image_paths)
    FMF.init_folders(exif_data)
    FMF.put_photos_in_folders(exif_data)


main()
