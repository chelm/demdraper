import JupyterReact from 'jupyter-react-js';
import components from './components';

const target = 'dem.draper';

function load_ipython_extension () {
  requirejs([
      "base/js/namespace",
      "base/js/events",
  ], function( Jupyter, events ) {
      // initialize jupyter react cells, comm mananger and components
      const on_update = ( module, props, commId ) => {
        components.dispatcher.dispatch({
          actionType: module.toLowerCase() + '_update',
          data: Object.assign({}, props, { commId: commId }),
          commId
        });
      }
      JupyterReact.init( Jupyter, events, 'dem.draper', { components, on_update } );
  });
}

module.exports = {
  load_ipython_extension: load_ipython_extension
};
