# Dem Draper

<img src="https://daeandwrite.files.wordpress.com/2015/04/mad-men-silhouette.jpg" width="500">

More than a visualization, it's an experience.  

## Install

```bash
pip install https://github.com/DigitalGlobe/demdraper/archive/master.zip && jupyter nbextension enable --py demdraper
```

## Example usage 

```python

from gbdxtools import CatalogImage, DemImage
from demdraper import Draper 

catalog_id = '1030010048532600'
bbox = [-106.95048736572267, 38.8635035952425, -106.90830230712892, 38.902522456789654]

image = CatalogImage(catalog_id, bbox=bbox)
rgb = image.rgb()

dem = DemImage(bbox=bbox, proj=image.proj)

Draper(dem, rgb, width=40, height=40)

```
