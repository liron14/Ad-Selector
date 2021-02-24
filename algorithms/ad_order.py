"""
a file contains ad order by given field algorithm
"""
from typing import Dict, List

import csv

import io_utils
import validation


def order_ads(csv_file_path: str, column_name: str) -> str:
    """
    the main function
    :param csv_file_path: the csv's path
    :param column_name: the requested column name
    :return: the sorted file
    """
    parsed_csv: List[Dict[str, int or float]] = parse_csv(csv_file_path)

    validation.validate_ads_columns(parsed_csv)

    sorted_csv: List[Dict[str, int or float]] = sorted(parsed_csv, key=lambda item: item[column_name].lower())

    out_file_path: str = io_utils.get_output_file_path(csv_file_path)

    _write_items_to_file(out_file_path, sorted_csv)

    return out_file_path


def parse_csv(csv_path: str) -> List[Dict[str, str or int]]:
    """
    validate the csv
    :param csv_path: the csv's path
    """
    csv_as_list: List[Dict[str, str or int]]

    try:
        csv_as_list: List[Dict[str, str or int]] = _parse_csv_as_list(csv_path)
    except Exception as e:
        raise Exception(f'Could not parse file: {str(e)}')

    # failed to parse or empty file
    if not csv_as_list:
        raise Exception(f'File is empty or could not be parsed')

    return csv_as_list


def _parse_csv_as_list(csv_path: str) -> List[Dict[str, str or int]]:
    """
    parse the csv as a dict
    :param csv_path: the csv's path
    :return: a parsed dict
    """
    csv_as_dict: List[Dict[str, str or int]]

    # read file
    with open(csv_path, newline='') as csv_file:
        reader: csv.DictReader = csv.DictReader(csv_file)
        # the if condition excludes the titles line
        csv_as_dict = [dict(row) for row in reader if row['Id'] != '']

    return csv_as_dict


def _write_items_to_file(file_path: str, items: List[Dict[str, int or float]]) -> None:
    """
    write the items to the file
    :param file_path: the file's path
    :param items: the items to write
    """
    with open(file_path, mode='w', newline='') as csv_file:
        # get the field names
        field_names: List[str] = list(items[0].keys())

        writer: csv.DictWriter = \
            csv.DictWriter(csv_file, fieldnames=field_names, dialect='excel')

        for item in items:
            writer.writerow(item)
