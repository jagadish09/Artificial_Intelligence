# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""
from game import Directions
from game import Agent
from game import Actions
from util import PriorityQueue

#####################################################
#                Tiny maze example                  #
#####################################################

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]


#####################################################
#                  Question 1                       #
#####################################################

def depthFirstSearch(problem):
	from game import Directions
	direction=[]
	path=[]
	path3=[]
	path.append(problem.getStartState())
	path3.append(problem.getStartState())
	expset=[]
	path1=[]
	path2=[]
	main_path=[]
	parent=[]
	while 1==1:
		if len(path)==0:
			return 0
		state1=path.pop()
		expset.append(state1)
		if problem.isGoalState(state1):
			break
			#write code for returning path from parent#
			return direction
		else :
			#add state1 to expset#
			path1=problem.getSuccessors(state1)

			for i in range(0,len(path1)):
				if list(path1[i])[0] not in path and list(path1[i])[0] not in expset:
					path.append(list(path1[i])[0])
					path3.append(list(path1[i])[0])
					main_path.append(list(path1[i])[0])
					parent.append(state1)
					direction.append(list(path1[i])[1])
	
	i=0
	g=0
	l=0
	while 1==1:
		if i<len(main_path):
			if state1==main_path[i]:
				g=1
				i+=1
			else:
				if g!=0:
					del main_path[i]
					del parent[i]
					del direction[i]
				else:
					i+=1
		else:
			break

	main_path.reverse()
	parent.reverse()
	direction.reverse()
	c=0
	'''
	while 1==1:
		print i
		if main_path[i]==state1:
			break;
		i=i+1
	'''
	i=0
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
	return direction

#####################################################
#                  Question 2                       #
#####################################################

def breadthFirstSearch(problem):
	from game import Directions
	direction=[]
	path=[]
	path3=[]
	path.append(problem.getStartState())
	path3.append(problem.getStartState())
	expset=[]
	path1=[]
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
		path1=problem.getSuccessors(state1)
		for i in range(0,len(path1)):
			if list(path1[i])[0] not in path and list(path1[i])[0] not in expset:
				path.append(list(path1[i])[0])
				path3.append(list(path1[i])[0])
				main_path.append(list(path1[i])[0])
				parent.append(state1)
				direction.append(list(path1[i])[1])
				if problem.isGoalState(list(path1[i])[0]):
					t=1
					break
		if t==1:
			break
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

	return direction
#####################################################
#                  Question 3                       #
#####################################################

def uniformCostSearch(problem):
	from game import Directions
	point=[]
	expset=[]
	final=[]
	frontier1=PriorityQueue()
	#frontier2=PriorityQueue()
	frontier1.push([problem.getStartState(),0,0,0],0)
	x=0
	y=0
	parent=[]
	while 1==1:
		if frontier1.isEmpty():
			return 0
		point=frontier1.pop()
		if problem.isGoalState(point[0]):
			break
		expset.append(point[0])
		list1=problem.getSuccessors(point[0])
		for i in range(0,len(list1)):
			totalcost=point[3]+list(list1[i])[2]
			frontier2=PriorityQueue()
			while not frontier1.isEmpty():
				x=0
				y=0
				p=frontier1.pop()
				if list(list1[i])[0]==p[0]:
					x=1
					if totalcost>p[3]:
						y=1
						frontier2.push([p[0],point[0],list(list1[i])[1],totalcost],totalcost)
					else:
						frontier2.push(p,p[3])
				else:
					frontier2.push(p,p[3])
			frontier1=frontier2
			del frontier2
			if list(list1[i])[0] not in expset and x==0:
				#frontier1.push(totalcost,totalcost)
				#frontier1.push(PriorityQueue(),(list(list1[i])[0],point[0],list(list1[i][1]),totalcost),totalcost)
				frontier1.push([list(list1[i])[0],point[0],list(list1[i][1]),totalcost],totalcost)
				parent.append([list(list1[i])[0],point[0],list(list1[i])[1]])
			else:
				if y==1:
					for m in range(0,len(parent)):
						if parent[m][0]==list(list1[i])[0]:
							parent[m][1]=point[0]
							parent[m][2]=list(list1[i])[1]
							break
	final1=[]
	point1=point[0]
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
		if point1==problem.getStartState():
			break;
	final1.reverse()
	return final1


