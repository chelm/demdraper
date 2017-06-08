class RasterLayer(dict):
    layer_type = 'raster'

    def __init__(self, gid, url_template, **kwargs):
        self['id'] = gid
        self['type'] = self.layer_type
        self['sourceId'] = "{}_raster".format(gid)

        for k, v in kwargs.iteritems():
            self[k] = v
        
        self.source = {
            "id": self['sourceId'],
            "tileJsonSource": { 
                "type": self.layer_type,
                "tilesize": 256,
                "tiles": [ url_template ]
            }
        }

