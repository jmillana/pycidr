import unittest
from ipcalc.ipv4 import IPv4Mask


class IPv4MaskTest(unittest.TestCase):
    def test_constructor_ok(self):
        mask = IPv4Mask(32)
        self.assertEqual(mask.value, 32)

        mask = IPv4Mask(0)
        self.assertEqual(mask.value, 0)

    def test_constructor_fails(self):
        self.assertRaises(ValueError, IPv4Mask, 33)
        self.assertRaises(ValueError, IPv4Mask, -1)

    def test_get_mask_ip(self):
        mask = IPv4Mask(24)
        self.assertEqual(mask.ip.address, "255.255.255.0")

    def test_get_mask_octets(self):
        mask = IPv4Mask(20)
        self.assertEqual(mask.octets, (255, 255, 240, 0))

    def test_get_mask_binary(self):
        mask = IPv4Mask(20)
        self.assertEqual(mask.binary, "11111111.11111111.11110000.00000000")

    def test_get_mask_hex(self):
        mask = IPv4Mask(13)
        self.assertEqual(mask.hex, "FF.F8.00.00")

    def test_str_representation(self):
        mask = IPv4Mask(3)
        self.assertEqual(str(mask), "/3")
