# Particle Swarm Otimization

# João Pedro Elger 
# Karine Faggian Franciscon

import random
import math
import matplotlib.pyplot as plt

maxx = 5 # x limit
maxy = 5 # y limit

s = 500 # Number of particles
iterations = 1000 # Number of iterations
  
minimaxi = False # MODE: Min = false | Max = true

c1 = 2
c2 = 2

# inertia weight w, where on each iteration: w = w - 3*w/iterations
w = 0.95
decrement = 3*w/iterations

pbest = []
pbestx = []
pbesty = []
gbest = 0
vx = []
vy = []
presentx = []
presenty = []
bestz = []


def fitnessfunction(x, y):
    z = -20.0*math.exp(-0.2*math.sqrt(0.5*(x*x + y*y))) - math.exp(0.5*(math.cos(2*math.pi*x) + math.cos(2*math.pi*y))) + math.e + 20 # Ackley's function
    return z

# initialization of the particles
for i in range(s):
    presentx.append(random.uniform(-1, 1)*maxx)
    presenty.append(random.uniform(-1, 1)*maxy)
    pbestx.append(presentx[i])
    pbesty.append(presenty[i])
    vx.append(1)
    vy.append(1)
      
counter = 0
if(minimaxi):
    while(counter < iterations):
        bestz.append(fitnessfunction(pbestx[gbest], pbesty[gbest]))
        w -= decrement
        for i in range(s):   

            # updates the speed
            vx[i] = w*vx[i] + c1 * random.uniform(-1, 1) * (pbestx[i] - presentx[i]) + c2 * random.uniform(-1, 1) * (pbestx[gbest] - presentx[i])
            vy[i] = w*vy[i] + c1 * random.uniform(-1, 1) * (pbesty[i] - presenty[i]) + c2 * random.uniform(-1, 1) * (pbesty[gbest] - presenty[i])
            
            # updates the positions
            presentx[i] = math.fmod((presentx[i] + vx[i]), maxx)
            presenty[i] = math.fmod((presenty[i] + vy[i]), maxy)

            # Updates best x,y position of the particle i, if necessary
            if(fitnessfunction(presentx[i], presenty[i]) > fitnessfunction(pbestx[i], pbesty[i])):
                pbestx[i] = presentx[i]         
                pbesty[i] = presenty[i]         

            # Updates best x,y position of the particle i, if necessary
            if(fitnessfunction(presentx[i], presenty[i]) > fitnessfunction(pbestx[gbest], pbesty[gbest])):         
                gbest = i
    
        counter += 1

    print("Global maximum approximation: " + str(fitnessfunction(pbestx[gbest], pbesty[gbest])))


elif(not minimaxi):
    while(counter < iterations):
        bestz.append(fitnessfunction(pbestx[gbest], pbesty[gbest]))
        w -= decrement
        for i in range(s):   

            # updates the speed
            vx[i] = w*vx[i] + c1 * random.uniform(-1, 1) * (pbestx[i] - presentx[i]) + c2 * random.uniform(-1, 1) * (pbestx[gbest] - presentx[i])
            vy[i] = w*vy[i] + c1 * random.uniform(-1, 1) * (pbesty[i] - presenty[i]) + c2 * random.uniform(-1, 1) * (pbesty[gbest] - presenty[i])
            
            # updates the position
            presentx[i] = math.fmod((presentx[i] + vx[i]), maxx)
            presenty[i] = math.fmod((presenty[i] + vy[i]), maxy)

            # Updates best x,y position of the particle i, if necessary
            if(fitnessfunction(presentx[i], presenty[i]) < fitnessfunction(pbestx[i], pbesty[i])):
                pbestx[i] = presentx[i]         
                pbesty[i] = presenty[i]         

            # Updates best x,y position of the particle i, if necessary
            if(fitnessfunction(presentx[i], presenty[i]) < fitnessfunction(pbestx[gbest], pbesty[gbest])):         
                gbest = i
             
        counter += 1

    print("Global minimum approximation: " + str(fitnessfunction(pbestx[gbest], pbesty[gbest])))

# prints the coordinates of the point with the best approximation found
print("X: " + str(pbestx[gbest]))
print("Y: " + str(pbesty[gbest]))

# plots the convergence graph
plt.subplots()
plt.plot(bestz)
plt.xlabel('Iterations')
plt.ylabel('Global Value')
plt.title('Convergence')
plt.grid()
plt.show()