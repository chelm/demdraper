from .map import Map
from .layers import GeojsonLayer
from .layers import RasterLayer

def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        'src': 'static',
        'dest': 'jupbox',
        'require': 'jupbox/index'
    }]
