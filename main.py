# main.py
# -------------------------------------------------------------------------------------------------
# Megaventory Internship Project
# name: George Tservenis
# email: george.tservenis@gmail.com
# date: 04-03-2022
# -------------------------------------------------------------------------------------------------

from api import API
from product import Product
from inventory_location import InventoryLocation
from tax import Tax
from discount import Discount

import supplier_client as sc
import sales_order as so

# Global info for requests
api_key = "3974d8451ecede7d@m128220"
base_url = "https://api.megaventory.com/v2017a"


if __name__ == '__main__':

    # Create an API object.
    api = API(api_key, base_url)

    # Create a dummy Product.
    product = Product("1112256", "Nike shoes")
    product.ProductSellingPrice = 99.99
    product.ProductPurchasePrice = 44.99

    # Insert Product and print its attributes.
    api.perform_action("Insert", product, "")
    # print(product.__dict__)

    # Create a dummy Client.
    c = sc.SupplierClient("babis", sc.CLIENT)
    c.SupplierClientEmail = "babis@exampletest.com"
    c.SupplierClientShippingAddress1 = "Example 8, Athens"
    c.SupplierClientPhone1 = "1235698967"

    # Insert Client and print its attributes.
    api.perform_action("Insert", c, "")
    # print(c.__dict__)

    print("\nINVENTORY_LOCATION:")
    # Create a dummy Inventory Location.
    il = InventoryLocation("LOC5", "Location_5")
    il.InventoryLocationAddress = "Ekei 31, Athens"

    # Insert Inventory Location and print its attributes.
    # api.perform_action("Insert", il, "")
    # print(il.__dict__)

    print("\nTAX:")
    # Create a dummy Tax
    t = Tax("Random_tax1", 24)
    t.TaxDescription = "A tax description"

    # Insert Tax and print its attributes.
    # api.perform_action("Insert", t, "")
    # print(t.__dict__)

    print("\nDISCOUNT:")
    # Create a dummy Discount
    d = Discount("Random_discount1", 50)
    d.TaxDescription = "A discount description"

    # Insert Tax and print its attributes.
    # api.perform_action("Insert", d, "")
    # print(d.__dict__)

    print("\nSALES_ORDER:")
    # Create a dummy SalesOrder
    products = [(product, 12)]
    so = so.SalesOrder("Verified", c, products)
    so.set_location(il)

    # Insert SalesOrder and print its attributes.
    # api.perform_action("Insert", so, "")
    # print(so.__dict__)

    print("Total Value: ", so.get_total_value(t, d))
