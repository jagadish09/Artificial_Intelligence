# inference.py
# ------------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import itertools
import util
import random
import busters
import game
from game import Actions
from game import Directions
from baseInference import InferenceModule
from bustersAgents import BustersAgent
from distanceCalculator import Distancer


#####################################################
#             Questions 1a and 1b                   #
#####################################################

class ExactInference(InferenceModule):
    """
    The exact dynamic inference module should use forward-algorithm
    updates to compute the exact belief function at each time step.
    """

    def initializeUniformly(self, gameState):
        "Begin with a uniform distribution over ghost positions."
        self.beliefs = util.Counter()
        for p in self.legalPositions: self.beliefs[p] = 1.0
        self.beliefs.normalize()

    def observe(self, observation, gameState):

		noisyDistance = observation
		observationDistribution = busters.getObservationDistribution(noisyDistance)
		pacmanPosition = gameState.getPacmanPosition()

		newBeliefs = util.Counter()
		
		if noisyDistance==None:
			newBeliefs[self.getJailPosition()]=1
		
		for p in self.legalPositions:
			trueDistance = util.manhattanDistance(p, pacmanPosition)
			if observationDistribution[trueDistance] > 0:
				newBeliefs[p] = self.beliefs[p]*observationDistribution[trueDistance]

		newBeliefs.normalize()
		self.beliefs = newBeliefs

        


    def elapseTime(self, gameState):

		newBeliefs = util.Counter()
		
		#if noisyDistance==None:
		#	newBeliefs[self.getJailPosition()]=1
		
		for p in self.legalPositions:
			newPosDist = self.getPositionDistribution(self.setGhostPosition(gameState, p))
			for i in newPosDist:
				newBeliefs[i]=newBeliefs[i]+self.beliefs[p]*newPosDist[i]

		newBeliefs.normalize()
		self.beliefs = newBeliefs
		
		


    def getBeliefDistribution(self):
        return self.beliefs


#####################################################
#                  Question 1c                      #
#####################################################

class GreedyBustersAgent(BustersAgent):
    "An agent that charges the closest ghost."

    def registerInitialState(self, gameState):
        "Pre-computes the distance between every two points."
        BustersAgent.registerInitialState(self, gameState)
        self.distancer = Distancer(gameState.data.layout, False)

    def chooseAction(self, gameState):

		pacmanPosition = gameState.getPacmanPosition()
		legal = [a for a in gameState.getLegalPacmanActions()]
		livingGhosts = gameState.getLivingGhosts()
		livingGhostPositionDistributions = [beliefs for i,beliefs
											in enumerate(self.ghostBeliefs)
											if livingGhosts[i+1]]
		
		point=0
		prob=0
		for i in livingGhostPositionDistributions:
			for j in i:

				if prob<i[j]:
					prob=i[j]
					point=j
		dist=9999999
		for i in legal:
			sucpos=Actions.getSuccessor(pacmanPosition, i)
			dist1=self.distancer.getDistance(sucpos, point)
			if dist>dist1:
				dist=dist1
				bestAction=i

		return bestAction


#####################################################
#             Questions 2a and 2b                   #
#####################################################

class ParticleFilter(InferenceModule):

    def __init__(self, ghostAgent, numParticles=300):
        InferenceModule.__init__(self, ghostAgent);
        self.setNumParticles(numParticles)
        self.particles = []

    def setNumParticles(self, numParticles):
        self.numParticles = numParticles


    def initializeUniformly(self, gameState):

		
		self.particles=[]
		for i in range(0,self.numParticles):
			for k in range(0,len(self.legalPositions)):
				if len(self.particles)<self.numParticles:
					self.particles.append(self.legalPositions[k])
				else:
					break
		
    def observe(self, observation, gameState):

		noisyDistance = observation
		emissionModel = busters.getObservationDistribution(noisyDistance)
		pacmanPosition = gameState.getPacmanPosition()

		if noisyDistance == None:
			for i in range(0,self.numParticles):
				self.particles = [self.getJailPosition()]
		else:
			dist = self.getBeliefDistribution()
			for point in dist:
				distance = util.manhattanDistance(pacmanPosition, point)
				dist[point] = dist[point]*emissionModel[distance]
			self.particles=[]
			sum=0
			for i in dist:
				sum=sum+dist[i]
			if sum == 0:
				self.initializeUniformly(gameState)
			else:
				dist.normalize()
				
				for i in range(0,self.numParticles):
					self.particles.append(util.sample(dist))
		
    def elapseTime(self, gameState):

		dist = []
		for i in self.particles:
			newPosDist = self.getPositionDistribution(self.setGhostPosition(gameState, i))
			dist.append(util.sampleFromCounter(newPosDist))
		self.particles = dist

    def getBeliefDistribution(self):
		dist=util.Counter()
		for i in self.particles:
			dist[i]=dist[i]+1
		dist.normalize()
		return dist

#####################################################
#             Questions 3a and 3b                   #
#####################################################

