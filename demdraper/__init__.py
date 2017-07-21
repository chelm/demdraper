from .drape import Draper

def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        'src': 'static',
        'dest': 'demdraper',
        'require': 'demdraper/index'
    }]
