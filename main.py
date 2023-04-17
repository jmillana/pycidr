import typer

from ip.ipv4 import IPNetwork
from ip import display


def main(ip: str):
    ip_network = IPNetwork.from_cidr(ip)
    display.show_2column_table(ip_network)


if __name__ == "__main__":
    typer.run(main)