class MarginalInference(InferenceModule):
    "A wrapper around the JointInference module that returns marginal beliefs about ghosts."

    def initializeUniformly(self, gameState):
        "Set the belief state to an initial, prior value."
        if self.index == 1: jointInference.initialize(gameState, self.legalPositions)
        jointInference.addGhostAgent(self.ghostAgent)

    def observeState(self, gameState):
        "Update beliefs based on the given distance observation and gameState."
        if self.index == 1: jointInference.observeState(gameState)

    def elapseTime(self, gameState):
        "Update beliefs for a time step elapsing from a gameState."
        if self.index == 1: jointInference.elapseTime(gameState)

    def getBeliefDistribution(self):
        "Returns the marginal belief over a particular ghost by summing out the others."
        jointDistribution = jointInference.getBeliefDistribution()
        dist = util.Counter()
        for t, prob in jointDistribution.items():
            dist[t[self.index - 1]] += prob
        return dist













class JointParticleFilter:
    "JointParticleFilter tracks a joint distribution over tuples of all ghost positions."

    def __init__(self, numParticles=600):
        self.setNumParticles(numParticles)
        self.particles = []

    def setNumParticles(self, numParticles):
        self.numParticles = numParticles

    def initialize(self, gameState, legalPositions):
        "Stores information about the game, then initializes particles."
        self.numGhosts = gameState.getNumAgents() - 1
        self.ghostAgents = []
        self.legalPositions = legalPositions
        self.initializeParticles()

    def initializeParticles(self):

		perm = list(itertools.product(self.legalPositions,repeat=self.numGhosts))
		random.shuffle(perm)		
		self.particles=[]
		for i in range(0,self.numParticles):
			for k in range(0,len(perm)):
				if len(self.particles)<self.numParticles:
					self.particles.append(perm[k])
				else:
					break

    def addGhostAgent(self, agent):
        "Each ghost agent is registered separately and stored (in case they are different)."
        self.ghostAgents.append(agent)

    def getJailPosition(self, i):
        return (2 * i + 1, 1);

    def observeState(self, gameState):

		pacmanPosition = gameState.getPacmanPosition()
		noisyDistances = gameState.getNoisyGhostDistances()
		if len(noisyDistances) < self.numGhosts: return
		emissionModels = [busters.getObservationDistribution(dist) for dist in noisyDistances]

		dist = util.Counter()
		for point in self.particles:
			d =1
			for i in range(0,self.numGhosts):
				if noisyDistances[i] == None:
					point = self.getParticleWithGhostInJail(point, i)
				else:
					dis = util.manhattanDistance(point[i], pacmanPosition)
					d = d * emissionModels[i][dis]
			dist[point] =dist[point] + d
		sum=0
		for i in dist:
			sum=sum+dist[i]
		if sum==0:
			self.initializeParticles()
			for point in self.particles:
				d=1
				for i in range(0,self.numGhosts):
					if noisyDistances[i] == None:
						point = self.getParticleWithGhostInJail(point, i)
				dist[point] =dist[point] + d
						
		else:
			dist.normalize()
			points = []
			for i in range(0, self.numParticles):
				points.append(util.sample(dist))
			self.particles = points

    def getParticleWithGhostInJail(self, particle, ghostIndex):
        particle = list(particle)
        particle[ghostIndex] = self.getJailPosition(ghostIndex)
        return tuple(particle)

    def elapseTime(self, gameState):
        newParticles = []
        for oldParticle in self.particles:
            newParticle = list(oldParticle)
            for i in range(self.numGhosts):
				newPosDist = getPositionDistributionForGhost(setGhostPositions(gameState, newParticle),i, self.ghostAgents[i])
				newParticle[i]=util.sample(newPosDist)			
            newParticles.append(tuple(newParticle))
        self.particles = newParticles

    def getBeliefDistribution(self):
        		
		dist=util.Counter()
		for i in self.particles:
			dist[i]=dist[i]+1
		dist.normalize()
		return dist

# One JointInference module is shared globally across instances of MarginalInference
jointInference = JointParticleFilter()

def getPositionDistributionForGhost(gameState, ghostIndex, agent):
    """
    Returns the distribution over positions for a ghost, using the supplied gameState.
    """

    # index 0 is pacman, but the students think that index 0 is the first ghost.
    ghostPosition = gameState.getGhostPosition(ghostIndex+1)
    actionDist = agent.getDistribution(gameState)
    dist = util.Counter()
    for action, prob in actionDist.items():
        successorPosition = game.Actions.getSuccessor(ghostPosition, action)
        dist[successorPosition] = prob
    return dist

def setGhostPositions(gameState, ghostPositions):
    "Sets the position of all ghosts to the values in ghostPositionTuple."
    for index, pos in enumerate(ghostPositions):
        conf = game.Configuration(pos, game.Directions.STOP)
        gameState.data.agentStates[index + 1] = game.AgentState(conf, False)
    return gameState

