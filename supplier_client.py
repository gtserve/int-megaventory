# supplier_client.py
# -------------------------------------------------------------------------------------------------
# Megaventory Internship Project
# name: George Tservenis
# email: george.tservenis@gmail.com
# date: 04-03-2022
# -------------------------------------------------------------------------------------------------

from enum import Enum


class SCType(Enum):
    SUPPLIER = "Supplier"
    CLIENT = "Client"
    SnC = "Supplier and Client"


class SupplierClient:

    def __init__(self, name: str, sc_type: SCType) -> None:
        self.SupplierClientID = -1
        self.SupplierClientType = sc_type
        self.SupplierClientName = name
        self.SupplierClientEmail = ""
        self.SupplierClientShippingAddress1 = ""
        self.SupplierClientPhone1 = ""

    def get_name(self) -> str:
        return self.SupplierClientName

    def set_id(self, record_id) -> None:
        self.SupplierClientID = record_id
