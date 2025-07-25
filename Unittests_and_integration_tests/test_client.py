#!/usr/bin/env python3
"""
Tests unitaires pour le module client
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Classe de test pour GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test que GithubOrgClient.org retourne la valeur correcte"""
        test_payload = {"login": org_name, "id": 12345}
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org_name)

        result = client.org

        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)

        self.assertEqual(result, test_payload)

    def test_public_repos_url(self):
        """Test que _public_repos_url retourne la valeur attendue"""
        test_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos"
            }

        with patch.object(
            GithubOrgClient,
            'org', new_callable=lambda: property(lambda self: test_payload)
        ):
            client = GithubOrgClient("google")

            result = client._public_repos_url

            self.assertEqual(result, test_payload["repos_url"])


if __name__ == '__main__':
    unittest.main()
