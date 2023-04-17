from dataclasses import dataclass
from typing import Tuple

from .ipv4 import IPv4


@dataclass
class IPv4Mask:
    value: int

    @property
    def ip(self) -> IPv4:
        return IPv4(".".join(str(octet) for octet in self.octets))

    @property
    def octets(self) -> Tuple[int, int, int, int]:
        mask_octets: list[int] = []
        octet = 0
        for bit in range(0, self.value):
            if bit % 8 == 0 and bit != 0:
                mask_octets.append(octet)
                octet = 0
            octet += 2 ** (7 - bit % 8)

        while len(mask_octets) < 4:
            mask_octets.append(octet)
            octet = 0
        return tuple(mask_octets)

    @property
    def binary(self) -> str:
        return self.ip.binary

    @property
    def hex(self) -> str:
        return self.ip.hex

    def __str__(self) -> str:
        return f"/{self.value}"

    def __post_init__(self) -> None:
        if not 0 <= self.value <= 32:
            raise ValueError("Mask value must be between 0 and 32")
