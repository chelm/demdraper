class RasterLayer(dict):
    layer_type = 'raster'

    def __init__(self, gid, url_template, **kwargs):
        self['id'] = gid
        self['type'] = self.layer_type
        self['source'] = "{}_raster".format(gid)

        for k, v in kwargs.iteritems():
            self[k] = v
        
        self.source = {
            "type": self.layer_type,
            "id": self['source'],
            "tilesize": 256,
            "tiles": [ url_template ]
            #"tiles": [ "http://idaho.geobigdata.io/v1/tile/idaho-images/9b537804-0ecc-40c8-945b-a58832dbe552/{z}/{x}/{y}?bands=4,2,1&gamma=1.3&highCutoff=0.98&lowCutoff=0.02&brightness=1.0&contrast=1.0&panId=undefined&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2RpZ2l0YWxnbG9iZS1wbGF0Zm9ybS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8Z2JkeHwyMTY2OCIsImF1ZCI6InZoYU5FSnltTDRtMVVDbzRUcVhtdUt0a245SkNZRGtUIiwiZXhwIjoxNDk2ODY3MTg1LCJpYXQiOjE0OTYyNjIzODV9.mfzG4GbRHUWPlQPuFopMzZwca6vUYP83sQ6S3fSSxek" ]
        }

