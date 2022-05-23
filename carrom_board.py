GlowScript 2.9 VPython

board=box(pos=vector(0,0,0),size=vector(10,10,0.2),color=color.red)
#strike=shapes.circle(radius=0.4)
#striker_path=[vector(0,-4.5,0),vector(0,-4.5,0.4)]
#striker=extrusion(path=striker_path,shape=strike)
sph=sphere(pos=vector(0,0,.5),radius=.5,color=color.yellow,velocity=vector(-8,5,0),make_trail=True,retain=100,trail_color=color.blue)
rigwall1=box(pos=vector(5,0,0),size=vector(0.5,10,0.8),color=color.green)
rigwall2=rigwall1.clone(pos=vector(-5,0,0))
rigwall3=box(pos=vector(0,-5,0),size=vector(10,0.5,0.5),color=color.green)
rigwall4=rigwall3.clone(pos=vector(0,5,0))
t=0
dt=0.01
tmax=3
while(True):
  rate(100)
  sph.pos=sph.pos+sph.velocity*dt
  t+=dt
  #striker.pos.x=striker.pos.x+dx
  #striker.pos.y=striker.pos.y+dy
  #striker.pos=striker.pos+striker.velocity*dt
  #if(abs(striker.pos)>board.size.x-striker.radius):
   # striker.velocity.y=-striker.velocity.y
  #if(abs(striker.pos)>board.size.y-striker.radius):
   # striker.velocity.x=-striker.velocity.x
   
  if(abs(sph.pos.x)>1/2*board.size.x-sph.radius):
    sph.velocity.x=-sph.velocity.x
  if(abs(sph.pos.y)>1/2*board.size.y-sph.radius):
    sph.velocity.y=-sph.velocity.y
    
