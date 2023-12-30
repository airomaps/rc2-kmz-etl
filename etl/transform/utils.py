from xml.etree import ElementTree

ns = {
    "kml": "http://www.opengis.net/kml/2.2",
    "wpml": "http://www.dji.com/wpmz/1.0.2",
}


def register_namespaces(file_path: str):
    """Preserve namespace prefixes
    https://stackoverflow.com/a/54491129
    """

    namespaces = dict([node for _, node in ElementTree.iterparse(file_path, events=['start-ns'])])
    for namespace in namespaces:
        ElementTree.register_namespace(namespace, namespaces[namespace])


def load_template(file_path: str):
    """Read the XML file located at `file_path`"""

    tree = ElementTree.parse(file_path)
    return tree


def dump_template(tree: ElementTree, file_path: str):
    """Write the tree to file.
    Preserves template XML declarations.
    """

    tree.write(file_path, xml_declaration=True, encoding="UTF-8")
