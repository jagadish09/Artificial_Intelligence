# multiAgents.py
# --------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

from util import manhattanDistance
from game import Directions
import random, util
from game import Agent
from util import Stack
from util import Queue

def scoreEvaluationFunction(currentGameState):
  """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
  """
  return currentGameState.getScore()



class MultiAgentSearchAgent(Agent):
  """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent and AlphaBetaPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
  """

  def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
    self.index = 0 # Pacman is always agent index 0
    self.evaluationFunction = util.lookup(evalFn, globals())
    self.depth = int(depth)

	
directions=[]
corner1=0
corner2=0
dist=0	
execget=0
maindepth=0
gproblem=0
execprob=0
dist=0
goal=0
pathlist=[]
pacpath=[]
class MinimaxAgent(MultiAgentSearchAgent):
  """
    Your minimax agent (question 1)
  """  
  
  def mini(self,gstate,m,depth):
	global maindepth
	if depth==maindepth:
		m=m+1
		if (m+1) == gstate.getNumAgents():
			v=999999
			glegactions=gstate.getLegalActions(m)
			for i in glegactions:
				if i !=Directions.STOP:
					x=self.utility(gstate.generateSuccessor(m,i))
					v=min(v,x)
			if glegactions==[]:
				return self.evaluationFunction(gstate)
			return v
		else:
			v=999999
			glegactions=gstate.getLegalActions(m)
			for i in glegactions:
				if i !=Directions.STOP:
					x=self.mini(gstate.generateSuccessor(m,i),m,depth)
					v=min(v,x)
			if glegactions==[]:
				return self.evaluationFunction(gstate)
			return v
	else:
		m=m+1
		if (m+1) == gstate.getNumAgents():
			v=999999
			glegactions=gstate.getLegalActions(m)
			for i in glegactions:
				if i !=Directions.STOP:
					x=self.maxi(gstate.generateSuccessor(m,i),depth)
					v=min(v,x)
			if glegactions==[]:
				return self.evaluationFunction(gstate)
			return v
		else:
			v=999999
			glegactions=gstate.getLegalActions(m)
			for i in glegactions:
				if i !=Directions.STOP:
					x=self.mini(gstate.generateSuccessor(m,i),m,depth)
					v=min(v,x)
			if glegactions==[]:
				return self.evaluationFunction(gstate)
			return v
  def maxi(self,pstate,depth):
	depth=depth+1
	v=-999999
	plegactions=pstate.getLegalActions(0)
	for i in plegactions:
		if i !=Directions.STOP:
			x=self.mini(pstate.generateSuccessor(0,i),0,depth)
			v=max(v,x)
	if plegactions==[]:
		return self.evaluationFunction(pstate)
	return v
  def utility(self,finstate):
	return self.evaluationFunction(finstate)
  
  

  def getAction(self, gameState):
	from game import Directions
	global maindepth
	v=-999999
	maindepth=self.depth
	action=""
	legactions=gameState.getLegalActions(0)
	for i in legactions:
		if i !=Directions.STOP:
			x=self.mini(gameState.generateSuccessor(0,i),0,1)
			if x>v:
				action=i
				v=x
	return action
	
 
class AlphaBetaAgent(MultiAgentSearchAgent):
  maindepth=0
  
  
  def mini(self,gstate,m,depth,al,be):
	
	global maindepth
	if depth==maindepth:
		m=m+1
		if (m+1) == gstate.getNumAgents():
			v=999999
			glegactions=gstate.getLegalActions(m)
			for i in glegactions:
				if i !=Directions.STOP:
					x=self.utility(gstate.generateSuccessor(m,i))
					v=min(v,x)
					if v<=al:
						return v
					be=min(be,v)
			if glegactions==[]:
				return self.evaluationFunction(gstate)
			return v
		else:
			v=999999
			glegactions=gstate.getLegalActions(m)
			for i in glegactions:
				if i !=Directions.STOP:
					x=self.mini(gstate.generateSuccessor(m,i),m,depth,al,be)
					v=min(v,x)
					if v<=al:
						return v
					be=min(be,v)
			if glegactions==[]:
				return self.evaluationFunction(gstate)
			return v
	else:
		m=m+1
		if (m+1) == gstate.getNumAgents():
			v=999999
			glegactions=gstate.getLegalActions(m)
			for i in glegactions:
				if i !=Directions.STOP:
					
					x=self.maxi(gstate.generateSuccessor(m,i),depth,al,be)
					v=min(v,x)
					if v<=al:
						return v
					be=min(be,v)
			if glegactions==[]:
				return self.evaluationFunction(gstate)
			return v
		else:
			v=999999
			glegactions=gstate.getLegalActions(m)
			for i in glegactions:
				if i !=Directions.STOP:
					
					x=self.mini(gstate.generateSuccessor(m,i),m,depth,al,be)
					v=min(v,x)
					if v<=al:
						return v
					be=min(be,v)
			if glegactions==[]:
				return self.evaluationFunction(gstate)
			return v
  def maxi(self,pstate,depth,al,be):
	global pathlist
	action=""
	depth=depth+1
	v=-999999
	plegactions=pstate.getLegalActions(0)
	for i in plegactions:
		if i !=Directions.STOP:
			sg=pstate.generateSuccessor(0,i)
			pathlist.append(sg)
			x=self.mini(sg,0,depth,al,be)
			pathlist.pop()
			if x>v:
				v=x
				action=i
				if v>=be:
					return v
				al=max(al,v)
	if plegactions==[]:
		return self.evaluationFunction(pstate)
	if depth==1:
		return action
	return v
  def utility(self,finstate):
	return self.evaluationFunction(finstate)
  
  

  def getAction(self, gameState):
	from game import Directions
	global maindepth
	global gproblem
	global execprob
	execprob=0
	gproblem=gameState
	maindepth=self.depth
	v=self.maxi(gameState,0,-999999,999999)
	return v

	
	
	

  
  
  
  
