import typer
from dataclasses import dataclass
from typing import Tuple
from ip.ip import IpAddress
from ip import display


def main(ip: str):
    ip_address = IpAddress.from_cidr(ip)
    display.show_2column_table(ip_address)


if __name__ == "__main__":
    typer.run(main)
