from dataclasses import dataclass
from typing import Tuple


@dataclass
class IpAddress:
    ip: str
    mask: int

    @classmethod
    def from_cidr(cls, ip: str) -> "IpAddress":
        if "/" in ip:
            ip, mask = ip.split("/")
            mask = int(mask)
        else:
            mask = 32
        return IpAddress(ip, mask)

    @property
    def dotted_binary(self) -> str:
        return ip_to_dotted_binary(self.ip)

    @property
    def mask_dotted_binary(self) -> str:
        mask_octets = get_mask_octets(self.mask)
        mask_ip = octets_to_dot_notation(mask_octets)
        return ip_to_dotted_binary(mask_ip)

    @property
    def cidr(self) -> str:
        return f"{self.ip}/{self.mask}"

    @property
    def network_id(self) -> str:
        mask_octets = get_mask_octets(self.mask)
        network_id = ".".join(
            str(octet & mask) for octet, mask in zip(get_octets(self.ip), mask_octets)
        )
        return network_id

    @property
    def broadcast_address(self) -> str:
        mask_octets = get_mask_octets(self.mask)
        network_octets = get_octets(self.network_id)
        bcast_address = []
        for network_octet, mask_octet in zip(network_octets, mask_octets):
            bcast_address.append(str(network_octet + (255 ^ mask_octet)))
        return ".".join(bcast_address)

    @property
    def cidr_class(self) -> str:
        if self.mask >= 24:
            return "C"
        elif self.mask >= 16:
            return "B"
        else:
            return "A"

    @property
    def total_addresses(self) -> int:
        return 2 ** (32 - self.mask)

    @property
    def usable_hosts(self) -> int:
        return max(self.total_addresses - 2, 0)


def get_octets(ip: str) -> Tuple[int, int, int, int]:
    return tuple(int(octet) for octet in ip.split("."))


def octets_to_dot_notation(octets: Tuple[int, int, int, int]) -> str:
    return ".".join(str(octet) for octet in octets)


def ip_to_dotted_binary(ip: str) -> str:
    return ".".join(format(int(octet), "08b") for octet in ip.split("."))


def get_mask_octets(mask: int) -> Tuple[int, int, int, int]:
    mask_octets: list[int] = []
    octet = 0
    for bit in range(0, mask):
        if bit % 8 == 0 and bit != 0:
            mask_octets.append(octet)
            octet = 0
        octet += 2 ** (7 - bit % 8)

    while len(mask_octets) < 4:
        mask_octets.append(octet)
        octet = 0
    return tuple(mask_octets)
