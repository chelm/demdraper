from jupyter_react import Component

class Map(Component):
    module = 'Map'
    target = 'jup.box'

    def __init__(self, **kwargs):
        self.layers = {}
        self.sources = {}
        super(Map, self).__init__(target_name='jup.box', props=kwargs)
        self.send({"method": "display"})
        self.on_msg(self._handle_msg)

    def add_layer(self, layer):
        self.layers[layer['id']] = dict(layer)
        self.sources[layer['id']] = layer.source
        self._update()

    def remove_layer(self, _id):
        try: 
            del self.layers[_id]
            del self.sources[_id]
        except:
            pass
        self._update()

    def _update(self):
        props = {
          "layers": self.layers.values(),
          "sources": self.sources.values()
        }
        self.send({"method": "update", "props": props})

    def _handle_msg(self, msg):
        data = msg['content']['data']
        print data
        #data.get('method', '') == 'notify':
        #    self.features = data.get('data', {}).get('features', [])
