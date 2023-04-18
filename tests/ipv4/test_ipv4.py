import unittest

from pycidr.ipv4 import IPv4


class IPv4Test(unittest.TestCase):
    def test_ipv4_constructor_ok(self):
        ip = IPv4("142.135.1.0")
        self.assertEqual(ip.address, "142.135.1.0")

        ip = IPv4("255.255.255.255")
        self.assertEqual(ip.address, "255.255.255.255")

        ip = IPv4("0.0.0.0")
        self.assertEqual(ip.address, "0.0.0.0")

    def test_ipv4_constructor_fails(self):
        self.assertRaises(ValueError, IPv4, "256.255.255.255")
        self.assertRaises(ValueError, IPv4, "123.01.213.04")
        self.assertRaises(ValueError, IPv4, "-122.1.2.3")

    def test_ipv4_to_binary(self):
        ip = IPv4("255.132.0.14")
        self.assertEqual(ip.binary, "11111111.10000100.00000000.00001110")

    def test_ipv4_to_hex(self):
        ip = IPv4("255.132.0.14")
        self.assertEqual(ip.hex, "FF.84.00.0E")

    def test_str_representation(self):
        ip = IPv4("255.132.0.14")
        self.assertEqual(str(ip), "255.132.0.14")
