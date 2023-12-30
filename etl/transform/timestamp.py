import click
import time
from xml.etree import ElementTree

from . import utils


def update_tree(tree: ElementTree, timestamp: int | str):
    root = tree.getroot()
    document = root.find(path="kml:Document", namespaces=utils.ns)
    document.find(path="wpml:createTime", namespaces=utils.ns).text = timestamp
    document.find(path="wpml:updateTime", namespaces=utils.ns).text = timestamp
    return tree


@click.command()
@click.argument("file_path")
@click.option("-t", "--timestamp", help="A UNIX timestamp as an integer")
def main(file_path: str, timestamp: int | str):
    utils.register_namespaces(file_path=file_path)
    tree = utils.load_template(file_path=file_path)
    if not timestamp:
        timestamp = str(int(time.time()))
    update_tree(tree=tree, timestamp=timestamp)
    tree.write(file_path, xml_declaration=True, encoding="UTF-8")