def uniformCostSearch(problem):
	from game import Directions
	from util import PriorityQueue
	global directions
	point=[]
	expset=[]
	final=[]
	frontier1=PriorityQueue()
	#frontier2=PriorityQueue()
	frontier1.push([problem,problem.getPacmanPosition(),0],0)
	parent=[]
	while 1==1:
		if frontier1.isEmpty():
			return 0,0,[]
		point=frontier1.pop()

		if (problem.hasFood(point[1][0],point[1][1]) or point[1] in problem.getCapsules()) and point[1] not in problem.getGhostPositions():
			break
		expset.append(point[1])
		list1=point[0].getLegalActions(0)
		
		
		for i in list1:
			notgoal=0
			distpointpos=finddistance(point[1],point[0].generateSuccessor(0,i).getPacmanPosition(),problem)
			for j in problem.getGhostPositions():
				k=0
				l=0
				if j[0]%2==0.5 or j[0]%2==1.5:
					k=j[0]-0.5
				else:
					k=j[0]
				if j[1]%2==0.5 or j[1]%2==1.5:
					l=j[1]-0.5
				else:
					l=j[1]
				if finddistance((k,l),point[0].generateSuccessor(0,i).getPacmanPosition(),problem)+distpointpos<=2:
					expset.append(point[0].generateSuccessor(0,i).getPacmanPosition())
					notgoal=1
					break
			if notgoal==0:
				x=0
				y=0
				if i!=Directions.STOP:
					totalcost=0
					if problem.hasFood(corner1[0],corner1[1]):
						if i==directions[0][0]:
							totalcost=point[2]
						elif i==directions[0][1]:
							totalcost=point[2]
						elif i==directions[0][2]:
							totalcost=point[2]+10
						else:
							totalcost=point[2]+10
					elif problem.hasFood(corner2[0],corner2[1]):
						if i==directions[1][0]:
							totalcost=point[2]
						elif i==directions[1][1]:
							totalcost=point[2]
						elif i==directions[1][2]:
							totalcost=point[2]+10
						else:
							totalcost=point[2]+10
			
					else:
						if i==directions[2][0]:
							totalcost=point[2]
						elif i==directions[2][1]:
							totalcost=point[2]+5
						elif i==directions[2][2]:
							totalcost=point[2]+5
						else:
							totalcost=point[2]+10
				
				
				
				
					frontier2=PriorityQueue()
					while not frontier1.isEmpty():
						p=frontier1.pop()
						if point[0].generateSuccessor(0,i).getPacmanPosition()==p[1]:
							x=1
							if totalcost<p[2]:
								y=1
								frontier2.push([point[0].generateSuccessor(0,i),point[0].generateSuccessor(0,i).getPacmanPosition(),totalcost],totalcost)
							else:
								frontier2.push(p,p[2])
						else:
							frontier2.push(p,p[2])
					frontier1=frontier2
					del frontier2
					if point[0].generateSuccessor(0,i).getPacmanPosition() not in expset and x==0:
						frontier1.push([point[0].generateSuccessor(0,i),point[0].generateSuccessor(0,i).getPacmanPosition(),totalcost],totalcost)
						parent.append([point[0].generateSuccessor(0,i).getPacmanPosition(),point[1],i])
					else:
						if y==1:
							for m in range(0,len(parent)):
								if parent[m][0]==point[0].generateSuccessor(0,i).getPacmanPosition():
									parent[m][1]=point[1]
									parent[m][2]=i
									break
	final1=[]
	pacpath=[]
	point1=point[1]
	i=len(parent)-1
	while 1==1:
		if parent[i][0]!=point1:
			del parent[i]
			i=i-1
		else:
			break
		
	k=len(parent)-1
	while k>-1:
		if parent[k][0]==point1:
			pacpath.append(point1)
			final1.append(parent[k][2])
			point1=parent[k][1]
		k=k-1
		if point1==problem.getPacmanPosition():
			break;
	final1.reverse()
	pacpath.reverse()
	return len(final1),point[1],pacpath
	
	
	
	
	
	

	
def uniformCostSearch1(problem,goal):
	from game import Directions
	from util import PriorityQueue
	global directions
	point=[]
	expset=[]
	final=[]
	frontier1=PriorityQueue()
	#frontier2=PriorityQueue()
	frontier1.push([problem,problem.getPacmanPosition(),0],0)
	parent=[]
	while 1==1:
		if frontier1.isEmpty():
			return 0,0,[]
		point=frontier1.pop()

		if point[1]==goal:
			break
		expset.append(point[1])
		
		
		
		eas=0
		wes=0
		nor=0
		sou=0
		
		xheuri=point[1][0]-goal[0]
		yheuri=point[1][1]-goal[1]
		
		if xheuri==0 or yheuri==0:
			if xheuri==0:
				if yheuri<0:
					nor=0
					sou=10
					eas=1
					wes=1
				else:
					sou=0
					nor=10
					eas=1
					wes=1
			else:
				if yheuri==0:
					if xheuri>0:
						wes=0
						eas=10
						nor=1
						sou=1
					else:
						eas=0
						wes=10
						nor=1
						sou=1
		else:
			if xheuri>0:
				if yheuri>0:
					sou=0
					wes=0
					nor=2
					eas=2
				else:
					wes=0
					eas=2
					nor=0
					sou=2
			else:
				if yheuri>0:
					eas=0
					wes=2
					sou=0
					nor=2
				else:
					eas=0
					wes=2
					nor=0
					sou=2
		
		
		
		
		list1=point[0].getLegalActions(0)
		
		
		for i in list1:
			notgoal=0
			distpointpos=finddistance(point[1],point[0].generateSuccessor(0,i).getPacmanPosition(),problem)
			for r in range(1,problem.getNumAgents()):
			#for j in problem.getGhostPositions():
				j=problem.getGhostPosition(r)
				k=0
				l=0
				if j[0]%2==0.5 or j[0]%2==1.5:
					k=j[0]-0.5
				else:
					k=j[0]
				if j[1]%2==0.5 or j[1]%2==1.5:
					l=j[1]-0.5
				else:
					l=j[1]
				if finddistance((k,l),point[0].generateSuccessor(0,i).getPacmanPosition(),problem)+distpointpos<=2 and problem.getGhostState(r).scaredTimer==0:
					expset.append(point[0].generateSuccessor(0,i).getPacmanPosition())
					notgoal=1
					break
			if notgoal==0:
				x=0
				y=0
				if i!=Directions.STOP:
					
					if i==Directions.EAST:
						totalcost=point[2]+eas
					elif i==Directions.WEST:
						totalcost=point[2]+wes
					elif i==Directions.NORTH:
						totalcost=point[2]+nor
					else:
						totalcost=point[2]+sou
					
					
					#totalcost=point[2]+1
					frontier2=PriorityQueue()
					while not frontier1.isEmpty():
						p=frontier1.pop()
						if point[0].generateSuccessor(0,i).getPacmanPosition()==p[1]:
							x=1
							if totalcost<p[2]:
								y=1
								frontier2.push([point[0].generateSuccessor(0,i),point[0].generateSuccessor(0,i).getPacmanPosition(),totalcost],totalcost)
							else:
								frontier2.push(p,p[2])
						else:
							frontier2.push(p,p[2])
					frontier1=frontier2
					del frontier2
					if point[0].generateSuccessor(0,i).getPacmanPosition() not in expset and x==0:
						frontier1.push([point[0].generateSuccessor(0,i),point[0].generateSuccessor(0,i).getPacmanPosition(),totalcost],totalcost)
						parent.append([point[0].generateSuccessor(0,i).getPacmanPosition(),point[1],i])
					else:
						if y==1:
							for m in range(0,len(parent)):
								if parent[m][0]==point[0].generateSuccessor(0,i).getPacmanPosition():
									parent[m][1]=point[1]
									parent[m][2]=i
									break
	final1=[]
	pacpath=[]
	point1=point[1]
	i=len(parent)-1
	while 1==1:
		if parent[i][0]!=point1:
			del parent[i]
			i=i-1
		else:
			break
		
	k=len(parent)-1
	while k>-1:
		if parent[k][0]==point1:
			pacpath.append(point1)
			final1.append(parent[k][2])
			point1=parent[k][1]
		k=k-1
		if point1==problem.getPacmanPosition():
			break;
	final1.reverse()
	pacpath.reverse()
	return len(final1),point[1],pacpath	
	
	

	





	
