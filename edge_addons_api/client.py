from dataclasses import dataclass
from os import path

import requests


@dataclass
class Options:
    product_id: str
    client_id: str
    client_secret: str
    access_token_url: str


class Client:

    BASE_URL = "https://api.addons.microsoftedge.microsoft.com"

    def __init__(self, options: Options):
        self.options = options

    def submit(self, file_path: str, notes: str):
        if not path.exists(file_path):
            raise FileNotFoundError(f"Unable to locate file at {file_path}")

        access_token = self._get_access_token()
        self._upload(file_path, access_token)
        self._publish(notes, access_token)

    def _publish(self, notes: str, access_token: str):
        response = requests.post(
            self._publish_endpoint(),
            data={"notes": notes},
            headers={
                "Authorization": f"Bearer {access_token}",
            },
        )

        response.raise_for_status()

    def _upload(self, file_path: str, access_token: str):

        files = {"file": open(file_path, "rb")}

        response = requests.post(
            self._upload_endpoint(),
            files=files,
            headers={
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/zip",
            },
        )

        response.raise_for_status()

    def _get_access_token(self) -> str:
        response = requests.post(
            self.options.access_token_url,
            data={
                "client_id": self.options.client_id,
                "scope": f"{self.BASE_URL}/.default",
                "client_secret": self.options.client_secret,
                "grant_type": "client_credentials",
            },
        )

        response.raise_for_status()

        json = response.json()

        return json["access_token"]

    def _product_endpoint(self) -> str:
        return f"{self.BASE_URL}/v1/products/{self.options.product_id}"

    def _publish_endpoint(self) -> str:
        return f"{self._product_endpoint()}/submissions"

    def _upload_endpoint(self) -> str:
        return f"{self._publish_endpoint()}/draft/package"
