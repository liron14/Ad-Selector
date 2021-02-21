"""
a file contains config
"""
from typing import Dict

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
