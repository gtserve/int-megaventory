# supplier_client.py
# -------------------------------------------------------------------------------------------------
# Megaventory Internship Project
# name: George Tservenis
# email: george.tservenis@gmail.com
# date: 04-03-2022
# -------------------------------------------------------------------------------------------------


class SupplierClient:
    """ A class that represents an mvSupplierClient object. """

    def __init__(self, name: str, sc_type: str) -> None:
        self.SupplierClientID = -1
        self.SupplierClientType = sc_type
        self.SupplierClientName = name
        self.SupplierClientEmail = ""
        self.SupplierClientShippingAddress1 = ""
        self.SupplierClientPhone1 = ""

    def get_name(self) -> str:
        return self.SupplierClientName

    def get_id(self) -> int:
        return self.SupplierClientID

    def set_id(self, record_id) -> None:
        self.SupplierClientID = record_id
