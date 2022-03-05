# main.py
# -------------------------------------------------------------------------------------------------
# Megaventory Internship Project
# name: George Tservenis
# date: 04-03-2022
# -------------------------------------------------------------------------------------------------

from enum import Enum
import requests
import json

api_key = "3974d8451ecede7d@m128220"

# Global info for requests
base_url = "https://api.megaventory.com/v2017a"
headers = {"Content-Type": "application/json"}


class Product:

    def __init__(self, sku: str, description: str) -> None:
        self.product_id = -1
        self.sku = sku
        self.description = description
        self.sales_price = 0.00
        self.purchase_price = 0.00

    def mv_product(self) -> dict:
        return {"ProductSKU": self.sku,
                "ProductDescription": self.description,
                "ProductSellingPrice": self.sales_price,
                "ProductPurchasePrice": self.purchase_price}


class Supplier:

    def __init__(self, name: str) -> None:
        self.name = name
        self.email = ""
        self.shipping_address = ""
        self.phone = ""


class Client:

    def __init__(self, name: str) -> None:
        self.name = name
        self.email = ""
        self.shipping_address = ""
        self.phone = ""


class InventoryLocation:

    def __init__(self, abbreviation: str, full_name: str) -> None:
        self.abbreviation = abbreviation
        self.full_name = full_name
        self.address = ""


class Tax:

    def __init__(self, name: str, percent: float) -> None:
        self.name = name
        self.description = ""
        self.percent = percent


class Discount:

    def __init__(self, name: str, percent: float) -> None:
        self.name = name
        self.description = ""
        self.percent = percent


# class OrderStatus(Enum):
#     PENDING = 1
#     APPROVED = 2
#     SHIPPED = 3
#     INVOICED = 4
#     CLOSED = 5
#
#
# class SalesOrder:
#
#     def __init__(self, order_id: int, no: int, status: OrderStatus) -> None:
#         self.order_id = order_id
#         self.no = no
#         self.status = status


def api_key_verify(key: str) -> str:
    data = {"APIKEY": api_key}
    response = requests.post(f"{base_url}/APIkey/APIkeyGet", headers=headers, json=data)
    return response.json()


def insert_product(product: Product, ext_app: str) -> str:
    data = {"APIKEY": api_key,
            "mvProduct": product.mv_product(),
            "mvRecordAction": "Insert"}

    if ext_app != "":
        # The ProductUpdate was triggered by an external application.
        data["mvInsertUpdateDeleteSourceApplication"] = ext_app

    response = requests.post(f"{base_url}/Product/ProductUpdate", headers=headers, json=data)

    # Store the ProductID that was assigned.
    product.product_id = response.json()["mvProduct"]["ProductID"]

    return response.json()["ResponseStatus"]["ErrorCode"]


if __name__ == '__main__':

    p = Product("PRODUCT_103", "Description")
    print(p.product_id)
    print(insert_product(p, ""))
    print(p.product_id)
