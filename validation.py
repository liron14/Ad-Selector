"""
a file contains validation methods
"""
from typing import Dict, List

import config


def validate_ads_columns(ads: List[Dict[str, int or float]]) -> None:
    """
    validate ads
    :param ads: the ads
    """
    for ad in ads:
        if len(ad) != len(config.REQUIRED_FIELDS):
            raise Exception('Incompatible ad fields')

        for column_name, column_value in ad.items():
            _validate_ad_values(column_name, column_value)


def _validate_ad_values(column_name: str, column_value: str or int) -> None:
    """
    validate a csv column
    :param column_name: the column's name
    :param column_value: the column's type
    """
    if 'Index' in column_name:
        if type(column_value) != config.REQUIRED_FIELDS['Index']:
            raise Exception(f'Incompatible column: {column_name}')
        return

    if column_name not in config.REQUIRED_FIELDS.keys():
        raise Exception('Incompatible column name')

    if config.REQUIRED_FIELDS[column_name] != type(column_value):
        raise Exception(f'Incompatible column: {column_name}')