def uniformlastcaps(problem,goal):
	from game import Directions
	from util import PriorityQueue
	global directions
	point=[]
	expset=[]
	final=[]
	frontier1=PriorityQueue()
	#frontier2=PriorityQueue()
	frontier1.push([problem,problem.getPacmanPosition(),0],0)
	parent=[]
	while 1==1:
		if frontier1.isEmpty():
			return 0,0,[]
		point=frontier1.pop()

		if point[1]==goal:
			break
		expset.append(point[1])
		
		
		
		eas=0
		wes=0
		nor=0
		sou=0
		
		xheuri=point[1][0]-goal[0]
		yheuri=point[1][1]-goal[1]
		
		if xheuri==0 or yheuri==0:
			if xheuri==0:
				if yheuri<0:
					nor=0
					sou=10
					eas=1
					wes=1
				else:
					sou=0
					nor=10
					eas=1
					wes=1
			else:
				if yheuri==0:
					if xheuri>0:
						wes=0
						eas=10
						nor=1
						sou=1
					else:
						eas=0
						wes=10
						nor=1
						sou=1
		else:
			if xheuri>0:
				if yheuri>0:
					sou=0
					wes=0
					nor=2
					eas=2
				else:
					wes=0
					eas=2
					nor=0
					sou=2
			else:
				if yheuri>0:
					eas=0
					wes=2
					sou=0
					nor=2
				else:
					eas=0
					wes=2
					nor=0
					sou=2
		
		
		
		
		list1=point[0].getLegalActions(0)
		
		
		for i in list1:
			notgoal=0
			distpointpos=finddistance(point[1],point[0].generateSuccessor(0,i).getPacmanPosition(),problem)
			for r in range(1,problem.getNumAgents()):
			#for j in problem.getGhostPositions():
				j=problem.getGhostPosition(r)
				k=0
				l=0
				if j[0]%2==0.5 or j[0]%2==1.5:
					k=j[0]-0.5
				else:
					k=j[0]
				if j[1]%2==0.5 or j[1]%2==1.5:
					l=j[1]-0.5
				else:
					l=j[1]
				if i!=Directions.STOP and (finddistance((k,l),point[0].generateSuccessor(0,i).getPacmanPosition(),problem)+distpointpos<=2 and problem.getGhostState(r).scaredTimer==0) or point[0].generateSuccessor(0,i).isWin():
					expset.append(point[0].generateSuccessor(0,i).getPacmanPosition())
					notgoal=1
					break
			if notgoal==0:
				x=0
				y=0
				if i!=Directions.STOP:
					
					if i==Directions.EAST:
						totalcost=point[2]+eas
					elif i==Directions.WEST:
						totalcost=point[2]+wes
					elif i==Directions.NORTH:
						totalcost=point[2]+nor
					else:
						totalcost=point[2]+sou
					
					
					#totalcost=point[2]+1
					frontier2=PriorityQueue()
					while not frontier1.isEmpty():
						p=frontier1.pop()
						if point[0].generateSuccessor(0,i).getPacmanPosition()==p[1]:
							x=1
							if totalcost<p[2]:
								y=1
								frontier2.push([point[0].generateSuccessor(0,i),point[0].generateSuccessor(0,i).getPacmanPosition(),totalcost],totalcost)
							else:
								frontier2.push(p,p[2])
						else:
							frontier2.push(p,p[2])
					frontier1=frontier2
					del frontier2
					if point[0].generateSuccessor(0,i).getPacmanPosition() not in expset and x==0:
						frontier1.push([point[0].generateSuccessor(0,i),point[0].generateSuccessor(0,i).getPacmanPosition(),totalcost],totalcost)
						parent.append([point[0].generateSuccessor(0,i).getPacmanPosition(),point[1],i])
					else:
						if y==1:
							for m in range(0,len(parent)):
								if parent[m][0]==point[0].generateSuccessor(0,i).getPacmanPosition():
									parent[m][1]=point[1]
									parent[m][2]=i
									break
	final1=[]
	pacpath=[]
	point1=point[1]
	i=len(parent)-1
	while 1==1:
		if parent[i][0]!=point1:
			del parent[i]
			i=i-1
		else:
			break
		
	k=len(parent)-1
	while k>-1:
		if parent[k][0]==point1:
			pacpath.append(point1)
			final1.append(parent[k][2])
			point1=parent[k][1]
		k=k-1
		if point1==problem.getPacmanPosition():
			break;
	final1.reverse()
	pacpath.reverse()
	return len(final1),point[1],pacpath	







	
	
	
  




def unigoal(problem,caps):
	from game import Directions
	from util import PriorityQueue
	global directions
	if problem.getPacmanPosition()==caps :
		return -1,-1
	point=[]
	expset=[]
	final=[]
	frontier1=PriorityQueue()
	#frontier2=PriorityQueue()
	frontier1.push([problem,problem.getPacmanPosition(),0],0)
	parent=[]
	while 1==1:
		if frontier1.isEmpty():
			return 0,0
		point=frontier1.pop()
		if point[1]==caps:
			break
		expset.append(point[1])
		list1=point[0].getLegalActions(0)
		for i in list1:
			x=0
			y=0
			if i!=Directions.STOP:
				totalcost=point[2]+1			
				frontier2=PriorityQueue()
				while not frontier1.isEmpty():
					p=frontier1.pop()
					if point[0].generateSuccessor(0,i).getPacmanPosition()==p[1]:
						x=1
						if totalcost<p[2]:
							y=1
							frontier2.push([point[0].generateSuccessor(0,i),point[0].generateSuccessor(0,i).getPacmanPosition(),totalcost],totalcost)
						else:
							frontier2.push(p,p[2])
					else:
						frontier2.push(p,p[2])
				frontier1=frontier2
				del frontier2
				if point[0].generateSuccessor(0,i).getPacmanPosition() not in expset and x==0:
					frontier1.push([point[0].generateSuccessor(0,i),point[0].generateSuccessor(0,i).getPacmanPosition(),totalcost],totalcost)
					parent.append([point[0].generateSuccessor(0,i).getPacmanPosition(),point[1],i])
				else:
					if y==1:
						for m in range(0,len(parent)):
							if parent[m][0]==point[0].generateSuccessor(0,i).getPacmanPosition():
								parent[m][1]=point[1]
								parent[m][2]=i
								break
	final1=[]
	point1=point[1]
	i=len(parent)-1
	while 1==1:
		if parent[i][0]!=point1:
			del parent[i]
			i=i-1
		else:
			break
		
	k=len(parent)-1
	while k>-1:
		if parent[k][0]==point1:
			final1.append(parent[k][2])
			point1=parent[k][1]
		k=k-1
		if point1==problem.getPacmanPosition():
			break;
	final1.reverse()
	return len(final1),point[1]








  
  
  
