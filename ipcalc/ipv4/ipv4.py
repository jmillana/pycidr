import re
from dataclasses import dataclass
from typing import Tuple

_regex = r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$"


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
        return ".".join(format(octet, "02x") for octet in self.octets).upper()

    def __str__(self) -> str:
        return self.address

    def __post_init__(self) -> None:
        if not re.match(_regex, self.address):
            raise ValueError(f"Invalid IPv4 address: {self.address}")
