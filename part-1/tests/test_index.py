import pytest
import re

from src.index import (
    get_file_extension,
    get_episode_number,
    get_cleaned_file_name,
    UNSUPPORTED_FILE_EXTENSIONS_ERROR,
    INVALID_EXTENSION_ERROR,
    INVALID_EPISODE_NUMBER_ERROR,
)


def test_get_file_extension_returns_an_extension_when_a_valid_file_is_passed_in():
    assert get_file_extension("Dragonball Z 182 - Gohan's Plea.mkv") == "mkv"


def test_get_file_extension_raises_an_error_when_a_file_without_an_extension_is_passed_in():
    with pytest.raises(ValueError, match=INVALID_EXTENSION_ERROR):
        get_file_extension("dbzwhisrocks blogspot com DBS Dubbed Ep 028")


def test_get_file_extension_returns_an_extension_in_lowecase_when_a_valid_file_is_passed_in():
    assert get_file_extension("Dragonball Z 182 - Gohan's Plea.MKV") == "mkv"


def test_get_file_extension_raises_an_error_when_file_with_unsupported_extension_is_passed_in():
    with pytest.raises(ValueError, match=UNSUPPORTED_FILE_EXTENSIONS_ERROR):
        get_file_extension("dbzwhisrocks.blogspot.com.DBS.Dubbed Ep 028.png")


def test_get_episode_number_returns_an_episode_number_str():
    assert get_episode_number("Dragonball Z 182 - Gohan's Plea.mkv") == "182"


def test_get_episode_number_raises_an_error__when_a_file_without_an_episode_number_is_passed_in():
    with pytest.raises(ValueError, match=INVALID_EPISODE_NUMBER_ERROR):
        assert get_episode_number("Dragonball Z - Gohan's Plea.mkv") == ""


def test_get_episode_number_returns_a_correctly_padded_episode_number_str():
    assert (
        get_episode_number("Dragonball 001 - The Secret Of The Dragon Balls.mkv")
        == "001"
    )


def test_get_episode_number_returns_a_left_padded_episode_number_str():
    assert get_episode_number("Dragonball GT 32 The Return Of Uub.mkv") == "032"


def test_get_cleaned_file_name_returns_cleaned_file_name():
    assert (
        get_cleaned_file_name("Dragonball 001 - The Secret Of The Dragon Balls.mkv")
        == "db-001.mkv"
    )


def test_get_cleaned_file_name_returns_cleaned_file_name_when_series_is_included():
    assert (
        get_cleaned_file_name(
            "dbzwhisrocks.blogspot.com.DBS.Dubbed Ep 028.MP4", "super"
        )
        == "db-super-028.mp4"
    )
