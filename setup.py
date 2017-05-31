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

extension_dir = os.path.join(os.path.dirname(__file__), "jupbox", "static")

class develop(_develop):
    try:
        def run(self):
            _develop.run(self)
            if install_nbextension is not None and ConfigManager is not None:
                install_nbextension(extension_dir, symlink=True,
                                overwrite=True, user=True, destination="jupbox")
                cm = ConfigManager()
                cm.update('notebook', {"load_extensions": {"jupbox/index": True } })
    except:
        pass

class install(_install):
    try:
        def run(self):
            _install.run(self)
            if install_nbextension is not None and ConfigManager is not None:
                cm = ConfigManager()
                cm.update('notebook', {"load_extensions": {"jupbox/index": True } })
    except:
        pass

setup(name='jupbox',
      cmdclass={'develop': develop, 'install': install},
      version='0.0.1',
      description='Python access to react-mapbox-gl for jupyter notebooks',
      url='https://github.com/chelm/jupbox',
      author='Chris Helm',
      author_email='christopeher.helm@gmail.com',
      license='MIT',
      packages=['jupbox'],
      zip_safe=False,
      data_files=[
        ('share/jupyter/nbextensions/jupbox', [
            'jupbox/static/index.js'
        ]),
      ],
      install_requires=[
          "ipython",
          "jupyter-react"
        ]
      )
