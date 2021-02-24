"""
a file contains config
"""
from typing import Dict, List


class Config:
    REQUIRED_FIELDS: Dict[str, type] = {
        'Index': str,
        'Id': str,
        'Name': str,
        'Description': str,
        'Category': str,
        'Campaign': str,
        'Url': str,
        'Nurl': str,
        'CustomerName': str,
    }

    SERVER_REQUIRED_FIELDS: List[str] = ['id', 'name', 'campaign', 'url', 'nurl']

    ADS_NUMBER: int = 10
