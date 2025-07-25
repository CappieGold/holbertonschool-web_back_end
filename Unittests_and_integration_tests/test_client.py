#!/usr/bin/env python3
"""
Tests unitaires pour le module client
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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
        ):
            client = GithubOrgClient("google")

            result = client.public_repos()

            expected_repos = [
                "Google-Search",
                "cpp-netlib",
                "dagger",
                "ios-webkit-debug-proxy"
            ]
            self.assertEqual(result, expected_repos)

            mock_get_json.assert_called_once_with(test_repos_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test que has_license retourne la valeur attendue"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3]
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Classe de test d'intégration pour GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Configure les mocks pour toute la classe de test"""
        def side_effect(url):
            """Fonction side_effect pour mocker requests.get"""
            mock_response = unittest.mock.Mock()

            if url == "https://api.github.com/orgs/google":
                mock_response.json.return_value = cls.org_payload
            elif url == "https://api.github.com/orgs/google/repos":
                mock_response.json.return_value = cls.repos_payload
            else:
                mock_response.json.return_value = None

            return mock_response

        cls.get_patcher = patch('requests.get', side_effect=side_effect)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Arrête le patcher après tous les tests"""
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
