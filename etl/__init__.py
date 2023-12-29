import click

from etl import extract
from etl import transform


@click.group()
def cli():
    pass


cli.add_command(extract.main, name="extract")
cli.add_command(transform.main, name="transform")
