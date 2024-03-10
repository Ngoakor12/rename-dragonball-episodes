import re


SUPPORTED_FILE_EXTENSIONS = ["mkv", "mp4"]
INVALID_EPISODE_NUMBER_ERROR = "File should have an episode number"
INVALID_EXTENSION_ERROR = "File should have an extension"
UNSUPPORTED_FILE_EXTENSIONS_ERROR = f"Unsupported file extension. Only the following file extensions are supported: {', '.join(SUPPORTED_FILE_EXTENSIONS)}"


def main(files, series=None):
    cleaned_file_names = []
    for file in files:
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
    db_file_names = [
        "Dragonball 001 - The Secret Of The Dragon Balls.mkv",
    ]
    db_z_file_names = [
        "Episode 159.MP4",
        "Dragonball Z 182 - Gohan's Plea.mkv",
    ]
    db_z_kai_file_names = [
        "Episode 167.MP4",
        "Dragon ball Z kai 117.mp4",
    ]

    db_gt_file_names = ["Dragonball GT 32 The Return Of Uub.mkv"]
    db_super_file_names = [
        "Dragonball 001 - The Secret Of The Dragon Balls.mkv",
    ]

    db_z = "z"
    db_z_kai = "z_kai"
    db_gt = "gt"
    db_super = "super"

    print("db:", db_gt_file_names, "->", main(db_gt_file_names))
    print(db_z, ":", db_z_file_names, "->", main(db_z_file_names, db_z))
    print(db_z_kai, ":", db_z_kai_file_names, "->", main(db_z_kai_file_names, db_z_kai))
    print(db_gt, ":", db_gt_file_names, "->", main(db_gt_file_names, db_gt))
    print(db_super, ":", db_super_file_names, "->", main(db_super_file_names, db_super))
