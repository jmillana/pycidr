from dataclasses import dataclass

from .ipv4 import IPv4
from .ipv4_mask import IPv4Mask


@dataclass
class IPNetwork:
    ip: IPv4
    mask: IPv4Mask

    @classmethod
    def from_cidr(cls, ip: str) -> "IPNetwork":
        if "/" in ip:
            ip, mask = ip.split("/")
            mask = int(mask)
        else:
            mask = 32
        return IPNetwork(IPv4(ip), IPv4Mask(mask))

    @property
    def network_id(self) -> IPv4:
        network_id = ".".join(
            str(ip_octet & mask_octet)
            for ip_octet, mask_octet in zip(self.ip.octets, self.mask.octets)
        )
        return IPv4(network_id)

    @property
    def cidr(self) -> str:
        return f"{self.ip}/{self.mask.value}"

    @property
    def broadcast_ip(self) -> IPv4:
        mask_octets = self.mask.octets
        network_octets = self.network_id.octets
        bcast_address = []
        for network_octet, mask_octet in zip(network_octets, mask_octets):
            bcast_address.append(str(network_octet + (255 ^ mask_octet)))
        return IPv4(".".join(bcast_address))

    @property
    def cidr_class(self) -> str:
        first_octet = self.ip.octets[0]
        if first_octet <= 127:
            return "A"
        elif first_octet <= 191:
            return "B"
        elif first_octet <= 223:
            return "C"
        elif first_octet <= 239:
            return "D"
        else:
            return "E"

    @property
    def total_addresses(self) -> int:
        return 2 ** (32 - self.mask.value)

    @property
    def usable_hosts(self) -> int:
        return max(self.total_addresses - 2, 0)
