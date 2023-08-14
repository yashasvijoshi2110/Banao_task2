import unittest
import requests

class TestATGWorldWebsite(unittest.TestCase):
    def test_website_loading(self):
        url = "https://atg.world"
        response = requests.get(url)

        print(f"Connecting to {url}")
        
        self.assertEqual(response.status_code, 200, f"Failed to load {url}. Status code: {response.status_code}")
        
        print(f"Successfully loaded {url}")

if __name__ == '__main__':
    unittest.main()
