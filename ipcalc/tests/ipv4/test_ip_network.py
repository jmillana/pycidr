import unittest
from ipcalc.ipv4 import IPNetwork


class IPNetworkTest(unittest.TestCase):
    def setUp(self):
        self.network = IPNetwork.from_cidr("10.10.10.10/22")

    def test_constructor_ok(self):
        network = IPNetwork.from_cidr("10.10.10.10/16")
        self.assertEqual(network.ip.address, "10.10.10.10")
        self.assertEqual(network.mask.value, 16)

        network = IPNetwork.from_cidr("10.10.10.10")
        self.assertEqual(network.ip.address, "10.10.10.10")
        self.assertEqual(network.mask.value, 32)

    def test_constructor_fails(self):
        self.assertRaises(ValueError, IPNetwork.from_cidr, "300.0.0.0/32")
        self.assertRaises(ValueError, IPNetwork.from_cidr, "150.0.132.1/33")

    def test_get_network_id(self):
        self.assertEqual(self.network.network_id.address, "10.10.8.0")

    def test_get_cidr_representation(self):
        self.assertEqual(self.network.cidr, "10.10.10.10/22")

    def test_get_bradcast_ip(self):
        bcast = self.network.broadcast_ip
        self.assertEqual(bcast.address, "10.10.11.255")

    def test_get_cidr_class(self):
        first_c_network = IPNetwork.from_cidr("10.10.10.10/32")
        self.assertEqual(first_c_network.cidr_class, "C")
        last_c_network = IPNetwork.from_cidr("10.10.10.10/24")
        self.assertEqual(last_c_network.cidr_class, "C")

        first_b_network = IPNetwork.from_cidr("10.10.10.10/23")
        self.assertEqual(first_b_network.cidr_class, "B")
        last_b_network = IPNetwork.from_cidr("10.10.10.10/16")
        self.assertEqual(last_b_network.cidr_class, "B")

        first_a_network = IPNetwork.from_cidr("10.10.10.10/15")
        self.assertEqual(first_a_network.cidr_class, "A")
        last_a_network = IPNetwork.from_cidr("10.10.10.10/0")
        self.assertEqual(last_a_network.cidr_class, "A")

    def test_total_addresses(self):
        first_c_network = IPNetwork.from_cidr("10.10.10.10/32")
        self.assertEqual(first_c_network.total_addresses, 1)
        last_c_network = IPNetwork.from_cidr("10.10.10.10/24")
        self.assertEqual(last_c_network.total_addresses, 256)

        first_b_network = IPNetwork.from_cidr("10.10.10.10/23")
        self.assertEqual(first_b_network.total_addresses, 512)
        last_b_network = IPNetwork.from_cidr("10.10.10.10/16")
        self.assertEqual(last_b_network.total_addresses, 65536)

        first_a_network = IPNetwork.from_cidr("10.10.10.10/15")
        self.assertEqual(first_a_network.total_addresses, 131072)
        last_a_network = IPNetwork.from_cidr("10.10.10.10/0")
        self.assertEqual(last_a_network.total_addresses, 4294967296)

    def test_usable_hosts(self):
        first_c_network = IPNetwork.from_cidr("10.10.10.10/32")
        self.assertEqual(first_c_network.usable_hosts, 0)
        last_c_network = IPNetwork.from_cidr("10.10.10.10/24")
        self.assertEqual(last_c_network.usable_hosts, 254)

        first_b_network = IPNetwork.from_cidr("10.10.10.10/23")
        self.assertEqual(first_b_network.usable_hosts, 510)
        last_b_network = IPNetwork.from_cidr("10.10.10.10/16")
        self.assertEqual(last_b_network.usable_hosts, 65534)

        first_a_network = IPNetwork.from_cidr("10.10.10.10/15")
        self.assertEqual(first_a_network.usable_hosts, 131070)
        last_a_network = IPNetwork.from_cidr("10.10.10.10/0")
        self.assertEqual(last_a_network.usable_hosts, 4294967294)
