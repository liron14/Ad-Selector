"""
the main file
"""
import algorithms


def main(csv_file_path: str, column_name: str) -> None:
    """
    the main function
    :param csv_file_path: the csv's path
    :param column_name: the requested column name
    :return: the sorted file
    """
    algorithms.order_ads_limited(csv_file_path, column_name)


CSV_PATH: str = r"C:\Users\Liron\Desktop\Interviews\Refael\‏‏example_ad_file_limited.csv"
COLUMN_NAME: str = 'Id'

main(CSV_PATH, COLUMN_NAME)
x = 5
