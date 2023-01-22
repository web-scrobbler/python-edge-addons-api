import logging
import os
import sys

from edge_addons_api.client import Client, Options

if len(sys.argv) < 3:
    print("You must provide file_path and notes")
    sys.exit(1)

file_path = sys.argv[1]
notes = sys.argv[2]

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

options = Options(
    product_id=os.environ["EDGE_PRODUCT_ID"],
    client_id=os.environ["EDGE_CLIENT_ID"],
    client_secret=os.environ["EDGE_CLIENT_SECRET"],
    access_token_url=os.environ["EDGE_ACCESS_TOKEN_URL"],
)

client = Client(options)

client.submit(file_path=file_path, notes=notes)
