import typer

from . import display
from .ipv4 import IPNetwork

app = typer.Typer()


@app.command()
def info(ip: str):
    ip_network = IPNetwork.from_cidr(ip)
    display.show_2column_table(ip_network)
