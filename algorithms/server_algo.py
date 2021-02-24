"""
a file contains a server based ad selection algorithm
"""
import random
from typing import Dict, List, Tuple

from config import Config
from algorithms import ad_order


_ADS: List[Dict[str, int or float]] = []


def insert_ads(file_names: List[str]) -> None:
    """
    select ads from files
    :param file_names: the file's names
    :return: selected ads
    """
    for file_name in file_names:
        file_ads: List[Dict[str, int or str]] = ad_order.parse_csv(file_name)
        _ADS.extend(file_ads)


def select_ads(weights: List[Tuple[str, int]] = None) -> List[Dict[str, int or float]]:
    """
    select ads from "db"
    :param weights: the weights of the campaigns
    :return: selected ads
    """
    try:
        selected_ids: List[int] = _get_ad_ids(weights)

        selected_ads: List[Dict[str, int or float]] = [_format_ad(ad) for ad in _ADS if int(ad['id']) in selected_ids]

        return selected_ads

    except Exception as e:
        raise e


def _get_ad_ids(weights: List[Tuple[str, int]] = None) -> List[int]:
    """
    get ads ids
    :param weights: campaign weights
    :return: ids
    """
    selected_ids: List[int] = []

    # weights were not inserted
    if not weights:
        selected_ids = random.sample(range(0, len(_ADS)), Config.ADS_NUMBER)
        return selected_ids

    for weight in weights:
        weight_ids: List[int] = _get_weight_ads(weight)
        selected_ids.extend(weight_ids)

    return selected_ids


def _get_weight_ads(weight: Tuple[str, int]) -> List[int]:
    """
    get weights ads ids
    :param weight: the wight
    :return: the selected ads by weight
    """
    weight_ads: int = weight[1] * Config.ADS_NUMBER
    optional_ids: List[int] = [ad['id'] for ad in _ADS if ad['Campaign'] == weight[0]]

    if weight_ads > len(optional_ids):
        raise Exception('Bad request, wrong weight')

    selected_ids: List[int] = random.sample(optional_ids, weight_ads)

    return selected_ids


def _format_ad(ad: Dict[str, int or float]) -> Dict[str, int or float]:
    """
    format the ad
    :param ad: the ad
    :return: the formatted ad
    """
    return {key: val for key, val in ad.items() if key in Config.SERVER_REQUIRED_FIELDS}
