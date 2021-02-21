"""
the main file
"""
from typing import Dict, List

import io_utils
import validation


def main(csv_file_path: str, column_name: str) -> str:
    """
    the main function
    :param csv_file_path: the csv's path
    :param column_name: the requested column name
    :return: the sorted file
    """
    parsed_csv: List[Dict[str, int or float]] = io_utils.parse_csv(csv_file_path)

    validation.validate_ads_columns(parsed_csv)

    sorted_csv: List[Dict[str, int or float]] = sorted(parsed_csv, key=lambda item: item[column_name].lower())

    out_file_path: str = io_utils.get_output_file_path(csv_file_path)

    io_utils.write_items_to_file(out_file_path, sorted_csv)

    return out_file_path
