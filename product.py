# product.py
# -------------------------------------------------------------------------------------------------
# Megaventory Internship Project
# name: George Tservenis
# email: george.tservenis@gmail.com
# date: 04-03-2022
# -------------------------------------------------------------------------------------------------


class Product:
    """ A class that represents an mvProduct object. """

    def __init__(self, sku: str, description: str) -> None:
        self.ProductID = -1
        self.ProductSKU = sku
        self.ProductDescription = description
        self.ProductSellingPrice = 0.00
        self.ProductPurchasePrice = 0.00

    def get_name(self) -> str:
        return self.ProductSKU

    def get_id(self) -> int:
        return self.ProductID

    def set_id(self, record_id) -> None:
        self.ProductID = record_id
