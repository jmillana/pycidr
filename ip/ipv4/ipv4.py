from dataclasses import dataclass
from typing import Tuple


def _to_dotted_binary(ip: str) -> str:
    return ".".join(format(int(octet), "08b") for octet in ip.split("."))


@dataclass
class IPv4:
    address: str

    @property
    def octets(self) -> Tuple[int, int, int, int]:
        return tuple(int(octet) for octet in self.address.split("."))

    @property
    def binary(self) -> str:
        return _to_dotted_binary(self.address)

    @property
    def hex(self) -> str:
        return ".".join(format(octet, "02x") for octet in self.octets)

    def __str__(self) -> str:
        return self.address
