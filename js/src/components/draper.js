import React from 'react';
import ReactDOM from 'react-dom';

import dispatcher from './dispatcher.js';
import autobind from 'autobind-decorator';

import React3 from 'react-three-renderer';
import * as THREE from 'three';

import TrackballControls from './trackball';

class Draper extends React.Component {

  constructor( props, context ) {
    super(props, context);
    this.cameraPosition = new THREE.Vector3(0, 0, 100);

    this.state = {
      comm: null,
      dem: null,
      drape: null
    };

    this._onAnimate = (p) => {
      this.controls.update();
    };

  }

  componentWillReceiveProps( newProps ) {
    if ( newProps.dem && newProps.drape ) {
      
    }
  }

  componentWillMount(){
    dispatcher.register( payload => {
      console.log('PAYLOAD', payload)
      if ( payload.actionType === 'draper_update' ) { //&& this.state.comm === payload.data.commId ) {
        const { data = {} } = payload;
        if ( data.dem ) {
          const { vWidth, vHeight, width, height, dem: inDem } = data;
          this.loadTerrain( '/notebooks/' + inDem, buf => {
            const dem = new THREE.PlaneGeometry(vWidth, vHeight, width-1, height-1);

            let drape = null;
            if ( data.drape ) {
              drape = THREE.ImageUtils.loadTexture('/notebooks/' + data.drape );
            }

            dem.vertices.forEach( ( v, i ) => v.z = buf[i] / 65535 * 10);
            this.setState( { dem, drape } );
          } );
        }
      }
    } );
  }

  componentDidMount(){
    const controls = new TrackballControls( this.refs.mainCamera, ReactDOM.findDOMNode( this.refs.react3 ) );
    controls.rotateSpeed = 1.0;
    controls.zoomSpeed = 1.2;
    controls.panSpeed = 0.8;

    controls.noZoom = false;
    controls.noPan = false;

    controls.staticMoving = true;
    controls.dynamicDampingFactor = 0.3;

    controls.addEventListener('change', () => {
      this.setState({
        cameraPosition: this.refs.mainCamera.position,
      });
    });

    this.controls = controls;
  }

  componentWillUnmount() {
    this.controls.dispose();
    delete this.controls;
  }

  @autobind
  _update( prop, val ){
    this.setState( { [ prop ]: val } );
  }
  
  @autobind
  notify_python( data ) {
    this.props.comm.send({ method: "notify", data } );
  }

  @autobind
  loadTerrain( file, callback ) {
    const req = new XMLHttpRequest();
    req.responseType = 'arraybuffer';
    req.open('GET', file, true);
    req.onload = function(evt) {
      if (req.response) {
        callback(new Uint16Array(req.response));
      }
    };
    req.send(null);
  }

  render() {
    const { dem, drape } = this.state;
    const width = 900; // canvas width
    const height = 700; // canvas height

    return (<React3
      ref="react3"
      mainCamera="mainCamera" // this points to the perspectiveCamera which has the name set to "camera" below
      width={width}
      height={height}
      onAnimate={this._onAnimate}>
        <scene>
          <perspectiveCamera
            name="mainCamera"
            ref="mainCamera"
            fov={45}
            aspect={width / height}
            near={1}
            far={10000} 

            position={this.cameraPosition}
          />
          { dem && 
            <mesh rotation={this.state.cubeRotation}>
              <planeGeometry {...dem.parameters} vertices={ dem.vertices }/>
              { drape 
                ? <meshBasicMaterial map={drape}/>
                : <meshBasicMaterial color={0xffffff} wireframe={true}/>
              }
            </mesh>
          }
        </scene>
      </React3>
    );
  }
}

export default Draper;