def finddistance(target,pos,problem):
	from game import Directions
	direction=[]
	path=[]
	path3=[]
	path.append(pos)
	path3.append(pos)
	expset=[]
	path2=[]
	main_path=[]
	parent=[]
	if pos==target:
		#print pos
		#print "xyz"
		return 0
	t=0
	while 1==1:
		if len(path)==0:
			return 0
		state1=path[0]
		del path[0]
		del path3[0]
		expset.append(state1)
		path1=(list(state1)[0]+1,list(state1)[1])
			
		if path1 not in path and path1 not in expset and not problem.getWalls()[list(path1)[0]][list(path1)[1]]:
			path.append(path1)
			path3.append(path1)
			main_path.append(path1)
			parent.append(state1)
			direction.append(Directions.EAST)
			if path1==target:
				t=1
				break
		
		path1=(list(state1)[0]-1,list(state1)[1])
		if path1 not in path and path1 not in expset and not problem.getWalls()[list(path1)[0]][list(path1)[1]]:
			path.append(path1)
			path3.append(path1)
			main_path.append(path1)
			parent.append(state1)
			direction.append(Directions.WEST)
			if path1==target:
				t=1
				break

		path1=(list(state1)[0],list(state1)[1]-1)
		if path1 not in path and path1 not in expset and not problem.getWalls()[list(path1)[0]][list(path1)[1]]:
			path.append(path1)
			path3.append(path1)
			main_path.append(path1)
			parent.append(state1)
			direction.append(Directions.SOUTH)
			if path1==target:
				t=1
				break

		if t==1:
			break
		
		path1=(list(state1)[0],list(state1)[1]+1)
		if path1 not in path and path1 not in expset and not problem.getWalls()[list(path1)[0]][list(path1)[1]]:
			path.append(path1)
			path3.append(path1)
			main_path.append(path1)
			parent.append(state1)
			direction.append(Directions.NORTH)
			if path1==target:
				t=1
				break				
		
		
	#print "main",main_path
	#print "parent",parent
	main_path.reverse()
	parent.reverse()
	direction.reverse()
	i=0
	c=0
	while 1==1:
		if i<=len(main_path)-1 and i<len(parent)-1:
			if parent[c]!=main_path[i+1]:
				del main_path[i+1]
				del parent[i+1]
				del direction[i+1]
			else:
				c=i+1
				i+=1
		else:
			break
	main_path.reverse()
	parent.reverse()
	direction.reverse()
	return len(direction)


def finddistance1(pos,problem):
	from game import Directions
	direction=[]
	path=[]
	path3=[]
	path.append(pos)
	path3.append(pos)
	expset=[]
	path2=[]
	main_path=[]
	parent=[]
	t=0
	while 1==1:
		if len(path)==0:
			return 0
		state1=path[0]
		del path[0]
		del path3[0]
		expset.append(state1)
		path1=(list(state1)[0]+1,list(state1)[1])
			
		if path1 not in path and path1 not in expset and not problem.getWalls()[list(path1)[0]][list(path1)[1]]:
			path.append(path1)
			path3.append(path1)
			main_path.append(path1)
			parent.append(state1)
			direction.append(Directions.EAST)
			if problem.hasFood(path1[0],path1[1]):
				t=1
				break
		
		path1=(list(state1)[0]-1,list(state1)[1])
		if path1 not in path and path1 not in expset and not problem.getWalls()[list(path1)[0]][list(path1)[1]]:
			path.append(path1)
			path3.append(path1)
			main_path.append(path1)
			parent.append(state1)
			direction.append(Directions.WEST)
			if problem.hasFood(path1[0],path1[1]):
				t=1
				break

		path1=(list(state1)[0],list(state1)[1]-1)
		if path1 not in path and path1 not in expset and not problem.getWalls()[list(path1)[0]][list(path1)[1]]:
			path.append(path1)
			path3.append(path1)
			main_path.append(path1)
			parent.append(state1)
			direction.append(Directions.SOUTH)
			if problem.hasFood(path1[0],path1[1]):
				t=1
				break

		if t==1:
			break
		
		path1=(list(state1)[0],list(state1)[1]+1)
		if path1 not in path and path1 not in expset and not problem.getWalls()[list(path1)[0]][list(path1)[1]]:
			path.append(path1)
			path3.append(path1)
			main_path.append(path1)
			parent.append(state1)
			direction.append(Directions.NORTH)
			if problem.hasFood(path1[0],path1[1]):
				t=1
				break				
		
		
	#print "main",main_path
	#print "parent",parent
	main_path.reverse()
	parent.reverse()
	direction.reverse()
	i=0
	c=0
	while 1==1:
		if i<=len(main_path)-1 and i<len(parent)-1:
			if parent[c]!=main_path[i+1]:
				del main_path[i+1]
				del parent[i+1]
				del direction[i+1]
			else:
				c=i+1
				i+=1
		else:
			break
	main_path.reverse()
	parent.reverse()
	direction.reverse()
	return len(direction),path1,main_path

	

  
  
  
  
  
  
def findfoodcorners(state):
	from game import Directions
	food1=state.getFood()
	rows=len(food1[:])
	cols=len(food1[0])
	listfood=[]
	xmin=99999999
	xmax=-99999999
	xmiymin=99999999
	xmiymax=-99999999
	xmaymin=99999999
	xmaymax=-99999999
	corners=[0,0,0,0]
	for i in range(0,rows):
		for j in range(0,cols):
			if food1[i][j]==True:
				if i<xmin:
					xmin=i
				if i>xmax:
					xmax=i
	for j in range(0,cols):
		if food1[xmin][j]==True:
			if j<xmiymin:
				xmiymin=j
				corners[0]=[(xmin,xmiymin),[Directions.SOUTH,Directions.WEST,Directions.NORTH,Directions.EAST]]
			if j>xmiymax:
				xmiymax=j
				corners[1]=[(xmin,xmiymax),[Directions.NORTH,Directions.WEST,Directions.SOUTH,Directions.EAST]]
		if food1[xmax][j]==True:
			if j<xmaymin:
				xmaymin=j
				corners[2]=[(xmax,xmaymin),[Directions.SOUTH,Directions.EAST,Directions.NORTH,Directions.WEST]]
			if j>xmaymax:
				xmaymax=j
				corners[3]=[(xmax,xmaymax),[Directions.NORTH,Directions.EAST,Directions.SOUTH,Directions.WEST]]
	return corners
	
	

	

