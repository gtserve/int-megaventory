# sales.order.py
# -------------------------------------------------------------------------------------------------
# Megaventory Internship Project
# name: George Tservenis
# email: george.tservenis@gmail.com
# date: 04-03-2022
# -------------------------------------------------------------------------------------------------

from supplier_client import SupplierClient
from inventory_location import InventoryLocation

# Type aliases for SalesOrder
PENDING = "Pending"
APPROVED = "Approved"
SHIPPED = "Shipped"
INVOICED = "Invoiced"
CLOSED = "Closed"


class SalesOrder:

    def __init__(self, status: str, client: SupplierClient, products: list) -> None:
        self.SalesOrderId = -1
        self.SalesOrderNo = -1
        self.SalesOrderStatus = status
        self.client = client
        self.products = products
        self.location = None

    def get_name(self) -> str:
        return f"SalesOrder {self.SalesOrderId} no{self.SalesOrderNo}"

    def set_id(self, record_id) -> None:
        self.SalesOrderId = record_id

    def set_location(self, location: InventoryLocation) -> None:
        self.location = location
