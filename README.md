JupBox

A Python interface to [https://github.com/alex3165/react-mapbox-gl](react-mapbox-gl) for using in a Jupyter Notebook. 

## Install

```bash
pip install jupbox && jupyter nbextension enable --py jupbox
```

## Example usage 

```python

from jupbox import Map, GeoJsonLayer
from IPython.display import display

m = Map(zoom=10, center=[lon, lat], api_key='YOUR_MB_TOKEN')

layer = GeoJsonLayer(geojson, style={})

m.add_layer(layer)

display(m)
```
