# main.py
# -------------------------------------------------------------------------------------------------
# Megaventory Internship Project
# name: George Tservenis
# email: george.tservenis@gmail.com
# date: 04-03-2022
# -------------------------------------------------------------------------------------------------

from api import API
from product import Product

api_key = "3974d8451ecede7d@m128220"

# Global info for requests
base_url = "https://api.megaventory.com/v2017a"
headers = {"Content-Type": "application/json"}


if __name__ == '__main__':

    api = API(api_key, base_url)

    p = Product("Product_114", "description")
    print(p.__dict__)
    print("Error code: ", api.perform_action("Insert", p, ""))
    print(p.__dict__)
