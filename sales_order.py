# sales.order.py
# -------------------------------------------------------------------------------------------------
# Megaventory Internship Project
# name: George Tservenis
# email: george.tservenis@gmail.com
# date: 04-03-2022
# -------------------------------------------------------------------------------------------------

from enum import Enum
from json import dumps as json_encoder


class OrderStatus(Enum):
    PENDING = 1
    APPROVED = 2
    SHIPPED = 3
    INVOICED = 4
    CLOSED = 5


class SalesOrder:

    def __init__(self, order_id: int, no: int, status: OrderStatus) -> None:
        self.order_id = order_id
        self.no = no
        self.status = status

    def to_json_str(self) -> str:
        return json_encoder(self, default=lambda o: o.__dict__)
