from prov.model import ProvDocument
from prov.dot import prov_to_dot
from IPython.display import Image



def mapping_DLC(document):
    prov_template = ProvDocument()
    for namespace in document.get_registered_namespaces():
        prov_template.add_namespace(namespace)
    document.mapping(prov_template)
    return prov_template
