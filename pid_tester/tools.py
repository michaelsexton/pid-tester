import requests
from xml.etree import ElementTree


def get_query(table,schema = 'MINRES'):
    return 'select * from {0}.{1}'.format(schema, table)


def resolve_pid(pid, feature_type, ns):
    if not pid:
        return "BLANK"
    response = requests.get(pid)
    xml = response.text
    root = ElementTree.fromstring(xml)
    xpath = "wfs:member/{0}".format(feature_type)
    nodes = root.findall(xpath, ns)
    if len(nodes) > 0:
        return "GOOD"
    return "BAD"


def resolve_vocab(vocab):
    if not vocab:
        return 'BLANK'
    response = requests.get(vocab)