def betterEvaluationFunction(currentGameState):
	global directions
	global corner1
	global corner2
	global dist
	global execget
	global maindepth
	global gproblem
	global execprob
	global dist
	global goal
	global pathlist
	global pacpath
	caps=[]
	food=gproblem.getFood()
	if execget==0:
		#print gproblem.getFood()
		corners=findfoodcorners(gproblem)
		clodistance=99999999
		q=0
		for i in range(0,len(corners)):
			x=finddistance(gproblem.getPacmanPosition(),corners[i][0],gproblem)
			if x<clodistance:
				q=corners[i][1]
				corner1=corners[i][0]
				clodistance=x
				
		directions.append(q)
		clodistance=99999999
		for i in range(0,len(corners)):
			if corners[i][0]!=corner1:
				x=finddistance(corner1,corners[i][0],gproblem)
				if x<clodistance:
					q=corners[i][1]
					corner2=corners[i][0]
					clodistance=x
		directions.append(q)
		
		if directions[0][0]==directions[1][0]:
			if directions[1][0]==Directions.SOUTH:
				directions.append([Directions.SOUTH,Directions.EAST,Directions.WEST,Directions.NORTH])
			else:
				directions.append([Directions.NORTH,Directions.EAST,Directions.WEST,Directions.SOUTH])
		
		else:
			if directions[1][0]==Directions.EAST:
				directions.append([Directions.EAST,Directions.NORTH,Directions.SOUTH,Directions.WEST])
			else:
				directions.append([Directions.WEST,Directions.NORTH,Directions.SOUTH,Directions.EAST])
		execget+=1	
	
	if execprob==0:
		goal=0
		dist=0
		pacpath=[]
		
		dogoal=0
		if len(gproblem.getCapsules())==1 and (finddistance(gproblem.getCapsules()[0],gproblem.getPacmanPosition(),gproblem)<=5 or gproblem.getNumFood()<=5):
			
			for r in range(1,gproblem.getNumAgents()):
				if gproblem.getGhostState(r).scaredTimer!=0:
					dogoal=1
					break
			if dogoal==0:
				dist,goal,pacpath=uniformlastcaps(gproblem,gproblem.getCapsules()[0])
				#print "goal for last caps",goal
		if goal==0:
		

		
			if (gproblem.getPacmanPosition()[0]+1,gproblem.getPacmanPosition()[1]) in gproblem.getCapsules() and dogoal==0:
				goal=(gproblem.getPacmanPosition()[0]+1,gproblem.getPacmanPosition()[1])
				dist=1
				pacpath.append((gproblem.getPacmanPosition()[0]+1,gproblem.getPacmanPosition()[1]))
			elif (gproblem.getPacmanPosition()[0]-1,gproblem.getPacmanPosition()[1]) in gproblem.getCapsules() and dogoal==0:
				goal=(gproblem.getPacmanPosition()[0]-1,gproblem.getPacmanPosition()[1])
				dist=1
				pacpath.append((gproblem.getPacmanPosition()[0]-1,gproblem.getPacmanPosition()[1]))
			elif (gproblem.getPacmanPosition()[0],gproblem.getPacmanPosition()[1]-1) in gproblem.getCapsules() and dogoal==0:
				goal=(gproblem.getPacmanPosition()[0],gproblem.getPacmanPosition()[1]-1)
				dist=1
				pacpath.append((gproblem.getPacmanPosition()[0],gproblem.getPacmanPosition()[1]-1))
			elif (gproblem.getPacmanPosition()[0],gproblem.getPacmanPosition()[1]+1) in gproblem.getCapsules() and dogoal==0:
				goal=(gproblem.getPacmanPosition()[0],gproblem.getPacmanPosition()[1]+1)
				dist=1
				pacpath.append((gproblem.getPacmanPosition()[0]-1,gproblem.getPacmanPosition()[1]+1))
			else:
			
			
				x=0
				goals=[]
				ghostdist=99999999
				for z in range(1,gproblem.getNumAgents()):
					gho=gproblem.getGhostState(z)
					if gho.scaredTimer>0:
						x+=1
						goals.append(gproblem.getGhostPosition(z))
				if x>1:
					for q in goals:
						
						k=0
						l=0
						if q[0]%2==0.5 or q[0]%2==1.5:
							k=q[0]-0.5
						else:
							k=q[0]
						if q[1]%2==0.5 or q[1]%2==1.5:
							l=q[1]-0.5
						else:
							l=q[1]
						
						d=finddistance((k,l),gproblem.getPacmanPosition(),gproblem)
						if d<ghostdist:
							ghostdist=d
							goal=(k,l)
				else:
					if x==1:
					
						q=goals[0]
						k=0
						l=0
						if q[0]%2==0.5 or q[0]%2==1.5:
							k=q[0]-0.5
						else:
							k=q[0]
						if q[1]%2==0.5 or q[1]%2==1.5:
							l=q[1]-0.5
						else:
							l=q[1]
						goal=(k,l)
						
				if goals!=[]:
					dist,goal,pacpath=uniformCostSearch1(gproblem,goal)
					#print "check ghosts",goal
				else:
					dist,goal,pacpath=uniformCostSearch(gproblem)
					#print "goal dust",goal
			'''
			if goal==0:
				dist=999999
				caps=gproblem.getCapsules()
				for i in caps:
					dist1,goal1=unigoal(gproblem,i)
					if dist1<dist:
						dist,goal=dist1,goal1
						dist1=dist
				if goal==0:
					return currentGameState.getScore()
					
			else:
				if gproblem.getNumFood()<5:
					dist2=999999
					dist10=0
					goal10=0
					caps=gproblem.getCapsules()
					if caps!=[]:
						for i in caps:
							dist1,goal1=unigoal(gproblem,i)
							if dist1<dist2:
								dist10,goal10=dist1,goal1
								dist2=dist1
						if goal10!=0:
							dist,goal=dist10,goal10
			'''
		execprob=1		
	#print goal,pacpath,pathlist
	#if goal==0:
	#	return currentGameState.getScore()
	'''
	if goal==0 and currentGameState.isLose():
		gpos=gproblem.getGhostPositions()
		if (gproblem.getPacmanPosition()[0]+1,gproblem.getPacmanPosition()[0]) not in gpos:
			goal=(gproblem.getPacmanPosition()[0]+1,gproblem.getPacmanPosition()[0])
			pacpath.append(goal)
			dist=1
		elif (gproblem.getPacmanPosition()[0]-1,gproblem.getPacmanPosition()[0]) not in gpos:
			goal=(gproblem.getPacmanPosition()[0]-1,gproblem.getPacmanPosition()[0])
			pacpath.append(goal)
			dist=1
		elif (gproblem.getPacmanPosition()[0],gproblem.getPacmanPosition()[0]+1) not in gpos:
			goal=(gproblem.getPacmanPosition()[0],gproblem.getPacmanPosition()[0]+1)
			pacpath.append(goal)
			dist=1
		else: 
			if (gproblem.getPacmanPosition()[0],gproblem.getPacmanPosition()[0]-1) not in gpos:
				goal=(gproblem.getPacmanPosition()[0],gproblem.getPacmanPosition()[0]-1)
				pacpath.append(goal)
				dist=1	
		
		score=0
		for j in pathlist:
			if j.getPacmanPosition() in pacpath:
				score=score+1000
		goal=0
		return score+currentGameState.getScore()
	'''
	'''			
	if goal==0 and not currentGameState.isLose():
		dist,goal,pacpath=finddistance1(gproblem.getPacmanPosition(),gproblem)
		score=0
		for j in pathlist:
			if j.getPacmanPosition() in pacpath:
				score=score+1000
		goal=0
		return score+currentGameState.getScore()
	'''
	
	if goal!=0 and not currentGameState.isLose():
		'''
		distcu,goalcu=unigoal(currentGameState,goal)
		if goalcu==0:
			return currentGameState.getScore()
		else:
		'''
		if currentGameState.getPacmanPosition()==goal or (currentGameState.hasFood(goal[0],goal[1])=='False' and goal not in currentGameState.getCapsules()):
			return 1000*dist+currentGameState.getScore()
		else:
			score=0
			for j in pathlist:
				if j.getPacmanPosition() in pacpath:
					score=score+1000
			return score+currentGameState.getScore()
			#return 1000*(dist-finddistance(goal,currentGameState.getPacmanPosition(),currentGameState))+currentGameState.getScore()
				
	else:
		return currentGameState.getScore()


# Abbreviation
better = betterEvaluationFunction

