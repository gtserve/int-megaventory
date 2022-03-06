# main.py
# -------------------------------------------------------------------------------------------------
# Megaventory Internship Project
# name: George Tservenis
# email: george.tservenis@gmail.com
# date: 04-03-2022
# -------------------------------------------------------------------------------------------------
# Description:
#   A simple application that uses the API class and the other entities to send/insert some dummy
#   instances.
# -------------------------------------------------------------------------------------------------

from api import API
from product import Product
from supplier_client import SupplierClient
from inventory_location import InventoryLocation
from tax import Tax
from discount import Discount
from sales_order import SalesOrder


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

    # Send (Insert) Product and print its attributes.
    api.perform_action("Insert", product, "")
    # print(product.__dict__)

    # Create a dummy Client.
    client = SupplierClient("babis", "Client")
    client.SupplierClientEmail = "babis@exampletest.com"
    client.SupplierClientShippingAddress1 = "Example 8, Athens"
    client.SupplierClientPhone1 = "1235698967"

    # Send (Insert) Client and print its attributes.
    api.perform_action("Insert", client, "")
    # print(c.__dict__)

    # Create a dummy Inventory Location.
    inv_location = InventoryLocation("Test", "Test Project Location")
    inv_location.InventoryLocationAddress = "Example 20, Athens"

    # Send (Insert) Inventory Location and print its attributes.
    api.perform_action("Insert", inv_location, "")
    # print(il.__dict__)

    # Create a dummy Tax
    tax = Tax("VAT", 24)
    tax.TaxDescription = "VAT GR"

    # Send (Insert) Tax and print its attributes.
    api.perform_action("Insert", tax, "")
    # print(t.__dict__)

    # Create a dummy Discount
    discount = Discount("Loyalty", 50)
    discount.TaxDescription = "Loyalty Customer Discount"

    # Send (Insert) Tax and print its attributes.
    api.perform_action("Insert", discount, "")
    # print(d.__dict__)

    # Create a dummy SalesOrder
    order_list = [(product, 12)]
    sales_order = SalesOrder("Verified", client, order_list)
    sales_order.set_location(inv_location)

    # Send (Insert) SalesOrder and print its attributes.
    api.perform_action("Insert", sales_order, "")
    # print(so.__dict__)

    print("Total Value: ", sales_order.get_total_value(tax, discount))
