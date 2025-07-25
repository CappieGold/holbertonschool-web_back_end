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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test que public_repos retourne la liste attendue de repos"""
        test_payload = [
            {"name": "Google-Search"},
            {"name": "cpp-netlib"},
            {"name": "dagger"},
            {"name": "ios-webkit-debug-proxy"},
        ]

        mock_get_json.return_value = test_payload

        test_repos_url = "https://api.github.com/orgs/google/repos"

        with patch.object(
            GithubOrgClient,
            '_public_repos_url',
            new_callable=lambda: property(lambda self: test_repos_url)
        ) as mock_public_repos_url:
            client = GithubOrgClient("google")

            result = client.public_repos()

            expected_repos = [
                "Google-Search",
                "cpp-netlib",
                "dagger",
                "ios-webkit-debug-proxy"
            ]
            self.assertEqual(result, expected_repos)

            mock_public_repos_url.assert_called_once()

            mock_get_json.assert_called_once_with(test_repos_url)


if __name__ == '__main__':
    unittest.main()