class UltimateAgent(MultiAgentSearchAgent):
  maindepth=0
  execprob=0
  goal=0
  pacpath=[]
  dist=0
  
  
  def finddistance(self,target,pos,problem):
	from game import Directions
	direction=[]
	path=[]
	path3=[]
	path.append(pos)
	path3.append(pos)
	expset=[]
	path2=[]
	main_path=[]
	parent=[]
	if pos==target:
		#print pos
		#print "xyz"
		return 0
	t=0
	while 1==1:
		if len(path)==0:
			return 0
		state1=path[0]
		del path[0]
		del path3[0]
		expset.append(state1)
		path1=(list(state1)[0]+1,list(state1)[1])
			
		if path1 not in path and path1 not in expset and not problem.getWalls()[list(path1)[0]][list(path1)[1]]:
			path.append(path1)
			path3.append(path1)
			main_path.append(path1)
			parent.append(state1)
			direction.append(Directions.EAST)
			if path1==target:
				t=1
				break
		
		path1=(list(state1)[0]-1,list(state1)[1])
		if path1 not in path and path1 not in expset and not problem.getWalls()[list(path1)[0]][list(path1)[1]]:
			path.append(path1)
			path3.append(path1)
			main_path.append(path1)
			parent.append(state1)
			direction.append(Directions.WEST)
			if path1==target:
				t=1
				break

		path1=(list(state1)[0],list(state1)[1]-1)
		if path1 not in path and path1 not in expset and not problem.getWalls()[list(path1)[0]][list(path1)[1]]:
			path.append(path1)
			path3.append(path1)
			main_path.append(path1)
			parent.append(state1)
			direction.append(Directions.SOUTH)
			if path1==target:
				t=1
				break

		if t==1:
			break
		
		path1=(list(state1)[0],list(state1)[1]+1)
		if path1 not in path and path1 not in expset and not problem.getWalls()[list(path1)[0]][list(path1)[1]]:
			path.append(path1)
			path3.append(path1)
			main_path.append(path1)
			parent.append(state1)
			direction.append(Directions.NORTH)
			if path1==target:
				t=1
				break				
		
		
	#print "main",main_path
	#print "parent",parent
	main_path.reverse()
	parent.reverse()
	direction.reverse()
	i=0
	c=0
	while 1==1:
		if i<=len(main_path)-1 and i<len(parent)-1:
			if parent[c]!=main_path[i+1]:
				del main_path[i+1]
				del parent[i+1]
				del direction[i+1]
			else:
				c=i+1
				i+=1
		else:
			break
	main_path.reverse()
	parent.reverse()
	direction.reverse()
	return len(direction)
  
  
  
  def uniformghost(self,problem,goal):
	from game import Directions
	from util import PriorityQueue
	global directions
	point=[]
	expset=[]
	final=[]
	frontier1=PriorityQueue()
	#frontier2=PriorityQueue()
	frontier1.push([problem,problem.getPacmanPosition(),0],0)
	parent=[]
	while 1==1:
		if frontier1.isEmpty():
			return 0,0,[]
		point=frontier1.pop()

		if point[1]==goal:
			break
		expset.append(point[1])
		
		
		
		eas=0
		wes=0
		nor=0
		sou=0
		
		xheuri=point[1][0]-goal[0]
		yheuri=point[1][1]-goal[1]
		
		if xheuri==0 or yheuri==0:
			if xheuri==0:
				if yheuri<0:
					nor=0
					sou=10
					eas=1
					wes=1
				else:
					sou=0
					nor=10
					eas=1
					wes=1
			else:
				if yheuri==0:
					if xheuri>0:
						wes=0
						eas=10
						nor=1
						sou=1
					else:
						eas=0
						wes=10
						nor=1
						sou=1
		else:
			if xheuri>0:
				if yheuri>0:
					sou=0
					wes=0
					nor=2
					eas=2
				else:
					wes=0
					eas=2
					nor=0
					sou=2
			else:
				if yheuri>0:
					eas=0
					wes=2
					sou=0
					nor=2
				else:
					eas=0
					wes=2
					nor=0
					sou=2
		
		
		
		
		list1=point[0].getLegalActions(0)
		
		
		for i in list1:
			notgoal=0
			distpointpos=finddistance(point[1],point[0].generateSuccessor(0,i).getPacmanPosition(),problem)
			for r in range(1,problem.getNumAgents()):
			#for j in problem.getGhostPositions():
				j=problem.getGhostPosition(r)
				k=0
				l=0
				if j[0]%2==0.5 or j[0]%2==1.5:
					k=j[0]-0.5
				else:
					k=j[0]
				if j[1]%2==0.5 or j[1]%2==1.5:
					l=j[1]-0.5
				else:
					l=j[1]
				if (i!=Directions.STOP  and  finddistance((k,l),point[0].generateSuccessor(0,i).getPacmanPosition(),problem)+distpointpos<=2 and problem.getGhostState(r).scaredTimer==0) or point[0].generateSuccessor(0,i).getPacmanPosition() in problem.getCapsules():
					expset.append(point[0].generateSuccessor(0,i).getPacmanPosition())
					notgoal=1
					break
			if notgoal==0:
				x=0
				y=0
				if i!=Directions.STOP:
					
					if i==Directions.EAST:
						totalcost=point[2]+eas
					elif i==Directions.WEST:
						totalcost=point[2]+wes
					elif i==Directions.NORTH:
						totalcost=point[2]+nor
					else:
						totalcost=point[2]+sou
					
					
					#totalcost=point[2]+1
					frontier2=PriorityQueue()
					while not frontier1.isEmpty():
						p=frontier1.pop()
						if point[0].generateSuccessor(0,i).getPacmanPosition()==p[1]:
							x=1
							if totalcost<p[2]:
								y=1
								frontier2.push([point[0].generateSuccessor(0,i),point[0].generateSuccessor(0,i).getPacmanPosition(),totalcost],totalcost)
							else:
								frontier2.push(p,p[2])
						else:
							frontier2.push(p,p[2])
					frontier1=frontier2
					del frontier2
					if point[0].generateSuccessor(0,i).getPacmanPosition() not in expset and x==0:
						frontier1.push([point[0].generateSuccessor(0,i),point[0].generateSuccessor(0,i).getPacmanPosition(),totalcost],totalcost)
						parent.append([point[0].generateSuccessor(0,i).getPacmanPosition(),point[1],i])
					else:
						if y==1:
							for m in range(0,len(parent)):
								if parent[m][0]==point[0].generateSuccessor(0,i).getPacmanPosition():
									parent[m][1]=point[1]
									parent[m][2]=i
									break
	final1=[]
	pacpath=[]
	point1=point[1]
	i=len(parent)-1
	while 1==1:
		if parent[i][0]!=point1:
			del parent[i]
			i=i-1
		else:
			break
		
	k=len(parent)-1
	while k>-1:
		if parent[k][0]==point1:
			pacpath.append(point1)
			final1.append(parent[k][2])
			point1=parent[k][1]
		k=k-1
		if point1==problem.getPacmanPosition():
			break;
	final1.reverse()
	pacpath.reverse()
	return len(final1),point[1],pacpath	  
  
 


  def uniformlastcaps(self,problem):
	from game import Directions
	from util import PriorityQueue
	global directions
	point=[]
	expset=[]
	final=[]
	frontier1=PriorityQueue()
	#frontier2=PriorityQueue()
	frontier1.push([problem,problem.getPacmanPosition(),0],0)
	parent=[]
	while 1==1:
		if frontier1.isEmpty():
			return 0,0,[]
		point=frontier1.pop()

		if point[1] in problem.getCapsules():
			break
		expset.append(point[1])
		
		
		
		
		list1=point[0].getLegalActions(0)
		
		
		for i in list1:
			notgoal=0
			distpointpos=finddistance(point[1],point[0].generateSuccessor(0,i).getPacmanPosition(),problem)
			for r in range(1,problem.getNumAgents()):
			#for j in problem.getGhostPositions():
				j=problem.getGhostPosition(r)
				k=0
				l=0
				if j[0]%2==0.5 or j[0]%2==1.5:
					k=j[0]-0.5
				else:
					k=j[0]
				if j[1]%2==0.5 or j[1]%2==1.5:
					l=j[1]-0.5
				else:
					l=j[1]
				if (i!=Directions.STOP  and  finddistance((k,l),point[0].generateSuccessor(0,i).getPacmanPosition(),problem)+distpointpos<=2 and problem.getGhostState(r).scaredTimer==0) and point[0].generateSuccessor(0,i).getPacmanPosition() !=goal:
					expset.append(point[0].generateSuccessor(0,i).getPacmanPosition())
					notgoal=1
					break
			if notgoal==0:
				x=0
				y=0
				if i!=Directions.STOP:
					totalcost=point[2]+1
					
					
					#totalcost=point[2]+1
					frontier2=PriorityQueue()
					while not frontier1.isEmpty():
						p=frontier1.pop()
						if point[0].generateSuccessor(0,i).getPacmanPosition()==p[1]:
							x=1
							if totalcost<p[2]:
								y=1
								frontier2.push([point[0].generateSuccessor(0,i),point[0].generateSuccessor(0,i).getPacmanPosition(),totalcost],totalcost)
							else:
								frontier2.push(p,p[2])
						else:
							frontier2.push(p,p[2])
					frontier1=frontier2
					del frontier2
					if point[0].generateSuccessor(0,i).getPacmanPosition() not in expset and x==0:
						frontier1.push([point[0].generateSuccessor(0,i),point[0].generateSuccessor(0,i).getPacmanPosition(),totalcost],totalcost)
						parent.append([point[0].generateSuccessor(0,i).getPacmanPosition(),point[1],i])
					else:
						if y==1:
							for m in range(0,len(parent)):
								if parent[m][0]==point[0].generateSuccessor(0,i).getPacmanPosition():
									parent[m][1]=point[1]
									parent[m][2]=i
									break
	final1=[]
	pacpath=[]
	point1=point[1]
	i=len(parent)-1
	while 1==1:
		if parent[i][0]!=point1:
			del parent[i]
			i=i-1
		else:
			break
		
	k=len(parent)-1
	while k>-1:
		if parent[k][0]==point1:
			pacpath.append(point1)
			final1.append(parent[k][2])
			point1=parent[k][1]
		k=k-1
		if point1==problem.getPacmanPosition():
			break;
	final1.reverse()
	pacpath.reverse()
	return len(final1),point[1],pacpath	



	
  def findfood(self,problem):
	from game import Directions
	from util import PriorityQueue
	global directions
	point=[]
	expset=[]
	final=[]
	frontier1=PriorityQueue()
	#frontier2=PriorityQueue()
	frontier1.push([problem,problem.getPacmanPosition(),0],0)
	parent=[]
	while 1==1:
		if frontier1.isEmpty():
			return 0,0,[]
		point=frontier1.pop()

		if problem.hasFood(point[1][0],point[1][1]):
			break
		expset.append(point[1])
		
		
		
		
		list1=point[0].getLegalActions(0)
		
		
		for i in list1:
			notgoal=0
			distpointpos=finddistance(point[1],point[0].generateSuccessor(0,i).getPacmanPosition(),problem)
			for r in range(1,problem.getNumAgents()):
			#for j in problem.getGhostPositions():
				j=problem.getGhostPosition(r)
				k=0
				l=0
				if j[0]%2==0.5 or j[0]%2==1.5:
					k=j[0]-0.5
				else:
					k=j[0]
				if j[1]%2==0.5 or j[1]%2==1.5:
					l=j[1]-0.5
				else:
					l=j[1]
				if (i!=Directions.STOP  and  finddistance((k,l),point[0].generateSuccessor(0,i).getPacmanPosition(),problem)+distpointpos<=2 and problem.getGhostState(r).scaredTimer==0):
					expset.append(point[0].generateSuccessor(0,i).getPacmanPosition())
					notgoal=1
					break
			if notgoal==0:
				x=0
				y=0
				if i!=Directions.STOP:
					totalcost=point[2]+1
					
					
					#totalcost=point[2]+1
					frontier2=PriorityQueue()
					while not frontier1.isEmpty():
						p=frontier1.pop()
						if point[0].generateSuccessor(0,i).getPacmanPosition()==p[1]:
							x=1
							if totalcost<p[2]:
								y=1
								frontier2.push([point[0].generateSuccessor(0,i),point[0].generateSuccessor(0,i).getPacmanPosition(),totalcost],totalcost)
							else:
								frontier2.push(p,p[2])
						else:
							frontier2.push(p,p[2])
					frontier1=frontier2
					del frontier2
					if point[0].generateSuccessor(0,i).getPacmanPosition() not in expset and x==0:
						frontier1.push([point[0].generateSuccessor(0,i),point[0].generateSuccessor(0,i).getPacmanPosition(),totalcost],totalcost)
						parent.append([point[0].generateSuccessor(0,i).getPacmanPosition(),point[1],i])
					else:
						if y==1:
							for m in range(0,len(parent)):
								if parent[m][0]==point[0].generateSuccessor(0,i).getPacmanPosition():
									parent[m][1]=point[1]
									parent[m][2]=i
									break
	final1=[]
	pacpath=[]
	point1=point[1]
	i=len(parent)-1
	while 1==1:
		if parent[i][0]!=point1:
			del parent[i]
			i=i-1
		else:
			break
		
	k=len(parent)-1
	while k>-1:
		if parent[k][0]==point1:
			pacpath.append(point1)
			final1.append(parent[k][2])
			point1=parent[k][1]
		k=k-1
		if point1==problem.getPacmanPosition():
			break;
	final1.reverse()
	pacpath.reverse()
	return len(final1),point[1],pacpath	

	




 

  
  
  
  
  def utility(self,gproblem1):
	global pathlist
	
	if self.execprob==0:
		self.goal=0
		self.pacpath=[]
		self.dist=0		
		goals=[]
		ghostdist=99999999
		x=0
		for z in range(1,gproblem.getNumAgents()):
			gho=gproblem.getGhostState(z)
			if gho.scaredTimer>0:
				x+=1
				goals.append(gproblem.getGhostPosition(z))
				
		if gproblem.getNumFood()<=5 and x<=(gproblem.getNumAgents()-2):
			self.dist,self.goal,self.pacpath=self.findfood(gproblem)
		if self.goal==0:
			if x<(gproblem.getNumAgents()/2):
				self.goal=0
				self.pacpath=[]
				self.dist=0	
				ghostdist=99999999
				gho=0
				for z in range(1,gproblem.getNumAgents()):
					
					k=0
					l=0
					g=gproblem.getGhostPosition(z)
					if g[0]%2==0.5 or g[0]%2==1.5:
						k=g[0]-0.5
					else:
						k=g[0]
					if g[1]%2==0.5 or g[1]%2==1.5:
						l=g[1]-0.5
					else:
						l=g[1]
					
					self.dist=self.finddistance((k,l),gproblem.getPacmanPosition(),gproblem)
					if self.dist<ghostdist:
						gho=gproblem.getGhostState(z)
						self.goal=(k,l)
						ghostdist=self.dist
				if gho.scaredTimer==0:
					self.goal=0
				else:
					self.dist,self.goal,self.pacpath=self.uniformghost(gproblem,self.goal)
					
				if self.goal==0:
					self.dist,self.goal,self.pacpath=self.uniformlastcaps(gproblem)
				if self.goal==0:
					self.dist,self.goal,self.pacpath=self.findfood(gproblem)

				gpos=gproblem.getGhostPositions()
				if (gproblem.getPacmanPosition()[0]+1,gproblem.getPacmanPosition()[0]) not in gpos and (gproblem.getPacmanPosition()[0]+1,gproblem.getPacmanPosition()[0]) in gproblem.getCapsules():
					self.goal=(gproblem.getPacmanPosition()[0]+1,gproblem.getPacmanPosition()[0])
					self.pacpath.append(self.goal)
					self.dist=1
				elif (gproblem.getPacmanPosition()[0]-1,gproblem.getPacmanPosition()[0]) not in gpos and (gproblem.getPacmanPosition()[0]-1,gproblem.getPacmanPosition()[0]) in gproblem.getCapsules():
					self.goal=(gproblem.getPacmanPosition()[0]-1,gproblem.getPacmanPosition()[0])
					self.pacpath.append(self.goal)
					self.dist=1
				elif (gproblem.getPacmanPosition()[0],gproblem.getPacmanPosition()[0]+1) not in gpos and (gproblem.getPacmanPosition()[0],gproblem.getPacmanPosition()[0]+1) in gproblem.getCapsules():
					self.goal=(gproblem.getPacmanPosition()[0],gproblem.getPacmanPosition()[0]+1)
					self.pacpath.append(self.goal)
					self.dist=1
				else: 
					if (gproblem.getPacmanPosition()[0],gproblem.getPacmanPosition()[0]-1) not in gpos and (gproblem.getPacmanPosition()[0],gproblem.getPacmanPosition()[0]-1) in gproblem.getCapsules():
						self.goal=(gproblem.getPacmanPosition()[0],gproblem.getPacmanPosition()[0]-1)
						self.pacpath.append(self.goal)
						self.dist=1			
				#print "ifffff",self.goal
			else:
				self.goal=0
				self.pacpath=[]
				self.dist=0	
				ghostdist=99999999

				if x>1:	
						
					for q in goals:
						
						k=0
						l=0
						if q[0]%2==0.5 or q[0]%2==1.5:
							k=q[0]-0.5
						else:
							k=q[0]
						if q[1]%2==0.5 or q[1]%2==1.5:
							l=q[1]-0.5
						else:
							l=q[1]
						
						d=self.finddistance((k,l),gproblem.getPacmanPosition(),gproblem)
						if d<ghostdist:
							ghostdist=d
							self.goal=(k,l)			
					
					if self.goal!=0:
						self.dist,self.goal,self.pacpath=self.uniformghost(gproblem,self.goal)
					if self.goal==0:
						self.dist,self.goal,self.pacpath=self.uniformlastcaps(gproblem)
					if self.goal==0:
						self.dist,self.goal,self.pacpath=self.findfood(gproblem)
					#print "elseeeee",self.goal
			#print self.goal
			
			

		self.execprob=1
	score=0	

	
	if self.goal!=0:
		if gproblem.getPacmanPosition()==self.goal or (gproblem.hasFood(self.goal[0],self.goal[1])=='False' and self.goal not in gproblem1.getCapsules()):
			return 1000*self.dist+gproblem1.getScore()
		else:
			score=0
			for j in pathlist:
				if j in self.pacpath:
					score=score+1000
			return score+gproblem1.getScore()

	
	
	
	
		
	if self.goal==0:
		return self.evaluationFunction(gproblem1)
	else:
		for j in pathlist:
			if j in self.pacpath:
				score=score+1000+gproblem1.getScore()
		return score
	
	
	
	
  
  def mini(self,gstate,m,depth,al,be):
	
	global maindepth
	if depth==maindepth:
		m=m+1
		if (m+1) == gstate.getNumAgents():
			v=999999
			glegactions=gstate.getLegalActions(m)
			for i in glegactions:
				if i !=Directions.STOP:
					x=self.utility(gstate.generateSuccessor(m,i))
					v=min(v,x)
					if v<=al:
						return v
					be=min(be,v)
			if glegactions==[]:
				return self.evaluationFunction(gstate)
			return v
		else:
			v=999999
			glegactions=gstate.getLegalActions(m)
			for i in glegactions:
				if i !=Directions.STOP:
					x=self.mini(gstate.generateSuccessor(m,i),m,depth,al,be)
					v=min(v,x)
					if v<=al:
						return v
					be=min(be,v)
			if glegactions==[]:
				return self.evaluationFunction(gstate)
			return v
	else:
		m=m+1
		if (m+1) == gstate.getNumAgents():
			v=999999
			glegactions=gstate.getLegalActions(m)
			for i in glegactions:
				if i !=Directions.STOP:
					
					x=self.maxi(gstate.generateSuccessor(m,i),depth,al,be)
					v=min(v,x)
					if v<=al:
						return v
					be=min(be,v)
			if glegactions==[]:
				return self.evaluationFunction(gstate)
			return v
		else:
			v=999999
			glegactions=gstate.getLegalActions(m)
			for i in glegactions:
				if i !=Directions.STOP:
					
					x=self.mini(gstate.generateSuccessor(m,i),m,depth,al,be)
					v=min(v,x)
					if v<=al:
						return v
					be=min(be,v)
			if glegactions==[]:
				return self.evaluationFunction(gstate)
			return v
  def maxi(self,pstate,depth,al,be):
	global pathlist
	action=""
	depth=depth+1
	v=-999999
	plegactions=pstate.getLegalActions(0)
	for i in plegactions:
		if i !=Directions.STOP:
			sg=pstate.generateSuccessor(0,i)
			pathlist.append(sg.getPacmanPosition())
			x=self.mini(sg,0,depth,al,be)
			pathlist.pop()
			if x>v:
				v=x
				action=i
				if v>=be:
					return v
				al=max(al,v)
	if plegactions==[]:
		return self.evaluationFunction(pstate)
	if depth==1:
		return action
	return v
  
  

  def getAction(self, gameState):
	from game import Directions
	global maindepth
	global gproblem
	self.execprob=0
	gproblem=gameState
	maindepth=2
	v=self.maxi(gameState,0,-999999,999999)
	return v




