# inventory_location.py
# -------------------------------------------------------------------------------------------------
# Megaventory Internship Project
# name: George Tservenis
# email: george.tservenis@gmail.com
# date: 04-03-2022
# -------------------------------------------------------------------------------------------------


class InventoryLocation:
    """ A class that represents an mvInventoryLocation object. """

    def __init__(self, abbreviation: str, full_name: str) -> None:
        self.InventoryLocationID = -1
        self.InventoryLocationAbbreviation = abbreviation
        self.InventoryLocationName = full_name
        self.InventoryLocationAddress = ""

    def get_name(self) -> str:
        return self.InventoryLocationName

    def get_id(self) -> int:
        return self.InventoryLocationID

    def set_id(self, record_id) -> None:
        self.InventoryLocationID = record_id
