from dataclasses import dataclass
from random import random
from enum import Enum
import openfoodfacts
from requests import ConnectionError
import logging
from dependency_sdk import SDKBuilder, SDKVersion, Product
from foodfacts import api

logger = logging.getLogger(__name__)

NO_BUILDER_PROVIDED = None
SDK_VERSION = SDKVersion.v1


class OpenfoodfactAdapter:
    def __init__(self, sdk_builder: SDKBuilder=NO_BUILDER_PROVIDED):
        if sdk_builder is NO_BUILDER_PROVIDED:
            self.sdk_builder = SDKBuilder()
        else:
            self.sdk_builder = sdk_builder

    def _get_product_id(self, product_name: str):
        return {
            "nutella": "59032823",
            "cantal": "3492847922008",
            "flocons d'avoines": "3229820019307",
            "lentilles": "3017800078853",
            "margherita": "8008698026090",
            "spaghetti": "8076800195057",
            "beurre": "3412290015980",
            "laitue": "3560070372997",
            "miel": "3088540255279",
            "saucisson":"3245390021298",
            "aligot": "3245390134721"
        }[product_name]
