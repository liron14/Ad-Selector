"""
a file contains parsing utils
"""
import csv
import os
from typing import List, Dict


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


def write_items_to_file(file_path: str, items: List[Dict[str, int or float]]) -> None:
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


def get_output_file_path(file_path: str) -> str:
    """
    get the output file's path
    :param file_path: the file path
    :return: the output file's path
    """
    split_file_path: List[str] = list(os.path.splitext(file_path))
    return f'{split_file_path[0]}_sorted{split_file_path[1]}'
