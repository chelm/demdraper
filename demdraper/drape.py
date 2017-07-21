from jupyter_react import Component

from subprocess import call
import os
from scipy.misc import imsave
from skimage.transform import resize

class Draper(Component):
    module = 'Draper'
    target = 'dem.draper'

    def __init__(self, dem, drape, **kwargs):
        super(Draper, self).__init__(target_name='dem.draper', props=kwargs)
        self.width = kwargs.get("width", dem.shape[2])
        self.height = kwargs.get("height", dem.shape[1])

        print dem.shape, drape.shape, self.width, self.height
        self.dem = self._process_dem(dem)
        self.drape = self._process_drape(drape)

        #self.dem = 't.bin'
        #self.drape = 'demdraper.png'

        self.send({"method": "display"})
        self._update()

    def _update(self):
        props = {
          "dem": self.dem,
          "drape": self.drape,
          "width": self.width,
          "height": self.height
        }
        self.send({"method": "update", "props": props})

    def _process_dem(self, dem, out="demdraper.bin"):
        data = dem.read()
        #dem = resize(dem, (1, self.height, self.width))
        tif = dem.geotiff(path='demdraper.tif')
        #tif = 'demdraper.tif'

        cmd = ' '.join(['gdal_translate', '-scale', str(data.min()), str(data.max()), '0', '65535', '-outsize', str(self.width), str(self.height), '-ot', 'UInt16', '-of', 'ENVI', tif, out])
        os.system(cmd)
        return out

    def _process_drape(self, drape, out="demdraper.png"):
        drape = resize(drape, (self.height, self.width,3))
        imsave(out,drape)
        return out

