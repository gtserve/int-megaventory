# tax.py
# -------------------------------------------------------------------------------------------------
# Megaventory Internship Project
# name: George Tservenis
# email: george.tservenis@gmail.com
# date: 04-03-2022
# -------------------------------------------------------------------------------------------------


class Tax:

    def __init__(self, name: str, percent: float) -> None:
        self.TaxID = -1
        self.TaxName = name
        self.TaxDescription = ""
        self.TaxValue = percent

    def get_name(self) -> str:
        return self.TaxName

    def set_id(self, record_id) -> None:
        self.TaxID = record_id
