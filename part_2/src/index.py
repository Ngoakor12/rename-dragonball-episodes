import re
import os

SUPPORTED_FILE_EXTENSIONS = ["mkv", "mp4"]
INVALID_EPISODE_NUMBER_ERROR = "File should have an episode number"
INVALID_EXTENSION_ERROR = "File should have an extension"
UNSUPPORTED_FILE_EXTENSIONS_ERROR = f"Unsupported file extension. Only the following file extensions are supported: {', '.join(SUPPORTED_FILE_EXTENSIONS)}"


def main(directory, series=None):
    cleaned_file_names = []
    for file in directory:
        cleaned_file_names.append(get_cleaned_file_name(file, series))

    return cleaned_file_names


def get_cleaned_file_name(file, series=None):
    file_name = ""

    episode_number = get_episode_number(file)
    extension = get_file_extension(file)

    if series:
        file_name = f"db-{series}-{episode_number}.{extension}"

        return file_name

    file_name = f"db-{episode_number}.{extension}"

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


if __name__ == "__main__":
    directory = os.listdir("data")
    print(main(directory, "z"))
