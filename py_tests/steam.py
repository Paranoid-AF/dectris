import unittest
from py_modules.steam import search_app_list  

class TestSteamMethods(unittest.TestCase):
    def test_appid(self):
        res = search_app_list("Half-Life 2")
        self.assertEqual(res[0][0], 220)
        self.assertEqual(res[0][1], "Half-Life 2")

if __name__ == '__main__':
    unittest.main()
