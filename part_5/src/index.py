import re
import os
import sys
import shutil
from colorama import Fore, Style

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


def main():
    env_vars = sys.argv[1:]
    source_path = env_vars[0]
    target_path = env_vars[1]

    # create parent directory if it doesn't exist
    parent_dir = "dragonball-series"
    if not (os.path.isdir(parent_dir)):
        print(f"--- creating parent directory: /{parent_dir} ---")
        os.mkdir(parent_dir)

    # create sub-directories if they don't exist yet
    for series in SERIES_LIST:
        series_dir = get_cleaned_series_directory_path(series[0])
        series_dir_path = os.path.join(target_path, series_dir)
        if not (os.path.isdir(series_dir_path)):
            print(f"--- creating series directory: /{series_dir} ---")
            os.mkdir(series_dir_path)

    if not (source_path and target_path):
        raise Exception("source and or target paths missing!")

    for current_dir, dirs, files in os.walk(source_path):
        series_directory = current_dir.split("/")[-1]
        series = get_series_code_from_directory(series_directory)

        if files and series:
            for current_file in files:
                current_file_path = os.path.join(current_dir, current_file)

                new_file = get_cleaned_file_name(current_file, series)
                new_file_path = os.path.join(
                    target_path,
                    get_cleaned_series_directory_path(current_dir.split("/")[-1]),
                    new_file,
                )
                print("#2", current_file_path)
                print("#3", new_file_path)
                shutil.copy2(
                    current_file_path,
                    new_file_path,
                )

                print(
                    current_file,
                    "->",
                    new_file,
                    "|",
                    Fore.GREEN,
                    f"success",
                    Style.RESET_ALL,
                )


def get_cleaned_file_name(file, series="original"):
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
    for name, code in SERIES_LIST:
        if name.lower() == directory.lower():
            return code


def get_cleaned_series_directory_path(series):
    return "-".join(series.lower().split())


if __name__ == "__main__":
    main()
