# sales.order.py
# -------------------------------------------------------------------------------------------------
# Megaventory Internship Project
# name: George Tservenis
# email: george.tservenis@gmail.com
# date: 04-03-2022
# -------------------------------------------------------------------------------------------------
from discount import Discount
from supplier_client import SupplierClient
from inventory_location import InventoryLocation
from tax import Tax


# Type aliases for SalesOrder
PENDING = "Pending"
APPROVED = "Approved"
SHIPPED = "Shipped"
INVOICED = "Invoiced"
CLOSED = "Closed"


class SalesOrder:

    def __init__(self, status: str, client: SupplierClient, order_list: list) -> None:
        self.SalesOrderId = -1
        self.SalesOrderNo = -1
        self.SalesOrderStatus = status
        self.client = client
        self.order_list = order_list
        self.location = None

    def get_name(self) -> str:
        return f"SalesOrder {self.SalesOrderId} no{self.SalesOrderNo}"

    def set_id(self, record_id) -> None:
        self.SalesOrderId = record_id

    def set_location(self, location: InventoryLocation) -> None:
        self.location = location

    def get_total_value(self, tax: Tax, discount: Discount) -> float:
        """ Calculate the total selling value of a SalesOrder. """

        value = 0.00
        for p, q in self.order_list:
            value += p.ProductSellingPrice * q

        if tax is not None:
            # If a Tax is given, apply it on total value.
            value += (tax.TaxValue * 0.01) * value

        if discount is not None:
            # If a Discount is given, apply it on total value. (After tax, if any).
            value -= (discount.DiscountValue * 0.01) * value

        return value
