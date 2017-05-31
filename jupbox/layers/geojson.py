class GeojsonLayer(dict):
    layer_type = 'geojson'

    def __init__(self, gid, features, _type, **kwargs):
        self['id'] = gid
        self['type'] = _type
        self['source'] = "{}_geojson".format(gid)

        for k, v in kwargs.iteritems():
            self[k] = v

        self.source = {
            "type": self.layer_type,
            "id": self['source'],
            "data": { 
                "type": "FeatureCollection",
                "features": list(features)
            }
        }

