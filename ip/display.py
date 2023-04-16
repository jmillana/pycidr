from rich import print
from rich.table import Table
from .ip import IpAddress, octets_to_dot_notation, get_mask_octets


def show_all(ip: IpAddress) -> None:
    table = Table(show_header=True, header_style="bold magenta")
    table.title = "IP Address Information: [bold blue]{}[/bold blue]".format(ip.ip)
    table.add_column("CIDR block", justify="center", style="cyan", no_wrap=True)
    table.add_column("Network Mask", justify="center", style="cyan", no_wrap=True)
    table.add_column("IP Address", justify="center", style="cyan", no_wrap=True)
    table.add_column("Network ID", justify="center", style="magenta")
    table.add_column("Broadcast Address", justify="center", style="green")
    table.add_column("CIDR Class", justify="center", style="blue")
    table.add_column("Total Addresses", justify="center", style="blue")
    table.add_column("Usable hosts", justify="center", style="blue")
    table.add_row(
        ip.cidr,
        octets_to_dot_notation(get_mask_octets(ip.mask)),
        ip.ip,
        ip.network_id,
        ip.broadcast_address,
        ip.cidr_class,
        str(ip.total_addresses),
        str(ip.usable_hosts),
    )
    print()
    print(table)


def show_2column_table(ip: IpAddress) -> None:
    mask_dot_notation = octets_to_dot_notation(get_mask_octets(ip.mask))
    table = Table(show_header=False, header_style="bold magenta")
    table.title = (
        f"IP Address Information for: [bold blue]{ip.ip}/{ip.mask}[/bold blue]"
    )

    table.add_row("Class", ip.cidr_class, style="green")
    table.add_row("CIDR block", f"/{ip.mask}", style="sea_green3")
    table.add_row("IP Address", ip.ip, style="blue")
    table.add_row("Network Mask", mask_dot_notation, style="orchid2")
    table.add_row("Network ID", ip.network_id, style="yellow")
    table.add_row("Broadcast Address", ip.broadcast_address, style="magenta")
    table.add_row("Total Addresses", str(ip.total_addresses), style="cyan")
    table.add_row("Usable hosts", str(ip.usable_hosts), style="red")
    table.add_row("Binary IP", ip.dotted_binary, style="blue")
    table.add_row("Binary Network Mask", ip.mask_dotted_binary, style="orchid2")
    print()
    print(table)