#####################################################
#                  Question 4                       #
#####################################################
adjacent=[]
w=0
z=0
def uniformCostSearch1(problem):
	from game import Directions
	global w
	global z
	global adjacent
	point=[]
	expset=[]
	final=[]
	frontier1=PriorityQueue()
	#frontier2=PriorityQueue()
	frontier1.push([problem.getStartState(),0,0,0],0)
	x=0
	y=0
	parent=[]
	list2=problem.getSuccessors(problem.getStartState())
	w=0
	v=0
	while 1==1:
		if w<len(adjacent): 
			for n in range(0,len(list2)):
				if adjacent[w]==list(list2[n])[0]:
					list3=problem.getSuccessors(list(list2[n])[0])
					for o in range(0,len(list3)):
						if problem.isGoalState(list(list3[o])[0]):
							v=1
					if list(list(list2[n])[0])[0]>list(problem.getStartState())[0] and v==0:
						if list(list2[n])[1]=="East":
							totalcost=(0)*list(list2[n])[2]
						elif list(list2[n])[1]=="West":
							totalcost=(2)*list(list2[n])[2]
						elif list(list2[n])[1]=="North":
							totalcost=(2)*list(list2[n])[2]
						elif list(list2[n])[1]=="South":
							totalcost=(0)*list(list2[n])[2]
						frontier1.push([adjacent[w],problem.getStartState(),list(list2[n])[1],totalcost],totalcost)
						parent.append([adjacent[w],problem.getStartState(),list(list2[n])[1]])
					'''
					else:
						if list(list2[n])[1]=="East":
							totalcost=(0)*list(list2[n])[2]
						elif list(list2[n])[1]=="West":
							totalcost=(2)*list(list2[n])[2]
						elif list(list2[n])[1]=="North":
							totalcost=(2)*list(list2[n])[2]
						elif list(list2[n])[1]=="South":
							totalcost=(0)*list(list2[n])[2]
					'''
			w+=1
		else:
			break
	while 1==1:
		if frontier1.isEmpty():
			return 0
		point=frontier1.pop()
		if problem.isGoalState(point[0]):
			break
		expset.append(point[0])

		list1=problem.getSuccessors(point[0])
		for i in range(0,len(list1)):
			z=z+1
			if z<2900:
				if list(list1[i])[1]=="East":
					totalcost=point[3]+(2)*list(list1[i])[2]
				elif list(list1[i])[1]=="West":
					totalcost=point[3]+(0)*list(list1[i])[2]
				elif list(list1[i])[1]=="North":
					totalcost=point[3]+(0)*list(list1[i])[2]
				elif list(list1[i])[1]=="South":
					totalcost=point[3]+(2)*list(list1[i])[2]
			else:
				if list(list1[i])[1]=="East":
					totalcost=point[3]+(0)*list(list1[i])[2]
				elif list(list1[i])[1]=="West":
					totalcost=point[3]+(2)*list(list1[i])[2]
				elif list(list1[i])[1]=="North":
					totalcost=point[3]+(2)*list(list1[i])[2]
				elif list(list1[i])[1]=="South":
					totalcost=point[3]+(0)*list(list1[i])[2]
			frontier2=PriorityQueue()
			x=0
			y=0
			while not frontier1.isEmpty():
				p=frontier1.pop()
				if list(list1[i])[0]==p[0]:
					x=1
					if totalcost<p[3]:
						y=1
						frontier2.push([p[0],point[0],list(list1[i])[1],totalcost],totalcost)
					else:
						frontier2.push(p,p[3])
				else:
					frontier2.push(p,p[3])
			while not frontier2.isEmpty():
				p=frontier2.pop()

				frontier1.push(p,p[3])
			del frontier2
			if list(list1[i])[0] not in expset and x==0:
				#frontier1.push(totalcost,totalcost)
				#frontier1.push(PriorityQueue(),(list(list1[i])[0],point[0],list(list1[i][1]),totalcost),totalcost)
				frontier1.push([list(list1[i])[0],point[0],list(list1[i][1]),totalcost],totalcost)
				parent.append([list(list1[i])[0],point[0],list(list1[i])[1]])

			else:
				if y==1:
					for m in range(0,len(parent)):
						if parent[m][0]==list(list1[i])[0]:
							parent[m][1]=point[0]
							parent[m][2]=list(list1[i])[1]
							break			
	final1=[]
	point1=point[0]
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
		else:
			del parent[k]
		if point1==problem.getStartState():
			break;
		k=k-1
	final1.reverse()
	for m in range(0,len(parent)):
		if parent[m][0] in adjacent:
			adjacent.remove(parent[m][0])
	return final1

def getAdjacents(problem):
	list2=[]
	global adjacent
	list2=problem.getSuccessors(problem.getStartState())
	for m in range(0,len(adjacent)):
		if adjacent[m]==problem.getStartState():
			del adjacent[m]
			break
	for m in range(0,len(list2)):
		if list(list2[m])[0] not in adjacent and problem.isGoalState(list(list2[m])[0]):
			adjacent.append(list(list2[m])[0])


class ApproximateSearchAgent(Agent):
	action=[]
	def registerInitialState(self, state):
		print 0
	def getAction(self, state):
		from game import Directions
		from searchProblems import AnyFoodSearchProblem
		problem = AnyFoodSearchProblem(state)
		
		if len(self.action)==0:
			self.action=uniformCostSearch1(problem)
		getAdjacents(problem)
		point=self.action[0]
		del self.action[0]
		return point
	
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
ucs = uniformCostSearch
