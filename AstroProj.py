import matplotlib.pyplot as plt
import numpy as np
import math

#set constants

#meteor constants
g=         9.81 #gravity
mm=        .029 #molar mass
gc=        8.134 #gas constant
SurfaceAD= .122 #density of surface air
temp=      200.0  #temp of gas in k
zet=       6.0*pow(10,6)        #latent heat coefficient
gam=       1.0    #drag coefficient
re=        6.4*pow(10,6) #distance to center of earth
ts=        .0005 #time step
density=   .005 #g/cm^3
height=     250.0 #height of meteor km
velocity=  30.0 #velocity of meteor km/s
mass=      500.0 #mass of meteor g
zu=        45*(math.pi/180) #angle of meteor in radians
lamb=1

#observer constants
Do = 100 #initial observer x distance from meteor

x=[] #plot coord
y=[]

y1=[]

i=0
v=velocity*1000 #puts into meters
m=mass
h=height*1000 #puts into meters
lightInt= 0.0 #intensity
mg=0.0 #magnitude

def newGrav ( re,height):

    return g*((re/(re+height))**2)

def AtmosphericDensity ( height):

    return SurfaceAD*math.exp((-mm*newGrav(re,height)*height)/(gc*temp))

def velo( velocity, mass, height):
    
    return -gam*math.exp((-1/3)*math.log(mass))*math.exp((-2/3)*math.log(density))*AtmosphericDensity(height)*(velocity**2)

def intensity(velocity, mass, height): #mass burned off

    return -lamb*math.exp((2/3)*math.log(mass/density))*AtmosphericDensity(height)*math.exp(3*math.log(velocity))/(2*zet)

def veloChange(velocity, mass, height):

    dv = velo(velocity,mass,height)*ts
   
    return velocity + dv

def heightChange(height):
    
    dh= v*ts*math.cos(zu)

    return height-dh

def angle(height): # was 's'

    return height/math.cos(zu)

def massChange(velocity, mass, height):

    dmdt= intensity(velocity,mass, height)
   
    return mass+dmdt*ts

def tau(velocity):

    if (velocity>16000):
        tau=.024/(velocity+8.8)
    else:
        tau=6.04*pow(10,-4)*math.exp((-.35)*math.log(velocity-8.8))

    return tau

def lum(tau, velocity, mass, height):
    
    return tau*math.exp((2/3)*math.log(mass/density))*AtmosphericDensity(height)*math.exp(5*math.log(velocity))/(4*zet)

def magnitude(lum, angle):

    return -14.01-2.5*math.log(lum/math.sqrt(angle))/math.log(10)


def Simulate(velocity, mass, height):
     
     return

while (v>=1000 and m>=.5):

    dv= velo(v,m,h)*ts #change in velocity
    v= v+dv #new velocity

    dh= v*ts*math.cos(zu) #change in height
    h=h-dh #new height
  
    dd=h/math.cos(zu) #s is distance traveled by meteor in x direction

    Df=Do-dd #new x distrance from observer

    D=math.sqrt((h**2)+(Df**2)) # direct distance from observer (hypotenuse) 
  
    dmdt= intensity(v,m,h) #change in mass
   
    m=m+dmdt*ts #new mass
    

    if (v>16000): #sets meteor coefficient tau
        tau=.024/(v+8.8)
    else:
        tau=6.04*pow(10,-4)*math.exp((-.35)*math.log(v-8.8))

    lightInt = tau*math.exp((2/3)*math.log(m/density))*AtmosphericDensity(h)*math.exp(5*math.log(v))/(4*zet)
 
    mg = (-14.01-2.5*math.log(lightInt/dd**2)/math.log(10)) #apaprent magnitude
    #mgo=

    y.append(lightInt) #adds light intensity result to the array
    x.append(ts* i) #multiplies time step by times the while loop runs to find time then saves this

    y1.append(m)

    i+=1
    #print ("velocity= ",v," Mass= ",m," Height= ",h," Is= ",lightInt," Mg= ",mg)

print ("velocity= ",v," Mass= ",m," Height= ",h," Is= ",lightInt," Mg= ",mg)

print(i)
plt.ylabel('Light Intensity')
plt.xlabel('Time')
plt.grid(True)
plt.title('F-Curve')

plt.plot(x[0:i], y[0:i])
plt.show()



