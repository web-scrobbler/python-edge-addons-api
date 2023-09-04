import logging
import os
import sys

from edge_addons_api.client import Client, Options
from edge_addons_api.exceptions import UploadException

if len(sys.argv) < 3:
    print("You must provide file_path and notes")
    sys.exit(1)

file_path = sys.argv[1]
notes = sys.argv[2]

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
logging.getLogger("urllib3").setLevel(logging.WARNING)


options = Options(
    product_id=os.environ["EDGE_PRODUCT_ID"],
    client_id=os.environ["EDGE_CLIENT_ID"],
    client_secret=os.environ["EDGE_CLIENT_SECRET"],
    access_token_url=os.environ["EDGE_ACCESS_TOKEN_URL"],
)

client = Client(options)

print("Submitting addon")

try:
    resp = client.submit(file_path=file_path, notes=notes)
    client.fetch_publish_status(resp)

    print("Successfully uploaded addon")
except UploadException as e:
    print(f"Failed to upload: {e.status} - {e.error_code} - {e.message}")
    print("Errors:")
    for error in e.errors:
        print(f"- {error['message']}")

    sys.exit(1)
except BaseException as e:
    print(f"failed to upload: {e}")
    sys.exit(1)
