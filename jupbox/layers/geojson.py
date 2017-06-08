class GeojsonLayer(dict):
    layer_type = 'geojson'

    def __init__(self, gid, features, _type, **kwargs):
        self['id'] = gid
        self['type'] = _type
        self['sourceId'] = "{}_geojson".format(gid)

        for k, v in kwargs.iteritems():
            self[k] = v

        self.source = {
            "id": self['sourceId'],
            "geoJsonSource": {
                "type": self.layer_type,
                "data": { 
                    "type": "FeatureCollection",
                    "features": list(features)
                }
            }
        }

