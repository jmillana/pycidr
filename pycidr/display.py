from rich import print
from rich.table import Table

from .ipv4 import IPNetwork


def show_all(network: IPNetwork) -> None:
    table = Table(show_header=True, header_style="bold magenta")
    table.title = "IP Address Information: [bold blue]{}[/bold blue]".format(
        network.cidr
    )
    table.add_column("CIDR block", justify="center", style="cyan", no_wrap=True)
    table.add_column("Network Mask", justify="center", style="cyan", no_wrap=True)
    table.add_column("IP Address", justify="center", style="cyan", no_wrap=True)
    table.add_column("Network ID", justify="center", style="magenta")
    table.add_column("Broadcast Address", justify="center", style="green")
    table.add_column("CIDR Class", justify="center", style="blue")
    table.add_column("Total Addresses", justify="center", style="blue")
    table.add_column("Usable hosts", justify="center", style="blue")
    table.add_row(
        str(network.mask),
        network.mask.ip.address,
        network.ip.address,
        network.network_id.address,
        network.broadcast_ip.address,
        network.cidr_class,
        str(network.total_addresses),
        str(network.usable_hosts),
    )
    print()
    print(table)


def show_2column_table(network: IPNetwork) -> None:
    table = Table(show_header=False, header_style="bold magenta")
    table.title = f"IP Address Information for: [bold blue]{network.cidr}[/bold blue]"

    table.add_row("Class", network.cidr_class, style="green")
    table.add_row("CIDR block", str(network.mask), style="sea_green3")
    table.add_row("IP Address", network.ip.address, style="blue")
    table.add_row("Network Mask", network.mask.ip.address, style="orchid2")
    table.add_row("Network ID", network.network_id.address, style="yellow")
    table.add_row("Broadcast Address", network.broadcast_ip.address, style="magenta")
    table.add_row("Total Addresses", str(network.total_addresses), style="cyan")
    table.add_row("Usable hosts", str(network.usable_hosts), style="red")
    table.add_row("Binary IP", network.ip.binary, style="blue")
    table.add_row("Binary Network Mask", network.mask.binary, style="orchid2")
    print()
    print(table)
