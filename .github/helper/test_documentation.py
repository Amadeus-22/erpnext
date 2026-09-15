import os
import unittest
from unittest.mock import Mock, patch

import documentation


class DocumentationTestCase(unittest.TestCase):
	@patch.dict(
		os.environ,
		{"GITHUB_API_URL": "https://api.github.com", "GITHUB_REPOSITORY": "Amadeus-22/erpnext"},
		clear=False,
	)
	@patch("documentation.requests.get")
	def test_check_pull_request_uses_current_repository(self, mock_get):
		mock_get.return_value = Mock(
			ok=True,
			json=Mock(return_value={"title": "feat: add thing", "head": {"sha": "abc123"}, "body": "no-docs"}),
		)

		exit_code, message = documentation.check_pull_request("9")

		self.assertEqual((exit_code, message), (0, "Skipping documentation checks... 🏃"))
		mock_get.assert_called_once_with("https://api.github.com/repos/Amadeus-22/erpnext/pulls/9")


if __name__ == "__main__":
	unittest.main()
