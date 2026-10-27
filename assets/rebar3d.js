/* Vista 3D de armadura: zapata + columna + dos vigas, dibujada en canvas 2D */
(function(){
const cv=document.getElementById('rebar3d'); if(!cv||!cv.getContext)return;
const ctx=cv.getContext('2d');
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
// ---------- geometría (m) ----------
const BARS=[],STIR=[],BOX=[];
const P=(x,y,z)=>[x,y,z];
function box(x0,x1,y0,y1,z0,z1){BOX.push([x0,x1,y0,y1,z0,z1])}
box(-0.7,0.7,-0.6,0,-0.7,0.7);          // zapata
box(-0.2,0.2,0,3.0,-0.2,0.2);           // columna
box(0.2,2.6,2.5,3.0,-0.125,0.125);      // viga X
box(-0.125,0.125,2.5,3.0,0.2,2.6);      // viga Z
const dL=0.019,dS=0.0095,dF=0.016;
// zapata: malla inferior en dos capas con ganchos
for(let s=-0.6;s<=0.601;s+=0.15){
  BARS.push({d:dF,pts:[P(-0.62,-0.30,s),P(-0.62,-0.52,s),P(0.62,-0.52,s),P(0.62,-0.30,s)]});
  BARS.push({d:dF,pts:[P(s,-0.30,-0.62),P(s,-0.50,-0.62),P(s,-0.50,0.62),P(s,-0.30,0.62)]});
}
// columna: 8 barras con pata en la zapata
const cb=0.15,colPos=[[-cb,-cb],[0,-cb],[cb,-cb],[cb,0],[cb,cb],[0,cb],[-cb,cb],[-cb,0]];
colPos.forEach(([x,z])=>{
  const n=Math.hypot(x,z)||1, fx=x/n*0.32, fz=z/n*0.32;
  BARS.push({d:dL,pts:[P(x+fx,-0.47,z+fz),P(x,-0.47,z),P(x,2.94,z),P(x-x/n*0.14,2.94,z-z/n*0.14)]});
});
function hoopXZ(y,h){const a=h,p=[P(-a,y,-a),P(a,y,-a),P(a,y,a),P(-a,y,a),P(-a,y,-a),P(-a+0.07,y,-a+0.07)];return p}
const ys=[-0.42,-0.27,-0.12,0.05];
for(let y=0.15;y<=0.66;y+=0.10)ys.push(y);
for(let y=0.9;y<=2.0;y+=0.25)ys.push(y);
for(let y=2.05;y<=2.46;y+=0.10)ys.push(y);
for(let y=2.6;y<=2.95;y+=0.15)ys.push(y);
ys.forEach(y=>STIR.push({d:dS,pts:hoopXZ(y,0.165)}));
// viga X
const bz=0.085;
[[2.94,-bz],[2.94,0],[2.94,bz],[2.56,-bz],[2.56,bz]].forEach(([y,z])=>{
  const down=y>2.7?-0.30:0.30;
  BARS.push({d:dL,pts:[P(-0.13,y+down,z),P(-0.13,y,z),P(2.58,y,z)]});
});
function hoopYZ(x){const y0=2.54,y1=2.96,z=0.1;return[P(x,y0,-z),P(x,y1,-z),P(x,y1,z),P(x,y0,z),P(x,y0,-z),P(x,y0+0.06,-z+0.06)]}
let xs=[0.25];for(let i=1;i<=8;i++)xs.push(0.25+0.10*i);for(let x=xs[xs.length-1]+0.2;x<2.56;x+=0.2)xs.push(x);
xs.forEach(x=>STIR.push({d:dS,pts:hoopYZ(x)}));
// viga Z (capa interior para no chocar)
[[2.91,-bz],[2.91,bz],[2.59,-bz],[2.59,0],[2.59,bz]].forEach(([y,x])=>{
  const down=y>2.7?-0.28:0.28;
  BARS.push({d:dL,pts:[P(x,y+down,-0.12),P(x,y,-0.12),P(x,y,2.58)]});
});
function hoopXY(z){const y0=2.54,y1=2.96,x=0.1;return[P(-x,y0,z),P(-x,y1,z),P(x,y1,z),P(x,y0,z),P(-x,y0,z),P(-x+0.06,y0+0.06,z)]}
let zs=[0.25];for(let i=1;i<=8;i++)zs.push(0.25+0.10*i);for(let z=zs[zs.length-1]+0.2;z<2.56;z+=0.2)zs.push(z);
zs.forEach(z=>STIR.push({d:dS,pts:hoopXY(z)}));
// segmentos
const SEG=[];
BARS.forEach(b=>{for(let i=0;i<b.pts.length-1;i++)SEG.push({a:b.pts[i],b:b.pts[i+1],d:b.d,k:0})});
STIR.forEach(b=>{for(let i=0;i<b.pts.length-1;i++)SEG.push({a:b.pts[i],b:b.pts[i+1],d:b.d,k:1})});
// caras y aristas de cajas
const FACES=[],EDGES=[];
BOX.forEach(([x0,x1,y0,y1,z0,z1])=>{
  const v=[P(x0,y0,z0),P(x1,y0,z0),P(x1,y1,z0),P(x0,y1,z0),P(x0,y0,z1),P(x1,y0,z1),P(x1,y1,z1),P(x0,y1,z1)];
  [[0,1,2,3],[4,5,6,7],[0,1,5,4],[3,2,6,7],[0,3,7,4],[1,2,6,5]].forEach(f=>FACES.push(f.map(i=>v[i])));
  [[0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],[0,4],[1,5],[2,6],[3,7]].forEach(([a,b])=>EDGES.push([v[a],v[b]]));
});
// ---------- cámara ----------
const T=[0.75,1.25,0.75];
let az=0.78, el=0.36, dist=8.6, t0=performance.now(), drag=null, autoOff=0;
let W=0,H=0,DPR=1,F=1;
function size(){const r=cv.getBoundingClientRect();DPR=Math.min(2,window.devicePixelRatio||1);W=r.width;H=r.height;cv.width=Math.round(W*DPR);cv.height=Math.round(H*DPR);F=Math.min(W,H*1.2)*1.6}
let C={};
function colors(){const s=getComputedStyle(document.documentElement);const g=n=>s.getPropertyValue(n).trim();C={ink:g('--ink'),acc:g('--accent'),mut:g('--muted'),bg:g('--surface')}}
function cam(){const c=[T[0]+dist*Math.cos(el)*Math.sin(az),T[1]+dist*Math.sin(el),T[2]+dist*Math.cos(el)*Math.cos(az)];
  let f=[T[0]-c[0],T[1]-c[1],T[2]-c[2]];const fl=Math.hypot(...f);f=f.map(x=>x/fl);
  let r=[f[1]*0-f[2]*1,f[2]*0-f[0]*0,f[0]*1-f[1]*0];/* f x up */ r=[-f[2],0,f[0]];const rl=Math.hypot(...r);r=r.map(x=>x/rl);
  const u=[r[1]*f[2]-r[2]*f[1],r[2]*f[0]-r[0]*f[2],r[0]*f[1]-r[1]*f[0]];return{c,f,r,u}}
function proj(p,K){const v=[p[0]-K.c[0],p[1]-K.c[1],p[2]-K.c[2]];const z=v[0]*K.f[0]+v[1]*K.f[1]+v[2]*K.f[2];
  return[W/2+(v[0]*K.r[0]+v[1]*K.r[1]+v[2]*K.r[2])/z*F, H*0.5-(v[0]*K.u[0]+v[1]*K.u[1]+v[2]*K.u[2])/z*F, z]}
function draw(){
  const K=cam();ctx.setTransform(DPR,0,0,DPR,0,0);ctx.clearRect(0,0,W,H);
  // sombra suelo
  ctx.globalAlpha=1;
  // caras de concreto
  ctx.fillStyle=C.mut;
  FACES.forEach(f=>{const q=f.map(p=>proj(p,K));ctx.globalAlpha=0.045;ctx.beginPath();q.forEach((p,i)=>i?ctx.lineTo(p[0],p[1]):ctx.moveTo(p[0],p[1]));ctx.closePath();ctx.fill()});
  // barras ordenadas de atrás hacia adelante
  const L=SEG.map(s=>{const a=proj(s.a,K),b=proj(s.b,K);return{a,b,z:(a[2]+b[2])/2,d:s.d,k:s.k}}).sort((p,q)=>q.z-p.z);
  const zmin=dist-3.2,zmax=dist+3.2;
  ctx.lineCap='round';ctx.lineJoin='round';
  L.forEach(s=>{
    const fog=Math.max(0,Math.min(1,(s.z-zmin)/(zmax-zmin)));
    const w=Math.max(1.1,s.d*F/s.z*1.9);
    ctx.globalAlpha=1-fog*0.55;
    ctx.strokeStyle=s.k?C.acc:C.ink;ctx.lineWidth=w;
    ctx.beginPath();ctx.moveTo(s.a[0],s.a[1]);ctx.lineTo(s.b[0],s.b[1]);ctx.stroke();
    if(w>2.2){ // brillo cilíndrico
      const dx=s.b[0]-s.a[0],dy=s.b[1]-s.a[1],n=Math.hypot(dx,dy)||1,ox=-dy/n*w*0.22,oy=dx/n*w*0.22;
      ctx.globalAlpha=(1-fog*0.55)*0.35;ctx.strokeStyle=C.bg;ctx.lineWidth=w*0.28;
      ctx.beginPath();ctx.moveTo(s.a[0]+ox,s.a[1]-Math.abs(oy));ctx.lineTo(s.b[0]+ox,s.b[1]-Math.abs(oy));ctx.stroke();
    }
  });
  // aristas de concreto
  ctx.globalAlpha=0.55;ctx.strokeStyle=C.mut;ctx.lineWidth=1;ctx.setLineDash([5,4]);
  EDGES.forEach(([a,b])=>{const p=proj(a,K),q=proj(b,K);ctx.beginPath();ctx.moveTo(p[0],p[1]);ctx.lineTo(q[0],q[1]);ctx.stroke()});
  ctx.setLineDash([]);ctx.globalAlpha=1;
}
let last=0,vis=true,cc=0;
function loop(t){
  if(vis){ if(!drag&&!reduce&&t>autoOff){az+=0.0016*Math.min(50,t-(last||t))/16}
    if(cc++%60===0)colors(); draw(); }
  last=t; requestAnimationFrame(loop);
}
cv.addEventListener('pointerdown',e=>{drag={x:e.clientX,y:e.clientY,az,el};cv.setPointerCapture(e.pointerId)});
cv.addEventListener('pointermove',e=>{if(!drag)return;az=drag.az-(e.clientX-drag.x)*0.008;el=Math.max(0.08,Math.min(1.25,drag.el+(e.clientY-drag.y)*0.006))});
const up=()=>{drag=null;autoOff=performance.now()+2500};
cv.addEventListener('pointerup',up);cv.addEventListener('pointercancel',up);
new ResizeObserver(size).observe(cv);
if('IntersectionObserver' in window)new IntersectionObserver(es=>{vis=es[0].isIntersecting}).observe(cv);
size();colors();draw();requestAnimationFrame(loop);
})();
