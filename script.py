from edge_addons_api.client import Options, Client

import os

options = Options(
    product_id=os.environ["EDGE_PRODUCT_ID"],
    client_id=os.environ["EDGE_CLIENT_ID"],
    client_secret=os.environ["EDGE_CLIENT_SECRET"],
    access_token_url=os.environ["EDGE_ACCES_TOKEN_URL"]
)

client = Client(options)

client.submit(
    file_path="/path/to/extension.zip",
    notes="Your upload notes"
)
