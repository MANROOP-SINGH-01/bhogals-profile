(globalThis.TURBOPACK||(globalThis.TURBOPACK=[])).push(["object"==typeof document?document.currentScript:void 0,31067,e=>{"use strict";function r(){return(r=Object.assign.bind()).apply(null,arguments)}e.s(["default",()=>r])},28600,e=>{"use strict";var r=e.i(1950);e.s(["useThree",()=>r.C])},31497,60602,e=>{"use strict";let r=parseInt(e.i(90072).REVISION.replace(/\D+/g,""));e.s(["version",0,r],31497);var t=e.i(1950);e.s(["useLoader",()=>t.G],60602)},67335,e=>{"use strict";var r=e.i(1950);e.s(["extend",()=>r.e])},24205,e=>{"use strict";var r=e.i(1950);e.s(["applyProps",()=>r.s])},44208,e=>{"use strict";var r=e.i(1950);e.s(["createPortal",()=>r.o])},39355,e=>{"use strict";var r=e.i(31067),t=e.i(71645),v=e.i(90072),u=e.i(28600),a=e.i(25234);let i={uniforms:{tDiffuse:{value:null},h:{value:1/512}},vertexShader:`
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
  `},n=t.forwardRef(({scale:e=10,frames:n=1/0,opacity:o=1,width:l=1,height:f=1,blur:c=1,near:m=0,far:d=10,resolution:x=512,smooth:h=!0,color:D="#000000",depthWrite:U=!1,renderOrder:g,...p},y)=>{let M,T,b=t.useRef(null),w=(0,u.useThree)(e=>e.scene),S=(0,u.useThree)(e=>e.gl),C=t.useRef(null);l*=Array.isArray(e)?e[0]:e||1,f*=Array.isArray(e)?e[1]:e||1;let[P,R,I,A,j,E,O]=t.useMemo(()=>{let e=new v.WebGLRenderTarget(x,x),r=new v.WebGLRenderTarget(x,x);r.texture.generateMipmaps=e.texture.generateMipmaps=!1;let t=new v.PlaneGeometry(l,f).rotateX(Math.PI/2),u=new v.Mesh(t),a=new v.MeshDepthMaterial;a.depthTest=a.depthWrite=!1,a.onBeforeCompile=e=>{e.uniforms={...e.uniforms,ucolor:{value:new v.Color(D)}},e.fragmentShader=e.fragmentShader.replace("void main() {",`uniform vec3 ucolor;
           void main() {
          `),e.fragmentShader=e.fragmentShader.replace("vec4( vec3( 1.0 - fragCoordZ ), opacity );","vec4( ucolor * fragCoordZ * 2.0, ( 1.0 - fragCoordZ ) * 1.0 );")};let n=new v.ShaderMaterial(i),o=new v.ShaderMaterial(s);return o.depthTest=n.depthTest=!1,[e,t,a,u,n,o,r]},[x,l,f,e,D]),k=e=>{A.visible=!0,A.material=j,j.uniforms.tDiffuse.value=P.texture,j.uniforms.h.value=e/256,S.setRenderTarget(O),S.render(A,C.current),A.material=E,E.uniforms.tDiffuse.value=O.texture,E.uniforms.v.value=e/256,S.setRenderTarget(P),S.render(A,C.current),A.visible=!1},B=0;return(0,a.useFrame)(()=>{C.current&&(n===1/0||B<n)&&(B++,M=w.background,T=w.overrideMaterial,b.current.visible=!1,w.background=null,w.overrideMaterial=I,S.setRenderTarget(P),S.render(w,C.current),k(c),h&&k(.4*c),S.setRenderTarget(null),b.current.visible=!0,w.overrideMaterial=T,w.background=M)}),t.useImperativeHandle(y,()=>b.current,[]),t.createElement("group",(0,r.default)({"rotation-x":Math.PI/2},p,{ref:b}),t.createElement("mesh",{renderOrder:g,geometry:R,scale:[1,-1,1],rotation:[-Math.PI/2,0,0]},t.createElement("meshBasicMaterial",{transparent:!0,map:P.texture,opacity:o,depthWrite:U})),t.createElement("orthographicCamera",{ref:C,args:[-l/2,l/2,f/2,-f/2,m,d]}))});e.s(["ContactShadows",0,n],39355)},70308,e=>{e.v(e=>Promise.resolve().then(()=>e(50471)))},26368,e=>{e.v(r=>Promise.all(["static/chunks/3zazvxpy9wdmi.js"].map(r=>e.l(r))).then(()=>r(57166)))}]);