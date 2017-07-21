from setuptools import setup
from setuptools.command.develop import develop as _develop
from setuptools.command.install import install as _install
import os

try:
    from notebook.nbextensions import install_nbextension
    from notebook.services.config import ConfigManager
except ImportError:
    install_nbextension = None
    ConfigManager = None

extension_dir = os.path.join(os.path.dirname(__file__), "demdraper", "static")

class develop(_develop):
    try:
        def run(self):
            _develop.run(self)
            if install_nbextension is not None and ConfigManager is not None:
                install_nbextension(extension_dir, symlink=True,
                                overwrite=True, user=True, destination="demdraper")
                cm = ConfigManager()
                cm.update('notebook', {"load_extensions": {"demdraper/index": True } })
    except:
        pass

class install(_install):
    try:
        def run(self):
            _install.run(self)
            if install_nbextension is not None and ConfigManager is not None:
                cm = ConfigManager()
                cm.update('notebook', {"load_extensions": {"demdraper/index": True } })
    except:
        pass

setup(name='demdraper',
      cmdclass={'develop': develop, 'install': install},
      version='0.0.1',
      description='Python access to webgl stuff',
      url='https://github.com/DigitalGlobe/demdraper',
      author='Chris Helm',
      author_email='christopeher.helm@gmail.com',
      license='MIT',
      packages=['demdraper'],
      zip_safe=False,
      data_files=[
        ('share/jupyter/nbextensions/demdraper', [
            'demdraper/static/index.js'
        ]),
      ],
      install_requires=[
          "ipython",
          "jupyter-react"
        ]
      )
