import click

from . import author
from . import timestamp


@click.group()
def main():
    pass


main.add_command(author.main, name="author")
main.add_command(timestamp.main, name="time")
