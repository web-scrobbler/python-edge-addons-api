from unittest import TestCase

from edge_addons_api.client import Client, Options


class ClientTest(TestCase):
    def test_submit_missing_file(self):
        client = Client(Options("", "", "", ""))

        with self.assertRaises(FileNotFoundError):
            client.submit("/non/existent/path", "new version upload")
