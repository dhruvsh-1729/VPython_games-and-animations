GlowScript 2.9 VPython

#To construct the sliding planks

box1=box(pos=vector(0,2,0),size=vector(1,0.2,4),color=color.white,opacity=1,shininess=100)
box2=box1.clone(pos=vector(0,-2,0))

#To construct the sphere that will be our ball

ball=sphere(pos=vector(0,0,0),radius=0.5,color=color.green,make_trail=False,trail_color=color.yellow)

#To construct the rigid walls

rigidwall1=box(pos=vector(10,0,0),size=vector(0.2,4.2,4),color=color.red,opacity=1)
rigidwall2=rigidwall1.clone(pos=vector(-10,0,0))
#rigidwall=compound([rigidwall1,rigidwall2])
# Defining the compound of the two moving planks

collectionofplanks=compound([box1,box2])

ball_velocity=vector(10,10,0)
ball_acceleration=vector(0,0,0)

tmax=30
t=0
dt=0.01
while(t<=tmax):
  rate(100)
  t+=dt
  ball_velocity=ball_velocity+ball_acceleration*dt
  ball.pos=ball.pos+ball_velocity*dt
  #box1.pos.x=ball.pos.x
  #box2.pos.x=ball.pos.x
  
  collectionofplanks.pos.x=ball.pos.x
  if(box1.pos.y-ball.pos.y<1/2*box1.size.y+ball.radius or abs(ball.pos.y-box2.pos.y)<1/2*box2.size.y+ball.radius):
    ball_velocity.y=-ball_velocity.y
  if(rigidwall1.pos.x-ball.pos.x<1/2*rigidwall1.size.x+ball.radius or abs(rigidwall2.pos.x-ball.pos.x)<1/2*rigidwall2.size.x+ball.radius):
    ball_velocity.x=-ball_velocity.x
    
        

    
    
  

  
