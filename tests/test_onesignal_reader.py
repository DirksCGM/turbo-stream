"""
Test turbo_stream.onesignal.reader
"""
import unittest

import OpenSSL
import pytest
from googleapiclient.discovery import build

from turbo_stream.onesignal.reader import OnesignalReader


class TestOnesignalReader(unittest.TestCase):
    def test_generate_url_csv_export(self):
        """Test endpoint creation of csv_export."""
        reader = OnesignalReader(
            configuration={"endpoint": "csv_export"},
            credentials="tests/assets/mock_onesignal_creds.yml",
            credential_file_fmt="yml",
        )

        self.assertEqual(
            reader._generate_url(endpoint="csv_export"),
            "https://onesignal.com/api/v1/players/csv_export?app_id=x000x00x-xx00-0x00-x000-x000x00xxx0",
        )

    def test_generate_url_view_notification(self):
        """Test endpoint creation of view_notification."""
        reader = OnesignalReader(
            configuration={"endpoint": "view_notification"},
            credentials="tests/assets/mock_onesignal_creds.yml",
            credential_file_fmt="yml",
        )

        self.assertEqual(
            reader._generate_url(endpoint="view_notification"),
            "https://onesignal.com/api/v1/notifications?app_id=x000x00x-xx00-0x00-x000-x000x00xxx0",
        )

    def test_view_notification_query_handler(self):
        """Test the view_notification_query_handler method."""
        reader = OnesignalReader(
            configuration={"endpoint": "view_notification"},
            credentials="tests/assets/mock_onesignal_creds.yml",
            credential_file_fmt="yml",
        )

        self.assertEqual(
            reader._view_notification_query_handler(limit=50, offset=0).json(),
            {"errors": ["Invalid app_id format"]},
        )

    def test_csv_export_query_handler(self):
        """Test the csv_export_query_handler method."""
        reader = OnesignalReader(
            configuration={"endpoint": "csv_export"},
            credentials="tests/assets/mock_onesignal_creds.yml",
            credential_file_fmt="yml",
        )

        self.assertEqual(
            reader._csv_export_query_handler().json(),
            {
                "errors": [
                    "app_id not found. You may be missing a Content-Type: application/json header."
                ]
            },
        )

    def test_run_query_csv_export(self):
        """Attempt to run query for csv export."""
        reader = OnesignalReader(
            configuration={"endpoint": "csv_export"},
            credentials="tests/assets/mock_onesignal_creds.yml",
            credential_file_fmt="yml",
        )

        with pytest.raises(ConnectionError):
            reader.run_query()

    def test_run_query_view_notification(self):
        """Attempt to run query for view notification."""
        reader = OnesignalReader(
            configuration={"endpoint": "view_notification"},
            credentials="tests/assets/mock_onesignal_creds.yml",
            credential_file_fmt="yml",
        )

        with pytest.raises(TypeError):
            reader.run_query()
