# api.py
# -------------------------------------------------------------------------------------------------
# Megaventory Internship Project
# name: George Tservenis
# email: george.tservenis@gmail.com
# date: 04-03-2022
# -------------------------------------------------------------------------------------------------

from requests import post as post_request
from product import Product
from supplier_client import SupplierClient
from inventory_location import InventoryLocation
from tax import Tax
from discount import Discount
from sales_order import SalesOrder


class API:
    """A class that acts as an interface and handles the API endpoints."""

    def __init__(self, key, base_url):
        self.key = key
        self.base_url = base_url
        self.headers = {"Content-Type": "application/json"}     # Always ask for json.

    def key_verify(self) -> int:
        data = {"APIKEY": self.key}
        response = post_request(f"{self.base_url}/APIkey/APIkeyGet",
                                headers=self.headers, json=data)
        return int(response.json()["ResponseStatus"]["ErrorCode"])

    def perform_action(self, mv_action: str, entity: object, ext_app: str) -> int:
        """ A general method for handling all mvRecordActions regardless of the entity type. """

        if (mv_action is None) or (entity is None):
            return -1

        # Currently only the Insert mvRecordAction is supported.
        if mv_action != "Insert":
            return -1

        # Find out what kind of entity is the action to be performed with.
        # If the entity type is not supported return with an error code.
        if isinstance(entity, Product):
            ent_type = "Product"
        elif isinstance(entity, SupplierClient):
            ent_type = "SupplierClient"
        elif isinstance(entity, InventoryLocation):
            ent_type = "InventoryLocation"
        elif isinstance(entity, Tax):
            ent_type = "Tax"
        elif isinstance(entity, Discount):
            ent_type = "Discount"
        elif isinstance(entity, SalesOrder):
            ent_type = "SalesOrder"
        else:
            return -1

        mv_str = f"mv{ent_type}"
        url_ext = f"/{ent_type}/{ent_type}Update"
        ent_id_attr = f"{ent_type}ID"

        # Depending on the action and the entity type, some attributes have to be ignored.
        ignore_attr = {}
        if mv_action == "Insert":
            if ent_type != "SalesOrder":
                ignore_attr = {ent_id_attr}
            else:
                ignore_attr = {"SalesOrderId", "SalesOrderΝο", "client", "order_list", "location"}

        ent_attr = {a: entity.__dict__[a] for a in entity.__dict__ if a not in ignore_attr}

        # If entity is a SalesOrder then some extra steps are required for ProductDetails.
        if ent_type == "SalesOrder":
            ent_attr["SalesOrderClientId"] = entity.client.get_id()
            so_details = {}
            for p, q in entity.order_list:
                so_details["SalesOrderRowProductSKU"] = p.get_name()
                so_details["SalesOrderRowQuantity"] = q
                so_details["SalesOrderRowShippedQuantity"] = 0
                so_details["SalesOrderRowUnitPriceWithoutTaxOrDiscount"] = p.ProductSellingPrice
            ent_attr["SalesOrderDetails"] = so_details
            if entity.location is not None:
                # Add location ID if SalesOrder has one.
                ent_attr["SalesOrderInventoryLocationID"] = entity.location.InventoryLocationID

        data = {"APIKEY": self.key,
                mv_str: ent_attr,
                "mvRecordAction": mv_action}

        if ext_app != "":
            # The action was triggered by an external application.
            data["mvInsertUpdateDeleteSourceApplication"] = ext_app

        # Print useful request info for debugging.
        # print("Request:")
        # print(f"  - action:      {mv_action}")
        # print(f"  - entity type: {ent_type}")
        # print(f"  - entity name: \"{entity.get_name()}\"")
        # print(f"  - request url: \"{self.base_url}{url_ext}\"")

        response = post_request(f"{self.base_url}{url_ext}", headers=self.headers, json=data)
        entity_id = int(response.json()["entityID"])
        error_code = int(response.json()["ResponseStatus"]["ErrorCode"])

        # Print useful response info for debugging.
        # print("\nResponse:")
        # print(f"  - status code: {response.status_code}")
        # print(f"  - error code:  {error_code}")
        # print(f"  - entityID:    {entity_id}")

        # print(response.json())

        if error_code != 0:
            print("[API]: Something went wrong with the request!")
            return -1

        # Store the record id that was assigned.
        entity.set_id(entity_id)

        if ent_type == "SalesOrder":
            entity.SalesOrderNo = int(response.json()[mv_str]["SalesOrderNo"])

        # Return the error code of the response message.
        return error_code
