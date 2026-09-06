(globalThis.TURBOPACK||(globalThis.TURBOPACK=[])).push(["object"==typeof document?document.currentScript:void 0,28600,e=>{"use strict";var r=e.i(1950);e.s(["useThree",()=>r.C])},31067,e=>{"use strict";function r(){return(r=Object.assign.bind()).apply(null,arguments)}e.s(["default",()=>r])},39355,e=>{"use strict";var r=e.i(31067),t=e.i(71645),v=e.i(90072),u=e.i(28600),a=e.i(25234);let i={uniforms:{tDiffuse:{value:null},h:{value:1/512}},vertexShader:`
      varying vec2 vUv;

      void main() {

        vUv = uv;
        gl_Position = projectionMatrix * modelViewMatrix * vec4( position, 1.0 );

      }
  `,fragmentShader:`
    uniform sampler2D tDiffuse;
    uniform float h;

    varying vec2 vUv;

    void main() {

    	vec4 sum = vec4( 0.0 );

    	sum += texture2D( tDiffuse, vec2( vUv.x - 4.0 * h, vUv.y ) ) * 0.051;
    	sum += texture2D( tDiffuse, vec2( vUv.x - 3.0 * h, vUv.y ) ) * 0.0918;
    	sum += texture2D( tDiffuse, vec2( vUv.x - 2.0 * h, vUv.y ) ) * 0.12245;
    	sum += texture2D( tDiffuse, vec2( vUv.x - 1.0 * h, vUv.y ) ) * 0.1531;
    	sum += texture2D( tDiffuse, vec2( vUv.x, vUv.y ) ) * 0.1633;
    	sum += texture2D( tDiffuse, vec2( vUv.x + 1.0 * h, vUv.y ) ) * 0.1531;
    	sum += texture2D( tDiffuse, vec2( vUv.x + 2.0 * h, vUv.y ) ) * 0.12245;
    	sum += texture2D( tDiffuse, vec2( vUv.x + 3.0 * h, vUv.y ) ) * 0.0918;
    	sum += texture2D( tDiffuse, vec2( vUv.x + 4.0 * h, vUv.y ) ) * 0.051;

    	gl_FragColor = sum;

    }
  `},s={uniforms:{tDiffuse:{value:null},v:{value:1/512}},vertexShader:`
    varying vec2 vUv;

    void main() {

      vUv = uv;
      gl_Position = projectionMatrix * modelViewMatrix * vec4( position, 1.0 );

    }
  `,fragmentShader:`

  uniform sampler2D tDiffuse;
  uniform float v;

  varying vec2 vUv;

  void main() {

    vec4 sum = vec4( 0.0 );

    sum += texture2D( tDiffuse, vec2( vUv.x, vUv.y - 4.0 * v ) ) * 0.051;
    sum += texture2D( tDiffuse, vec2( vUv.x, vUv.y - 3.0 * v ) ) * 0.0918;
    sum += texture2D( tDiffuse, vec2( vUv.x, vUv.y - 2.0 * v ) ) * 0.12245;
    sum += texture2D( tDiffuse, vec2( vUv.x, vUv.y - 1.0 * v ) ) * 0.1531;
    sum += texture2D( tDiffuse, vec2( vUv.x, vUv.y ) ) * 0.1633;
    sum += texture2D( tDiffuse, vec2( vUv.x, vUv.y + 1.0 * v ) ) * 0.1531;
    sum += texture2D( tDiffuse, vec2( vUv.x, vUv.y + 2.0 * v ) ) * 0.12245;
    sum += texture2D( tDiffuse, vec2( vUv.x, vUv.y + 3.0 * v ) ) * 0.0918;
    sum += texture2D( tDiffuse, vec2( vUv.x, vUv.y + 4.0 * v ) ) * 0.051;

    gl_FragColor = sum;

  }
  `},n=t.forwardRef(({scale:e=10,frames:n=1/0,opacity:o=1,width:f=1,height:l=1,blur:c=1,near:m=0,far:d=10,resolution:x=512,smooth:D=!0,color:U="#000000",depthWrite:h=!1,renderOrder:g,...p},y)=>{let M,T,b=t.useRef(null),S=(0,u.useThree)(e=>e.scene),w=(0,u.useThree)(e=>e.gl),C=t.useRef(null);f*=Array.isArray(e)?e[0]:e||1,l*=Array.isArray(e)?e[1]:e||1;let[R,P,I,A,E,O,j]=t.useMemo(()=>{let e=new v.WebGLRenderTarget(x,x),r=new v.WebGLRenderTarget(x,x);r.texture.generateMipmaps=e.texture.generateMipmaps=!1;let t=new v.PlaneGeometry(f,l).rotateX(Math.PI/2),u=new v.Mesh(t),a=new v.MeshDepthMaterial;a.depthTest=a.depthWrite=!1,a.onBeforeCompile=e=>{e.uniforms={...e.uniforms,ucolor:{value:new v.Color(U)}},e.fragmentShader=e.fragmentShader.replace("void main() {",`uniform vec3 ucolor;
           void main() {
          `),e.fragmentShader=e.fragmentShader.replace("vec4( vec3( 1.0 - fragCoordZ ), opacity );","vec4( ucolor * fragCoordZ * 2.0, ( 1.0 - fragCoordZ ) * 1.0 );")};let n=new v.ShaderMaterial(i),o=new v.ShaderMaterial(s);return o.depthTest=n.depthTest=!1,[e,t,a,u,n,o,r]},[x,f,l,e,U]),B=e=>{A.visible=!0,A.material=E,E.uniforms.tDiffuse.value=R.texture,E.uniforms.h.value=e/256,w.setRenderTarget(j),w.render(A,C.current),A.material=O,O.uniforms.tDiffuse.value=j.texture,O.uniforms.v.value=e/256,w.setRenderTarget(R),w.render(A,C.current),A.visible=!1},G=0;return(0,a.useFrame)(()=>{C.current&&(n===1/0||G<n)&&(G++,M=S.background,T=S.overrideMaterial,b.current.visible=!1,S.background=null,S.overrideMaterial=I,w.setRenderTarget(R),w.render(S,C.current),B(c),D&&B(.4*c),w.setRenderTarget(null),b.current.visible=!0,S.overrideMaterial=T,S.background=M)}),t.useImperativeHandle(y,()=>b.current,[]),t.createElement("group",(0,r.default)({"rotation-x":Math.PI/2},p,{ref:b}),t.createElement("mesh",{renderOrder:g,geometry:P,scale:[1,-1,1],rotation:[-Math.PI/2,0,0]},t.createElement("meshBasicMaterial",{transparent:!0,map:R.texture,opacity:o,depthWrite:h})),t.createElement("orthographicCamera",{ref:C,args:[-f/2,f/2,l/2,-l/2,m,d]}))});e.s(["ContactShadows",0,n],39355)},31497,60602,e=>{"use strict";let r=parseInt(e.i(90072).REVISION.replace(/\D+/g,""));e.s(["version",0,r],31497);var t=e.i(1950);e.s(["useLoader",()=>t.G],60602)},67335,e=>{"use strict";var r=e.i(1950);e.s(["extend",()=>r.e])},44208,e=>{"use strict";var r=e.i(1950);e.s(["createPortal",()=>r.o])},24205,e=>{"use strict";var r=e.i(1950);e.s(["applyProps",()=>r.s])},65574,e=>{"use strict";var r=e.i(1950);e.s(["invalidate",()=>r.m])}]);