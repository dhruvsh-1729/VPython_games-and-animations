GlowScript 2.9 VPython

sph=sphere(pos=vector(0,0,0),radius=0.1,color=color.yellow,make_trail=True,trail_color=color.green)
dx=dy=dz=0.1
dt=0.1
t=0
while(t<=1000):
  rate()
  prob=int(1+random()*6)
  if prob==1:
    sph.pos.x+=dx
  elif prob==2:
    sph.pos.y+=dy
  #elif prob==3:
   # sph.pos.z+=dz
  elif prob==4:
    sph.pos.x=-dx
  elif prob==5:
    sph.pos.y=-dy
  #else:
  # sph.pos.z+=-dz
t+=dt    
