import zipfile

import click


@click.command()
@click.argument("input_path")
@click.argument("output_path")
def main(input_path: str, output_path: str):
    kmz = zipfile.ZipFile(input_path, "r")
    for file_name in kmz.namelist():
        kmz.extract(member=file_name, path=output_path)
    kmz.close()
    click.echo(f"{input_path} extracted to {output_path}")
