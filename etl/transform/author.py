import click
from xml.etree import ElementTree

from . import utils


def update_tree(tree: ElementTree, author: str):
    root = tree.getroot()
    document = root.find(path="kml:Document", namespaces=utils.ns)
    document.find(path="wpml:author", namespaces=utils.ns).text = author
    return tree


@click.command()
@click.argument("file_path")
@click.argument("author")
def main(file_path: str, author: str):
    utils.register_namespaces(file_path=file_path)
    tree = utils.load_template(file_path=file_path)
    update_tree(tree=tree, author=author)
    tree.write(file_path, xml_declaration=True, encoding="UTF-8")
