# discount.py
# -------------------------------------------------------------------------------------------------
# Megaventory Internship Project
# name: George Tservenis
# email: george.tservenis@gmail.com
# date: 04-03-2022
# -------------------------------------------------------------------------------------------------


class Discount:

    def __init__(self, name: str, percent: float) -> None:
        self.DiscountID = -1
        self.DiscountName = name
        self.DiscountDescription = ""
        self.DiscountValue = percent

    def get_name(self) -> str:
        return self.DiscountName

    def set_id(self, record_id) -> None:
        self.DiscountID = record_id
