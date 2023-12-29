import click

from etl import extract


@click.group()
def cli():
    pass


cli.add_command(extract.main, name="extract")
