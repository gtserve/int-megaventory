# api.py
# -------------------------------------------------------------------------------------------------
# Megaventory Internship Project
# name: George Tservenis
# email: george.tservenis@gmail.com
# date: 04-03-2022
# -------------------------------------------------------------------------------------------------

from requests import post as post_request
from json import dumps as json_encoder
from product import Product


class API:

    def __init__(self, key, base_url):
        self.key = key
        self.base_url = base_url
        self.headers = {"Content-Type": "application/json"}

    def key_verify(self) -> int:
        data = {"APIKEY": self.key}
        response = post_request(f"{self.base_url}/APIkey/APIkeyGet",
                                headers=self.headers, json=data)
        return int(response.json()["ResponseStatus"]["ErrorCode"])

    def perform_action(self, mv_action: str, entity, ext_app: str) -> int:

        # Currently only the Insert action is supported.
        if mv_action != "Insert":
            return -1

        # Find out what kind of entity is the action to be performed with.
        # If the entity is not supported return an error code.
        if isinstance(entity, Product):
            ent_type = "Product"
        else:
            return -1

        mv_str = f"mv{ent_type}"
        url_ext = f"/{ent_type}/{ent_type}Update"
        ent_id_attr = f"{ent_type}ID"

        ent_attr = {}
        if mv_action == "Insert":
            ent_attr = {a: entity.__dict__[a] for a in entity.__dict__ if a != ent_id_attr}

        data = {"APIKEY": self.key,
                mv_str: ent_attr,
                "mvRecordAction": mv_action}

        if ext_app != "":
            # The action was triggered by an external application.
            data["mvInsertUpdateDeleteSourceApplication"] = ext_app

        # Print useful request info for debugging.
        print("Request:")
        print(f"  - action:      {mv_action}")
        print(f"  - entity type: {ent_type}")
        print(f"  - entity name: \"{entity.get_name()}\"")
        print(f"  - request url: \"{self.base_url}{url_ext}\"")

        response = post_request(f"{self.base_url}{url_ext}", headers=self.headers, json=data)
        entity_id = int(response.json()["entityID"])
        error_code = int(response.json()["ResponseStatus"]["ErrorCode"])

        # Print useful response info for debugging.
        print("\nResponse:")
        print(f"  - status code: {response.status_code}")
        print(f"  - error code:  {error_code}")
        print(f"  - entityID:    {entity_id}")

        # Store the record id that was assigned.
        entity.set_id(entity_id)

        # Return the error code of the response message.
        return error_code
