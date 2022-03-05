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
        self.record_id = -1
        self.sku = sku
        self.description = description
        self.sales_price = 0.00
        self.purchase_price = 0.00

    def record_dict(self) -> dict:
        return {"ProductSKU": self.sku,
                "ProductDescription": self.description,
                "ProductSellingPrice": self.sales_price,
                "ProductPurchasePrice": self.purchase_price}


class SCType(Enum):
    SUPPLIER = 1
    CLIENT = 2
    SnC = 3


class SupplierClient:

    def __init__(self, name: str, sc_type: SCType) -> None:
        self.record_id = -1
        self.sc_type = sc_type
        self.name = name
        self.email = ""
        self.shipping_address = ""
        self.phone = ""

    def record_dict(self) -> dict:
        if self.sc_type == SCType.SUPPLIER:
            sc_type_str = "Supplier"
        elif self.sc_type == SCType.CLIENT:
            sc_type_str = "Client"
        else:
            sc_type_str = "Supplier and Client"

        return {"SupplierClientType": sc_type_str,
                "SupplierClientName": self.name,
                "SupplierClientEmail": self.email,
                "SupplierClientShippingAddress1": self.shipping_address,
                "SupplierClientPhone1": self.phone}


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


def api_key_verify(key: str) -> int:
    data = {"APIKEY": api_key}

    response = requests.post(f"{base_url}/APIkey/APIkeyGet",
                             headers=headers, json=data)

    return int(response.json()["ResponseStatus"]["ErrorCode"])


def insert_product(product: Product, ext_app: str) -> int:
    data = {"APIKEY": api_key,
            "mvProduct": product.record_dict(),
            "mvRecordAction": "Insert"}

    if ext_app != "":
        # The ProductUpdate was triggered by an external application.
        data["mvInsertUpdateDeleteSourceApplication"] = ext_app

    response = requests.post(f"{base_url}/Product/ProductUpdate",
                             headers=headers, json=data)

    # Store the ProductID that was assigned.
    product.record_id = response.json()["mvProduct"]["ProductID"]

    # Return the error code of the response message.
    return int(response.json()["ResponseStatus"]["ErrorCode"])


def insert_supplier_client(sc: SupplierClient, ext_app: str) -> int:
    data = {"APIKEY": api_key,
            "mvSupplierClient": sc.record_dict(),
            "mvRecordAction": "Insert"}

    if ext_app != "":
        # The SupplierClientUpdate was triggered by an external application.
        data["mvInsertUpdateDeleteSourceApplication"] = ext_app

    response = requests.post(f"{base_url}/SupplierClient/SupplierClientUpdate",
                             headers=headers, json=data)

    # Store the SupplierClientID that was assigned.
    sc.record_id = response.json()["mvSupplierClient"]["SupplierClientID"]

    # Return the error code of the response message.
    return int(response.json()["ResponseStatus"]["ErrorCode"])


if __name__ == '__main__':
    supplier = SupplierClient("George_0", SCType.SUPPLIER)
    supplier.email = "george@mail.com"
    supplier.shipping_address = "Here 56, Athens"
    supplier.phone = "6923452345"

    print(supplier.record_id)
    print("Error code: ", insert_supplier_client(supplier, ""))
    print(supplier.record_id)


