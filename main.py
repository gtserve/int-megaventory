# main.py
# -------------------------------------------------------------------------------------------------
# Megaventory Internship Project
# name: George Tservenis
# email: george.tservenis@gmail.com
# date: 04-03-2022
# -------------------------------------------------------------------------------------------------

from api import API
from product import Product
import supplier_client as sc
from inventory_location import InventoryLocation
from tax import Tax
from discount import Discount
import sales_order as so

api_key = "3974d8451ecede7d@m128220"

# Global info for requests
base_url = "https://api.megaventory.com/v2017a"
headers = {"Content-Type": "application/json"}


if __name__ == '__main__':

    # Create an API object.
    api = API(api_key, base_url)

    print("\nPRODUCT:")
    # Create a dummy Product.
    p = Product("Product_136", "product description")
    p.ProductSellingPrice = 76.99
    p.ProductPurchasePrice = 32.98

    # Insert Product and print its attributes.
    api.perform_action("Insert", p, "")
    print(p.__dict__)

    print("\nCLIENT:")
    # Create a dummy Client.
    c = sc.SupplierClient("Client_19", sc.CLIENT)
    c.SupplierClientEmail = "nikos@mail.com"
    c.SupplierClientShippingAddress1 = "Edw 21, Athens"
    c.SupplierClientPhone1 = "2106781906"

    # Insert Client and print its attributes.
    api.perform_action("Insert", c, "")
    print(c.__dict__)

    print("\nINVENTORY_LOCATION:")
    # Create a dummy Inventory Location.
    il = InventoryLocation("LOC3", "Location_3")
    il.InventoryLocationAddress = "Ekei 31, Athens"

    # Insert Inventory Location and print its attributes.
    api.perform_action("Insert", il, "")
    print(il.__dict__)

    # print("\nTAX:")
    # # Create a dummy Tax
    # t = Tax("Random_tax", 12.5)
    # t.TaxDescription = "A tax description"
    #
    # # Insert Tax and print its attributes.
    # api.perform_action("Insert", t, "")
    # print(t.__dict__)
    #
    # print("\nDISCOUNT:")
    # # Create a dummy Discount
    # d = Discount("Random_discount", 12.5)
    # d.TaxDescription = "A discount description"
    #
    # # Insert Tax and print its attributes.
    # api.perform_action("Insert", d, "")
    # print(d.__dict__)

    print("\nSALES_ORDER:")
    # Create a dummy SalesOrder
    products = [(p, 12)]
    so = so.SalesOrder("Verified", c, products)
    so.set_location(il)

    # Insert SalesOrder and print its attributes.
    api.perform_action("Insert", so, "")
    print(so.__dict__)
