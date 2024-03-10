import re
import os
from colorama import Fore, Back, Style

SERIES_LIST = [
    ["Dragonball", "original"],
    ["Dragonball Z", "z"],
    ["Dragonball Z Kai", "z_kai"],
    ["Dragonball GT", "gt"],
    ["Dragonball Super", "super"],
]
SUPPORTED_FILE_EXTENSIONS = ["mkv", "mp4"]
INVALID_EPISODE_NUMBER_ERROR = "File should have an episode number"
INVALID_EXTENSION_ERROR = "File should have an extension"
UNSUPPORTED_FILE_EXTENSIONS_ERROR = f"Unsupported file extension. Only the following file extensions are supported: {', '.join(SUPPORTED_FILE_EXTENSIONS)}"


def main(directory, series=None):
    series_folder = os.listdir(directory)[0].split("/")[-1]

    if not series:
        series = get_series_code_from_directory(directory)

    for file in os.listdir(f"{directory}/{series_folder}"):
        new_file = get_cleaned_file_name(file, series)

        if file != new_file:
            os.rename(
                f"{directory}/{series_folder}/{file}",
                f"{directory}/{series_folder}/{new_file}",
            )

            print(file, "->", new_file, "|", Fore.GREEN, f"success", Style.RESET_ALL)

        else:
            print(new_file, "|", Fore.YELLOW, "skipped", Style.RESET_ALL)


def get_cleaned_file_name(file, series=None):
    file_name = ""

    episode_number = get_episode_number(file)
    extension = get_file_extension(file)

    if series == "original":
        file_name = f"db-{episode_number}.{extension}"
    else:
        file_name = f"db-{series}-{episode_number}.{extension}"

    return file_name


def get_episode_number(file):
    match = re.search(r"\d+", file)
    if match:
        number = int(match.group(0))
        padded_number_str = str(number).zfill(3)

        return padded_number_str

    raise ValueError(INVALID_EPISODE_NUMBER_ERROR)


def get_file_extension(file=None):

    file_parts = file.split(".")
    extension = file_parts[-1].lower()

    if len(file_parts) > 1:
        if extension in SUPPORTED_FILE_EXTENSIONS:
            return extension

        raise ValueError(UNSUPPORTED_FILE_EXTENSIONS_ERROR)

    raise ValueError(INVALID_EXTENSION_ERROR)


def get_series_code_from_directory(directory):
    series_folder = os.listdir(directory)[0].split("/")[-1]
    for name, code in SERIES_LIST:
        if name.lower() == series_folder.lower():
            return code


if __name__ == "__main__":
    root_directory = f"data"
    main(root_directory)
