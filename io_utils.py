"""
a file contains parsing utils
"""
import os
from typing import List


def get_output_file_path(file_path: str) -> str:
    """
    get the output file's path
    :param file_path: the file path
    :return: the output file's path
    """
    split_file_path: List[str] = list(os.path.splitext(file_path))
    return f'{split_file_path[0]}_sorted{split_file_path[1]}'
