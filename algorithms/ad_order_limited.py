"""
a file contains ad order by given field algorithm with limited memory use
"""
from typing import List

import csv
import csvsorter

import io_utils


def order_ads_limited(csv_file_path: str, column_name: str) -> str:
    """
    the main function
    :param csv_file_path: the csv's path
    :param column_name: the requested column name
    :return: the sorted file
    """
    column_id: int = _get_column_id(csv_file_path, column_name)
    out_file_path: str = io_utils.get_output_file_path(csv_file_path)

    csvsorter.csvsort(csv_file_path, [column_id], output_filename=out_file_path, max_size=2000)

    return out_file_path


def _get_column_id(csv_path: str, column_name: str) -> int:
    """
    parse the csv as a dict
    :param csv_path: the csv's path
    :return: a parsed dict
    """
    # read file
    with open(csv_path, newline='') as csv_file:
        reader: csv.DictReader = csv.DictReader(csv_file)
        # the if condition excludes the titles line
        ids: List[str] = list(reader.fieldnames)

    requested_column_id: int = ids.index(column_name)

    return requested_column_id
