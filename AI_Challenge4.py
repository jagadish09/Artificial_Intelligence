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
In search.py, you will implement generic search algorithms and heuristics.
"""

import util
from util import Stack
from util import Queue
from util import PriorityQueue

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
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0
k=0
a=0
b=0
c=0
d=0
e=0
f=0
corners=[]
seq=[]
def aStarSearch(problem, heuristic=nullHeuristic):
	#print "start",problem.getStartState()
	#walls1=problem.walls
	#print problem.getStartState()
	#print walls1
	point=[]
	expset=[]
	frontier1=PriorityQueue()
	frontier1.push([problem.getStartState(),0,[],0],0)
	x=0
	y=0
	q=0
	expsuccessors=[]
	while 1==1:
		if frontier1.isEmpty():
			return 0
		point=frontier1.pop()
		if problem.isGoalState(point[0]):
			print "cost",problem.getCostOfActions(point[2]),point[3]
			break
		if point[0] not in expset:
			expset.append(point[0])
			
			list1=problem.getSuccessors(point[0])
			expsuccessors.append(list1)
		else:
			for j in range(0,len(expset)):
				if point[0]==expset[j]:
					list1=expsuccessors[j]
					break
		#print "succ",list1
		list3=point[2]
		for i in range(0,len(list1)):
			if list(list1[i])[0] not in expset:
				totalcost=0
				list4=[]
				list4.extend(list3)
				list4.append(list(list1[i])[1])
				totalcost=problem.getCostOfActions(list4)+heuristic(list(list1[i])[0],problem)
				frontier2=PriorityQueue()
				x=0
				y=0
				while not frontier1.isEmpty():
					p=frontier1.pop()
					if list(list1[i])[0]==p[0]:
						x=1
						if totalcost<p[3]:
							y=1
							frontier2.push([p[0],point[0],list4,totalcost],totalcost)
						else:
							frontier2.push(p,p[3])
					else:
						frontier2.push(p,p[3])
				while not frontier2.isEmpty():
					p=frontier2.pop()

					frontier1.push(p,p[3])
				
				del frontier2
				if list(list1[i])[0] not in expset and x==0:
					frontier1.push([list(list1[i])[0],point[0],list4,totalcost],totalcost)
	return point[2]


#####################################################
#                  Question 2                       #
#####################################################
def cornersHeuristic(state, problem):
	'''
	corners=list(problem.getCorners())
	cornersvisited=list(state.getCornersVisited())
	pos=state.getCurrentPos()
	i=0
	a=abs(list(corners[0])[0]-list(corners[1])[0])+abs(list(corners[0])[1]-list(corners[1])[1])
	b=abs(list(corners[1])[0]-list(corners[2])[0])+abs(list(corners[1])[1]-list(corners[2])[1])
	c=abs(list(corners[3])[0]-list(corners[2])[0])+abs(list(corners[3])[1]-list(corners[2])[1])
	for i in range(0,len(cornersvisited)):
		if cornersvisited[i]==0:
			break
	tardist=finddistance(corners[i],pos,problem)
	return abs(list(corners[i])[0]-list(pos)[0])+abs(list(corners[i])[1]-list(pos)[1])
	return 1
	'''
	
	global k,a,b,c,corners
	cornersvisited=list(state.getCornersVisited())
	pos=state.getCurrentPos()
	#print pos
	
	i=0
	j=0
	targetpath=[]
	start=problem.getStartState()
	if k==0:
		corners=list(problem.getCorners())
		#targetpath=
		findpath1(pos,corners,problem)
		print targetpath
		corners=list(problem.getCorners())
		print corners
		a=finddistance(corners[0],corners[1],problem)+1
		b=finddistance(corners[1],corners[2],problem)+1
		c=finddistance(corners[2],corners[3],problem)+1
		print a,b,c
		for l in range(0,len(targetpath)):
			for m in range(0,len(corners)):
				if targetpath[l]==corners[m]:
					seq.append(m)
					break
		
		
		k=1
	

	#print "seq",seq
	#print "cornersvisited",cornersvisited 
	#print corners[3]
	#find closest corner 
	#print "cornersvisited",cornersvisited
	if	cornersvisited[0]==0:
		tardist=finddistance(corners[0],pos,problem)
		#print "anaa,b,c",corners[0],pos,tardist,tardist+a+b+c
		return (tardist+a+b+c)
	elif	cornersvisited[1]==0:
		tardist=finddistance(corners[1],pos,problem)
		#print "anab,c",corners[1],pos,tardist,tardist+b+c
		return (tardist+b+c)
	elif	cornersvisited[2]==0:
		tardist=finddistance(corners[2],pos,problem)
		#print "ana,c",corners[2],pos,tardist,tardist+c
		return (tardist+c)
	else:
		if	cornersvisited[3]==0:
			tardist=finddistance(corners[3],pos,problem)
			#print "ana00",corners[3],pos,tardist,tardist
			return tardist
	return 0
	
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
	
targets=[]	
def findpath(point,corners1,problem):
	global targets
	frontier1=PriorityQueue()
	if len(corners1)==1:
		targets.append(corners1[0])
		return targets
	for i in range(0,len(corners1)):
		print "targets",targets,point,corners1[i]
		dist=finddistance(corners1[i],point,problem)
		frontier1.push(corners1[i],dist)
	p=frontier1.pop()
	targets.append(p)
	print "targets",targets
	corners1.remove(p)
	return findpath(p,corners1,problem)
	
def findpath1(point,corners1,problem):
	corners1.insert(0,point)
	matrix = [[0 for x in range(5)] for x in range(5)]
	for i in range(0,5):
		for j in range(0,5):
			if i==j:
				matrix[i][j]=0
			else:
				matrix[i][j]=finddistance(corners1[i],corners[j],problem)
	print matrix
	
#####################################################
#                  Question 3                       #
#####################################################

def foodHeuristic(state, problem):
    """
    Your heuristic for the FoodSearchProblem goes here.

    This heuristic must be consistent to ensure correctness.  First, try to come up
    with an admissible heuristic; almost all admissible heuristics will be consistent
    as well.

    If using A* ever finds a solution that is worse uniform cost search finds,
    your heuristic is *not* consistent, and probably not admissible!  On the other hand,
    inadmissible or inconsistent heuristics may find optimal solutions, so be careful.

    The state is a tuple ( pacmanPosition, foodGrid ) where foodGrid is a
    Grid (see game.py) of either True or False. You can call foodGrid.asList()
    to get a list of food coordinates instead.

    If you want access to info like walls, capsules, etc., you can query the problem.
    For example, problem.walls gives you a Grid of where the walls are.

    If you want to *store* information to be reused in other calls to the heuristic,
    there is a dictionary called problem.heuristicInfo that you can use. For example,
    if you only want to count the walls once and store that value, try:
      problem.heuristicInfo['wallCount'] = problem.walls.count()
    Subsequent calls to this heuristic can access problem.heuristicInfo['wallCount']
    """
    position, foodGrid = state
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
astar = aStarSearch
