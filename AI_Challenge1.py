# your_Agents.py
# ---------
# COSC4550/COSC5550
# Artificial Intelligence
# University of Wyoming
# ---------
# Most code was part of the Pacman AI projects by John DeNero and Dan Klein
# Code has been modified for the Cleaning Agents AI Challenge by Joost Huizinga
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
This file contains all of the agents that can be selected to 
control our cleaner robot.  To select an agent, use the '-p' option
when running cleaner.py. 

Please only change the parts of the file you are asked to.
Look for the lines that say

# YOUR CODE HERE #

Good luck!
"""
from game import Directions
from game import Agent
from game import RobotActions
from game import Grid
from sets import Set
import util
import time
import random

class BasicAgent(Agent):
  "An agent that goes Forward until it can't, and then turns in a random direction."
  def getAction(self, state):
    "The agent receives an AgentState (defined in game.py)."
    if state.frontWallSensor == 1:
      if random.random() < 0.5:
        action = RobotActions.TURN_AND_MOVE_LEFT
      else:
        action = RobotActions.TURN_AND_MOVE_RIGHT
    else:
      action = RobotActions.FORWARD

    return action

class SimpleReflexAgent(Agent):
  "A reflex agent you have to implement"
  
  def getAction(self, state):
	fd=state.frontDustSensor
	ld=state.leftDustSensor
	rd=state.rightDustSensor
	fw=state.frontWallSensor
	rw=state.rightWallSensor
	bw=state.backWallSensor
	lw=state.leftWallSensor
	if fd > 1:
		action=RobotActions.FORWARD
		return action
	elif ld>1:
		action=RobotActions.TURN_AND_MOVE_LEFT
		return action
	elif rd>1:
		action=RobotActions.TURN_AND_MOVE_RIGHT
		return action
	elif fd==1:
		action=RobotActions.FORWARD
		return action
	elif ld==1:
		action=RobotActions.TURN_AND_MOVE_LEFT
		return action
	elif rd==1:
		action=RobotActions.TURN_AND_MOVE_RIGHT
		return action
	elif fd==0.5 and fw>2:
		action=RobotActions.FORWARD
		return action
	elif ld==0.5 and lw>2:
		action=RobotActions.TURN_AND_MOVE_LEFT
		return action
	elif rd==0.5 and rw>2:
		action=RobotActions.TURN_AND_MOVE_RIGHT
		return action
	elif fw==2:
		if random.random() < 0.5:
			action=RobotActions.FORWARD
			return action
		elif rw<=1 and lw<=1:
			action=RobotActions.TURN_LEFT
			return action
		elif rw<=1 and lw>=2:
			action=RobotActions.TURN_AND_MOVE_LEFT
			return action
		elif lw<=1 and rw>=2:
			action=RobotActions.TURN_AND_MOVE_RIGHT
			return action
		elif rw <= 2 and lw>2:
			action=RobotActions.TURN_AND_MOVE_LEFT
			return action
		elif rw > 2 and lw <=2:
			action=RobotActions.TURN_AND_MOVE_RIGHT
			return action
		else :
			if random.random() < 0.5:
				action=RobotActions.TURN_AND_MOVE_LEFT
				return action
			else:
				action=RobotActions.TURN_AND_MOVE_RIGHT
				return action
	elif fw <= 1 :
		if rw<=1 and lw<=1:
			action=RobotActions.TURN_LEFT
			return action
		elif rw<=1 and lw>=2:
			action=RobotActions.TURN_AND_MOVE_LEFT
			return action
		elif lw<=1 and rw>=2:
			action=RobotActions.TURN_AND_MOVE_RIGHT
			return action
		elif rw <= 2 and lw>2:
			action=RobotActions.TURN_AND_MOVE_LEFT
			return action
		elif rw > 2 and lw <=2:
			action=RobotActions.TURN_AND_MOVE_RIGHT
			return action
		else :
			if random.random() < 0.5:
				action=RobotActions.TURN_AND_MOVE_LEFT
				return action
			else:
				action=RobotActions.TURN_AND_MOVE_RIGHT
				return action
		
	elif rw<=1 and lw>1 and fw> 1:
		if random.random()<0.5:
			action=RobotActions.FORWARD
			return action
		else :
			action=RobotActions.TURN_AND_MOVE_LEFT
			return action
	elif rw>1 and lw<=1 and fw > 1:
		if random.random()<0.5:
			action = RobotActions.FORWARD
			return action
		else:
			action=RobotActions.TURN_AND_MOVE_RIGHT
			return action

	elif bw<3 and lw==1 and lw!=rw:
			action=RobotActions.TURN_AND_MOVE_RIGHT
			return action
	elif bw<3 and rw==1 and lw!=rw:
			action=RobotActions.TURN_AND_MOVE_LEFT
			return action
	elif fw > 1 :
		action=RobotActions.FORWARD
		return action

	else :
		if random.random() < 0.5:
			action=RobotActions.TURN_AND_MOVE_RIGHT
			return action
		else:
			action=RobotActions.TURN_AND_MOVE_LEFT
			return action
	'''
	elif dir=="West":
		if state.rightWallSensor<=1 and state.leftWallSensor>1 and state.frontWallSensor>1:
			if random.random()<0.5:
				action=RobotActions.FORWARD
				
			else:
				action=RobotActions.TURN_AND_MOVE_LEFT
		elif state.rightWallSensor>1 and state.leftWallSensor<=1 and state.frontWallSensor>1:
			if random.random()<0.5:
				action = RobotActions.FORWARD
			else:
				action=RobotActions.TURN_AND_MOVE_RIGHT
				
		elif state.frontWallSensor > 1 :
			action=RobotActions.FORWARD
		elif state.frontWallSensor <= 1 :
			if state.rightWallSensor <= 1 and state.leftWallSensor >1:
				action=RobotActions.TURN_AND_MOVE_LEFT
			elif state.rightWallSensor > 1 and state.leftWallSensor <=1:
				action=RobotActions.TURN_AND_MOVE_RIGHT
			else :
				if random.random() < 0.5:
					action=RobotActions.TURN_RIGHT
				else:
					action=RobotActions.TURN_LEFT

		else :
			if random.random() < 0.5:
				action=RobotActions.TURN_RIGHT
			else:
				action=RobotActions.TURN_LEFT
	elif dir=="North":
		if state.rightWallSensor<=1 and state.leftWallSensor>1 and state.frontWallSensor>1:
			if random.random()<0.5:
				action = RobotActions.FORWARD
			else :
				action=RobotActions.TURN_AND_MOVE_LEFT
		elif state.rightWallSensor>1 and state.leftWallSensor<=1 and state.frontWallSensor>1:
			if random.random()<0.5:
				action = RobotActions.FORWARD
			else:
				action=RobotActions.TURN_AND_MOVE_RIGHT
		elif state.frontWallSensor > 1 :
			action=RobotActions.FORWARD
		elif state.frontWallSensor <= 1 :
			if state.rightWallSensor <= 1 and state.leftWallSensor >1:
				action=RobotActions.TURN_AND_MOVE_LEFT
			elif state.rightWallSensor > 1 and state.leftWallSensor <=1:
				action=RobotActions.TURN_AND_MOVE_RIGHT
			else :
				if random.random() < 0.5:
					action=RobotActions.TURN_RIGHT
				else:
					action=RobotActions.TURN_LEFT

		else :
			if random.random() < 0.5:
				action=RobotActions.TURN_RIGHT
			else:
				action=RobotActions.TURN_LEFT
	elif dir=="South":
		if state.rightWallSensor<=1 and state.leftWallSensor>1 and state.frontWallSensor>1:
			if random.random()<0.5:
				action = RobotActions.FORWARD
			else :
				action=RobotActions.TURN_AND_MOVE_LEFT
		elif state.rightWallSensor>1 and state.leftWallSensor<=1 and state.frontWallSensor>1:
			if random.random()<0.5:
				action = RobotActions.FORWARD
			else:
				action=RobotActions.TURN_AND_MOVE_RIGHT
		elif state.frontWallSensor > 1 :
			action=RobotActions.FORWARD
		elif state.frontWallSensor <= 1 :
			if state.rightWallSensor <= 1 and state.leftWallSensor >1:
				action=RobotActions.TURN_AND_MOVE_LEFT
			elif state.rightWallSensor > 1 and state.leftWallSensor <=1:
				action=RobotActions.TURN_AND_MOVE_RIGHT
			else :
				if random.random() < 0.5:
					action=RobotActions.TURN_LEFT
				else:
					action=RobotActions.TURN_RIGHT

		else :
			if random.random() < 0.5:
				action=RobotActions.TURN_RIGHT
			else:
				action=RobotActions.TURN_LEFT
	'''

class ModelBasedReflexAgent(Agent):
  def __init__(self):
	self.m = [[0 for i in range(20)] for i in range(20)] ;
	self.dust=0
	self.steps=0
	self.dust=0
	self.path=[]
	self.point=[]
	self.parent=[]
  def search(self,pointx,pointy,goal):
	self.point=[pointx,pointy]
	path1=[]
	expset=[]
	localpoint=[]
	i=0
	c=0
	d=0
	path1.append(self.point)
	while 1==1:
		if len(path1) ==0:
			return 0
		localpoint=path1[0]
		del path1[0]
		
		expset.append(localpoint)
		if localpoint[0]+1<20 and self.m[localpoint[0]+1][localpoint[1]]!=0 and self.m[localpoint[0]+1][localpoint[1]]!=3 and [localpoint[0]+1,localpoint[1]] not in path1 and [localpoint[0]+1,localpoint[1]] not in expset:
			path1.append([localpoint[0]+1,localpoint[1]])
			self.path.append([localpoint[0]+1,localpoint[1]])
			self.parent.append(localpoint)
			if self.m[localpoint[0]+1][localpoint[1]]==goal:
				if goal==4:
					if (localpoint[0]+1+1<20 and self.m[localpoint[0]+1+1][localpoint[1]]==0) or self.m[localpoint[0]+1][localpoint[1]+1]==0 or self.m[localpoint[0]+1][localpoint[1]-1]==0:	
						break
				else:
					break
		if localpoint[0]-1>=0 and self.m[localpoint[0]-1][localpoint[1]]!=0 and self.m[localpoint[0]-1][localpoint[1]]!=3 and [localpoint[0]-1,localpoint[1]] not in path1 and [localpoint[0]-1,localpoint[1]] not in expset:
			path1.append([localpoint[0]-1,localpoint[1]])
			self.path.append([localpoint[0]-1,localpoint[1]])
			self.parent.append(localpoint)
			if self.m[localpoint[0]-1][localpoint[1]]==goal:
				if goal==4:
					if (localpoint[0]-1-1 and self.m[localpoint[0]-1-1][localpoint[1]] == 0) or self.m[localpoint[0]-1][localpoint[1]+1]==0 or self.m[localpoint[0]-1][localpoint[1]-1]==0:
						break
				else:
					break
		if localpoint[1]+1<20 and self.m[localpoint[0]][localpoint[1]+1]!=0 and self.m[localpoint[0]][localpoint[1]+1]!=3 and [localpoint[0],localpoint[1]+1] not in path1 and [localpoint[0],localpoint[1]+1] not in expset:
			path1.append([localpoint[0],localpoint[1]+1])
			self.path.append([localpoint[0],localpoint[1]+1])
			self.parent.append(localpoint)
			if self.m[localpoint[0]][localpoint[1]+1]==goal:
				if goal==4:
					if (localpoint[1]+1+1 and self.m[localpoint[0]][localpoint[1]+1+1]==0) or self.m[localpoint[0]-1][localpoint[1]+1]==0 or self.m[localpoint[0]+1][localpoint[1]+1]==0:
						break
				else:
					break
		if localpoint[1]-1>=0 and self.m[localpoint[0]][localpoint[1]-1]!=0 and self.m[localpoint[0]][localpoint[1]-1]!=3 and [localpoint[0],localpoint[1]-1] not in path1 and [localpoint[0],localpoint[1]-1] not in expset:
			path1.append([localpoint[0],localpoint[1]-1])
			self.path.append([localpoint[0],localpoint[1]-1])
			self.parent.append(localpoint)
			if self.m[localpoint[0]][localpoint[1]-1]==goal:
				if goal==4:
					if (localpoint[1]-1-1 and self.m[localpoint[0]][localpoint[1]-1-1]==0) or self.m[localpoint[0]-1][localpoint[1]-1]==0 or self.m[localpoint[0]+1][localpoint[1]-1]==0:
						break
				else:		
					break
				
	#make changes to self.path accordingly#
	self.path.reverse()
	self.parent.reverse()
	i=0
	c=0
	while 1==1:
		if i<=len(self.path)-1 and i<len(self.parent)-1:
			if self.parent[c]!=self.path[i+1]:
				del self.path[i+1]
				del self.parent[i+1]
			else:
				c=i+1
				i+=1
		else:
			break
	self.path.reverse()
	self.parent.reverse()			
	return 1
	#path changes#
	
  def findAction(self,cx,cy,pointx,pointy,direct):
	if direct == 'North':
		if cx-1==pointx:
			action=RobotActions.TURN_AND_MOVE_LEFT
			return action
		if cx+1==pointx:
			action=RobotActions.TURN_AND_MOVE_RIGHT
			return action
		if cy-1==pointy:
			action=RobotActions.TURN_LEFT
			return action
		if cy+1==pointy:
			action=RobotActions.FORWARD
			return action
			
	if direct == 'South':
		if cx-1==pointx:
			action=RobotActions.TURN_AND_MOVE_RIGHT
			return action
		if cx+1==pointx:
			action=RobotActions.TURN_AND_MOVE_LEFT
			return action
		if cy-1==pointy:
			action=RobotActions.FORWARD
			return action
		if cy+1==pointy:
			action=RobotActions.TURN_LEFT
			return action
			
	if direct == 'East':
		if cx-1==pointx:
			action=RobotActions.TURN_LEFT
			return action
		if cx+1==pointx:
			action=RobotActions.FORWARD
			return action
		if cy-1==pointy:
			action=RobotActions.TURN_AND_MOVE_RIGHT
			return action
		if cy+1==pointy:
			action=RobotActions.TURN_AND_MOVE_LEFT
			return action

	if direct == 'West':
		if cx-1==pointx:
			action=RobotActions.FORWARD
			return action
		if cx+1==pointx:
			action=RobotActions.TURN_LEFT
			return action
		if cy-1==pointy:
			action=RobotActions.TURN_AND_MOVE_LEFT
			return action
		if cy+1==pointy:
			action=RobotActions.TURN_AND_MOVE_RIGHT
			return action
  
  def getAction(self, state):
	#print self.m#
	x,y=state.getPosition()
	dir=state.getDirection()
	fd=state.frontDustSensor
	ld=state.leftDustSensor
	rd=state.rightDustSensor
	fw=state.frontWallSensor
	rw=state.rightWallSensor
	bw=state.backWallSensor
	lw=state.leftWallSensor
	
	#reducing dust by 1 if there was dust#
	if self.m[x][y]==2:
		self.dust=self.dust-1
		self.m[x][y]=1
	else:
		self.m[x][y]=1
	
	#reducing dust by 1 if there was dust#
	
	#updating matrix#
	if dir == 'North':
		if fd>=0:
			if fd==1.5:
				if self.m[x][y+2]!=2:
					self.dust+=1
					self.m[x][y+2]=2
				if self.m[x][y+1]!=2:
					self.dust+=1
					self.m[x][y+1]=2
			elif fd==1:
				if self.m[x][y+1]!=2: 
					self.dust+=1
					self.m[x][y+1]=2
				if fw>2 and y+2<20 and self.m[x][y+2]!=1:
					self.m[x][y+2]=4
			elif fd==0.5:
				if self.m[x][y+2]!=2: 
					self.dust+=1
					self.m[x][y+2]=2
				if fw>2 and self.m[x][y+1]!=1:
					self.m[x][y+1]=4
			else:
				if y+2<20 and self.m[x][y+2]!=1 and fw>2:
					self.m[x][y+2]=4
				if y+1<20 and self.m[x][y+1]!=1 and fw>1:
					self.m[x][y+1]=4
		if ld>=0:
			if ld==1.5:
				if self.m[x-2][y]!=2:
					self.dust+=1
					self.m[x-2][y]=2
				if self.m[x-1][y]!=2:
					self.dust+=1
					self.m[x-1][y]=2
			elif ld==1:
				if self.m[x-1][y]!=2:
					self.dust+=1
					self.m[x-1][y]=2
				if lw>2 and x-2 >=0 and self.m[x-2][y]!=1:
					self.m[x-2][y]=4
			elif ld==0.5:
				if self.m[x-2][y]!=2:
					self.dust+=1
					self.m[x-2][y]=2
				if lw>2 and self.m[x-1][y]!=1:
					self.m[x-1][y]=4
			else:
				if x-2>=0 and self.m[x-2][y]!=1 and lw>2:
					self.m[x-2][y]=4
				if x-1>=0 and self.m[x-1][y]!=1 and lw>1:
					self.m[x-1][y]=4		
		if rd>=0:
			if rd==1.5:
				if self.m[x+2][y]!=2:
					self.dust+=1
					self.m[x+2][y]=2
				if self.m[x+1][y]!=2:
					self.dust+=1
					self.m[x+1][y]=2
			elif rd==1:
				if self.m[x+1][y]!=2:
					self.dust+=1
					self.m[x+1][y]=2	
				if rw>2 and x+2<20 and self.m[x+2][y]!=1:
					self.m[x+2][y]=4
			elif rd==0.5 :
				if self.m[x+2][y]!=2:
					self.dust+=1
					self.m[x+2][y]=2
				if rw>2 and self.m[x+1][y]!=1:
					self.m[x+1][y]=4
			else:
				if x+2<20 and self.m[x+2][y]!=1 and rw>2:
					self.m[x+2][y]=4
				if x+1<20 and self.m[x+1][y]!=1 and rw>1:
					self.m[x+1][y]=4
					
		self.m[x][y+fw]=3
		self.m[x-lw][y]=3
		self.m[x+rw][y]=3
		self.m[x][y-bw]=3
		
	elif dir == 'South':
		if fd>=0:
			if fd==1.5:
				if self.m[x][y-2]!=2:
					self.dust+=1
					self.m[x][y-2]=2
				if self.m[x][y-1]!=2:
					self.dust+=1
					self.m[x][y-1]=2
			elif fd==1:
				if self.m[x][y-1]!=2:
					self.dust+=1
					self.m[x][y-1]=2
				if fw>2 and y-2>=0 and self.m[x][y-2]!=1:
					self.m[x][y-2]=4
			elif fd==0.5:
				if self.m[x][y-2]!=2:
					self.dust+=1
					self.m[x][y-2]=2
				if fw>2 and self.m[x][y-1]!=1:
					self.m[x][y-1]=4
			else:
				if y-2>=0 and self.m[x][y-2]!=1 and fw>2:
					self.m[x][y-2]=4
				if self.m[x][y-1]!=1 and y-1>=0 and fw>1:
					self.m[x][y-1]=4
					
		if ld>=0:
			if ld==1.5:
				if self.m[x+2][y]!=2:
					self.dust+=1
					self.m[x+2][y]=2
				if self.m[x+1][y]!=2:
					self.dust+=1
					self.m[x+1][y]=2
			elif ld==1:
				if self.m[x+1][y]!=2:
					self.dust+=1
					self.m[x+1][y]=2
				if lw>2 and x+2<20 and self.m[x+2][y]!=1:
					self.m[x+2][y]=4
			elif ld==0.5 :
				if self.m[x+2][y]!=2:
					self.dust+=1
					self.m[x+2][y]=2
				if lw>2 and self.m[x+1][y]!=1:
					self.m[x+1][y]=4
			else:
				if x+2<20 and self.m[x+2][y]!=1 and lw>2:
					self.m[x+2][y]=4
				if x+1<20 and self.m[x+1][y]!=1 and lw>1:
					self.m[x+1][y]=4					
		if rd>=0:
			if rd==1.5:
				if self.m[x-2][y]!=2:
					self.dust+=1
					self.m[x-2][y]=2
				if self.m[x-1][y]!=2:
					self.dust+=1
					self.m[x-1][y]=2
			elif rd==1:
				if self.m[x-1][y]!=2:
					self.dust+=1
					self.m[x-1][y]=2
				if rw>2 and x-2>=0 and self.m[x-2][y]!=1:
					self.m[x-2][y]=4
			elif rd==0.5:
				if self.m[x-2][y]!=2:
					self.dust+=1
					self.m[x-2][y]=2
				if rw>2 and self.m[x-1][y]!=1:
					self.m[x-1][y]=4
			else:
				if x-2>=0 and self.m[x-2][y]!=1 and rw>2:
					self.m[x-2][y]=4
				if x-1>=0 and self.m[x-1][y]!=1 and rw>1:
					self.m[x-1][y]=4
					
		self.m[x][y-fw]=3
		self.m[x+lw][y]=3
		self.m[x-rw][y]=3
		self.m[x][y+bw]=3
		
	elif dir == 'East':
		if fd>=0:
			if fd==1.5:
				if self.m[x+2][y]!=2:
					self.dust+=1
					self.m[x+2][y]=2
				if self.m[x+1][y]!=2:
					self.dust+=1
					self.m[x+1][y]=2
			elif fd==1:
				if self.m[x+1][y]!=2:
					self.dust+=1
					self.m[x+1][y]=2
				if fw>2 and x+2<20 and self.m[x+2][y]!=1:
					self.m[x+2][y]=4
			elif fd==0.5:
				if self.m[x+2][y]!=2:
					self.dust+=1
					self.m[x+2][y]=2
				if fw>2 and self.m[x+1][y]!=1:
					self.m[x+1][y]=4
			else:
				if x+2<20 and self.m[x+2][y]!=1 and fw>2:
					self.m[x+2][y]=4
				if x+1<20 and self.m[x+1][y]!=1 and fw>1:
					self.m[x+1][y]=4
					
		if ld>=0:
			if ld==1.5:
				if self.m[x][y+2]!=2:
					self.dust+=1
					self.m[x][y+2]=2
				if self.m[x][y+1]!=2:
					self.dust+=1
					self.m[x][y+1]=2
			elif ld==1:
				if self.m[x][y+1]!=2:
					self.dust+=1
					self.m[x][y+1]=2
				if lw>2 and y+2<20 and self.m[x][y+2]!=1:
					self.m[x][y+2]=4
			elif ld==0.5:
				if self.m[x][y+2]!=2:
					self.dust+=1
					self.m[x][y+2]=2
				if lw>2 and self.m[x][y+1]!=1:
					self.m[x][y+1]=4
			else:
				if y+2<20 and self.m[x][y+2]!=1 and lw>2:
					self.m[x][y+2]=4
				if y+1<20 and self.m[x][y+1]!=1 and lw>1:
					self.m[x][y+1]=4
		if rd>=0:
			if rd==1.5:
				if self.m[x][y-2]!=2:
					self.dust+=1
					self.m[x][y-2]=2
				if self.m[x][y-1]!=2:
					self.dust+=1
					self.m[x][y-1]=2
			elif rd==1:
				if self.m[x][y-1]!=2:
					self.dust+=1
					self.m[x][y-1]=2
				if rw>2 and y-2>=0 and self.m[x][y-2]!=1:
					self.m[x][y-2]=4
			elif rd==0.5:
				if self.m[x][y-2]!=2:
					self.dust+=1
					self.m[x][y-2]=2
				if rw>2 and self.m[x][y-1]!=1:
					self.m[x][y-1]=4
			else:
				if y-2>=0 and self.m[x][y-2]!=1 and rw>2:
					self.m[x][y-2]=4
				if y-1>=0 and self.m[x][y-1]!=1 and rw>1:
					self.m[x][y-1]=4
					
		self.m[x+fw][y]=3
		self.m[x][y+lw]=3
		self.m[x][y-rw]=3
		self.m[x-bw][y]=3
	else:
		if fd>=0:
			if fd==1.5:
				if self.m[x-2][y]!=2:
					self.dust+=1
					self.m[x-2][y]=2
				if self.m[x-1][y]!=2:
					self.m[x-1][y]=2
					self.dust+=1
			elif fd==1:
				if self.m[x-1][y]!=2:
					self.m[x-1][y]=2
					self.dust+=1
				if fw>2 and x-2>=0 and self.m[x-2][y]!=1:
					self.m[x-2][y]=4
			elif fd==0.5:
				if self.m[x-2][y]!=2:
					self.dust+=1
					self.m[x-2][y]=2
				if fw>2 and self.m[x-1][y]!=1:
					self.m[x-1][y]=4
			else:
				if x-2>=0 and self.m[x-2][y]!=1 and fw>2:
					self.m[x-2][y]=4
				if x-1>=0 and self.m[x-1][y]!=1 and fw>1:
					self.m[x-1][y]=4
					
		if ld>=0:
			if ld==1.5:
				if self.m[x][y-2]!=2:
					self.m[x][y-2]=2
					self.dust+=1
				if self.m[x][y-1]!=2:
					self.m[x][y-1]=2
					self.dust+=1
			elif ld==1:
				if self.m[x][y-1]!=2:
					self.m[x][y-1]=2
					self.dust+=1
				if lw>2 and y-2>=0 and self.m[x][y-2]!=1:
					self.m[x][y-2]=4
			elif ld==0.5:
				if self.m[x][y-2]!=2:
					self.m[x][y-2]=2
					self.dust+=1
				if lw>2 and self.m[x][y-1]!=1:
					self.m[x][y-1]=4
			else:
				if y-2>=0 and self.m[x][y-2]!=1 and lw>2:
					self.m[x][y-2]=4
				if y-1>=0 and self.m[x][y-1]!=1 and lw>1:
					self.m[x][y-1]=4
					
		if rd>=0:
			if rd==1.5:
				if self.m[x][y+2]!=2:
					self.m[x][y+2]=2
					self.dust+=1
				if self.m[x][y+1]!=2:
					self.m[x][y+1]=2
					self.dust+=1
			elif rd==1:
				if self.m[x][y+1]!=2:
					self.m[x][y+1]=2
					self.dust+=1
				if rw>2 and y+2<20 and self.m[x][y+2]!=1:
					self.m[x][y+2]=4
			elif rd==0.5:
				if self.m[x][y+2]!=2:
					self.m[x][y+2]=2
					self.dust+=1
				if rw>2 and self.m[x][y+1]!=1:
					self.m[x][y+1]=4
			else:
				if y+2<20 and self.m[x][y+2]!=1 and rw>2:
					self.m[x][y+2]=4
				if y+1<20 and self.m[x][y+1]!=1 and rw>1:
					self.m[x][y+1]=4
					
		self.m[x-fw][y]=3
		self.m[x][y-lw]=3
		self.m[x][y+rw]=3
		self.m[x+bw][y]=3
	#updating matrix#
	
	#actions using dust sensors#	
	if fd > 1:
		action=RobotActions.FORWARD
		return action
	elif ld>1:
		action=RobotActions.TURN_AND_MOVE_LEFT
		return action
	elif rd>1:
		action=RobotActions.TURN_AND_MOVE_RIGHT
		return action
	elif fd==1:
		action=RobotActions.FORWARD
		return action
	elif ld==1:
		action=RobotActions.TURN_AND_MOVE_LEFT
		return action
	elif rd==1:
		action=RobotActions.TURN_AND_MOVE_RIGHT
		return action
	elif fd==0.5 and fw>2:
		action=RobotActions.FORWARD
		return action
	elif ld==0.5 and lw>2:
		action=RobotActions.TURN_AND_MOVE_LEFT
		return action
	else:
		if rd==0.5 and rw>2:
			action=RobotActions.TURN_AND_MOVE_RIGHT
			return action
	
		
	if fw<=2 and len(self.path)==0:
		if fw==2 and lw==1 and rw>1:
			if dir == 'North':
				if self.m[x+1][y]==4:
					action=RobotActions.TURN_AND_MOVE_RIGHT
					return action
				else:
					action=RobotActions.FORWARD
					return action
			if dir=='South':
				if self.m[x-1][y]==4:
					action=RobotActions.TURN_AND_MOVE_RIGHT
					return action
				else:
					action=RobotActions.FORWARD
					return action
			if dir == 'East':
				if self.m[x][y-1]==4:
					action=RobotActions.TURN_AND_MOVE_RIGHT
					return action
				else:
					action=RobotActions.FORWARD
					return action
			if dir == 'West':
				if self.m[x][y+1]==4:
					action=RobotActions.TURN_AND_MOVE_RIGHT
					return action
				else:
					action=RobotActions.FORWARD
					return action			
				
		if fw==2 and rw==1 and lw>1:
			if dir == 'North':
				if self.m[x-1][y]==4:
					action=RobotActions.TURN_AND_MOVE_LEFT
					return action
				else:
					action=RobotActions.FORWARD
					return action
			if dir=='South':
				if self.m[x+1][y]==4:
					action=RobotActions.TURN_AND_MOVE_LEFT
					return action
				else:
					action=RobotActions.FORWARD
					self.steps+=1
					return action
			if dir == 'East':
				if self.m[x][y+1]==4:
					action=RobotActions.TURN_AND_MOVE_LEFT
					return action
				else:
					action=RobotActions.FORWARD
					return action
			if dir == 'West':
				if self.m[x][y-1]==4:
					action=RobotActions.TURN_AND_MOVE_LEFT
					return action
				else:
					action=RobotActions.FORWARD
					self.steps+=1
					return action			
		if fw==1 and rw==1 and lw==1:
			action=RobotActions.TURN_LEFT
			return action
		if fw==1 and lw==1 and rw>1:
			action=RobotActions.TURN_AND_MOVE_RIGHT
			return action
		if fw==1 and rw==1 and lw>1:
			action=RobotActions.TURN_AND_MOVE_LEFT
			return action
		if fw==1:
			if random.random() < 0.5:
				action=RobotActions.TURN_AND_MOVE_RIGHT
				return action
			else:
				action=RobotActions.TURN_AND_MOVE_LEFT
				return action
		if fw==2:
			if random.random() < 0.5:
				action=RobotActions.FORWARD
				return action
			else:
				action=RobotActions.TURN_AND_MOVE_LEFT
				return action

	#movements based on the stored data#
	if self.dust>=1:
		if len(self.path)==0:
			del self.path[:]
			del self.parent[:]			
			self.search(x,y,2)
			self.point=self.path[0]
			action=self.findAction(x,y,self.point[0],self.point[1],dir)
			return action
		else:
			self.point=self.path[0]
			if x== self.point[0] and y == self.point[1]:
				del self.path[0]
				del self.parent[0]
			if len(self.path)>0:
				self.point==self.parent[0]
				if x == self.point[0] and y == self.point[1]:
					action=self.findAction(x,y,self.point[0],self.point[1],dir)
					return action

				else:
					del self.path[:]
					del self.parent[:]
					self.search(x,y,2)
					self.point=self.path[0]
					action=self.findAction(x,y,self.point[0],self.point[1],dir)
					return action
			else:
					del self.path[:]
					del self.parent[:]
					self.search(x,y,2)
					self.point=self.path[0]
					action=self.findAction(x,y,self.point[0],self.point[1],dir)
					return action
		
	else:
		if len(self.path)==0:
			del self.path[:]
			del self.parent[:]
			self.search(x,y,4)
			self.point=self.path[0]
			action=self.findAction(x,y,self.point[0],self.point[1],dir)
			return action
		else:
			self.point=self.path[0]
			if x== self.point[0] and y == self.point[1]:
				del self.path[0]
				del self.parent[0]
			if len(self.path)>0:
				self.point==self.parent[0]
				if x == self.point[0] and y == self.point[1]:
					action=self.findAction(x,y,self.point[0],self.point[1],dir)
					return action
				else:
					del self.path[:]
					del self.parent[:]
					self.search(x,y,4)
					self.point=self.path[0]
					action=self.findAction(x,y,self.point[0],self.point[1],dir)
					return action

			else:
				del self.path[:]
				del self.parent[:]
				self.search(x,y,4)
				self.point=self.path[0]
				action=self.findAction(x,y,self.point[0],self.point[1],dir)
				return action

	#movements based on the stored data#			
				
	
		

class UtilityBasedAgent(Agent):
  def __init__(self):
	self.m = [[0 for i in range(20)] for i in range(20)] ;
	self.dust=0
	self.steps=0
	self.dust=0
	self.path=[]
	self.point=[]
	self.parent=[]
  def search(self,pointx,pointy,goal):
	self.point=[pointx,pointy]
	path1=[]
	expset=[]
	localpoint=[]
	i=0
	c=0
	d=0
	path1.append(self.point)
	while 1==1:
		if len(path1) ==0:
			return 0
		localpoint=path1[0]
		del path1[0]
		
		expset.append(localpoint)
		if localpoint[0]+1<20 and self.m[localpoint[0]+1][localpoint[1]]!=0 and self.m[localpoint[0]+1][localpoint[1]]!=3 and [localpoint[0]+1,localpoint[1]] not in path1 and [localpoint[0]+1,localpoint[1]] not in expset:
			path1.append([localpoint[0]+1,localpoint[1]])
			self.path.append([localpoint[0]+1,localpoint[1]])
			self.parent.append(localpoint)
			if self.m[localpoint[0]+1][localpoint[1]]==goal:
				if goal==4:
					if (localpoint[0]+1+1<20 and self.m[localpoint[0]+1+1][localpoint[1]]==0) or self.m[localpoint[0]+1][localpoint[1]+1]==0 or self.m[localpoint[0]+1][localpoint[1]-1]==0:	
						break
				else:
					break
		if localpoint[0]-1>=0 and self.m[localpoint[0]-1][localpoint[1]]!=0 and self.m[localpoint[0]-1][localpoint[1]]!=3 and [localpoint[0]-1,localpoint[1]] not in path1 and [localpoint[0]-1,localpoint[1]] not in expset:
			path1.append([localpoint[0]-1,localpoint[1]])
			self.path.append([localpoint[0]-1,localpoint[1]])
			self.parent.append(localpoint)
			if self.m[localpoint[0]-1][localpoint[1]]==goal:
				if goal==4:
					if (localpoint[0]-1-1 and self.m[localpoint[0]-1-1][localpoint[1]] == 0) or self.m[localpoint[0]-1][localpoint[1]+1]==0 or self.m[localpoint[0]-1][localpoint[1]-1]==0:
						break
				else:
					break
		if localpoint[1]+1<20 and self.m[localpoint[0]][localpoint[1]+1]!=0 and self.m[localpoint[0]][localpoint[1]+1]!=3 and [localpoint[0],localpoint[1]+1] not in path1 and [localpoint[0],localpoint[1]+1] not in expset:
			path1.append([localpoint[0],localpoint[1]+1])
			self.path.append([localpoint[0],localpoint[1]+1])
			self.parent.append(localpoint)
			if self.m[localpoint[0]][localpoint[1]+1]==goal:
				if goal==4:
					if (localpoint[1]+1+1 and self.m[localpoint[0]][localpoint[1]+1+1]==0) or self.m[localpoint[0]-1][localpoint[1]+1]==0 or self.m[localpoint[0]+1][localpoint[1]+1]==0:
						break
				else:
					break
		if localpoint[1]-1>=0 and self.m[localpoint[0]][localpoint[1]-1]!=0 and self.m[localpoint[0]][localpoint[1]-1]!=3 and [localpoint[0],localpoint[1]-1] not in path1 and [localpoint[0],localpoint[1]-1] not in expset:
			path1.append([localpoint[0],localpoint[1]-1])
			self.path.append([localpoint[0],localpoint[1]-1])
			self.parent.append(localpoint)
			if self.m[localpoint[0]][localpoint[1]-1]==goal:
				if goal==4:
					if (localpoint[1]-1-1 and self.m[localpoint[0]][localpoint[1]-1-1]==0) or self.m[localpoint[0]-1][localpoint[1]-1]==0 or self.m[localpoint[0]+1][localpoint[1]-1]==0:
						break
				else:		
					break
				
	#make changes to self.path accordingly#
	self.path.reverse()
	self.parent.reverse()
	i=0
	c=0
	while 1==1:
		if i<=len(self.path)-1 and i<len(self.parent)-1:
			if self.parent[c]!=self.path[i+1]:
				del self.path[i+1]
				del self.parent[i+1]
			else:
				c=i+1
				i+=1
		else:
			break
	self.path.reverse()
	self.parent.reverse()			
	return 1
	#path changes#
	
  def findAction(self,cx,cy,pointx,pointy,direct):
	if direct == 'North':
		if cx-1==pointx:
			action=RobotActions.TURN_AND_MOVE_LEFT
			return action
		if cx+1==pointx:
			action=RobotActions.TURN_AND_MOVE_RIGHT
			return action
		if cy-1==pointy:
			action=RobotActions.TURN_LEFT
			return action
		if cy+1==pointy:
			action=RobotActions.FORWARD
			return action
			
	if direct == 'South':
		if cx-1==pointx:
			action=RobotActions.TURN_AND_MOVE_RIGHT
			return action
		if cx+1==pointx:
			action=RobotActions.TURN_AND_MOVE_LEFT
			return action
		if cy-1==pointy:
			action=RobotActions.FORWARD
			return action
		if cy+1==pointy:
			action=RobotActions.TURN_LEFT
			return action
			
	if direct == 'East':
		if cx-1==pointx:
			action=RobotActions.TURN_LEFT
			return action
		if cx+1==pointx:
			action=RobotActions.FORWARD
			return action
		if cy-1==pointy:
			action=RobotActions.TURN_AND_MOVE_RIGHT
			return action
		if cy+1==pointy:
			action=RobotActions.TURN_AND_MOVE_LEFT
			return action

	if direct == 'West':
		if cx-1==pointx:
			action=RobotActions.FORWARD
			return action
		if cx+1==pointx:
			action=RobotActions.TURN_LEFT
			return action
		if cy-1==pointy:
			action=RobotActions.TURN_AND_MOVE_LEFT
			return action
		if cy+1==pointy:
			action=RobotActions.TURN_AND_MOVE_RIGHT
			return action
  
  def getAction(self, state):
	#print self.m#

	if state.dustUtility==5 or state.dustUtility==2:
		action=RobotActions.DO_NOTHING
		return action
	x,y=state.getPosition()
	dir=state.getDirection()
	fd=state.frontDustSensor
	ld=state.leftDustSensor
	rd=state.rightDustSensor
	fw=state.frontWallSensor
	rw=state.rightWallSensor
	bw=state.backWallSensor
	lw=state.leftWallSensor
	
	#reducing dust by 1 if there was dust#
	if self.m[x][y]==2:
		self.dust=self.dust-1
		self.m[x][y]=1
		self.steps=0
	else:
		self.m[x][y]=1
	
	#reducing dust by 1 if there was dust#
	
	#updating matrix#
	if dir == 'North':
		if fd>=0:
			if fd==1.5:
				if self.m[x][y+2]!=2:
					self.dust+=1
					self.m[x][y+2]=2
				if self.m[x][y+1]!=2:
					self.dust+=1
					self.m[x][y+1]=2
			elif fd==1:
				if self.m[x][y+1]!=2: 
					self.dust+=1
					self.m[x][y+1]=2
				if fw>2 and y+2<20 and self.m[x][y+2]!=1:
					self.m[x][y+2]=4
			elif fd==0.5:
				if self.m[x][y+2]!=2: 
					self.dust+=1
					self.m[x][y+2]=2
				if fw>2 and self.m[x][y+1]!=1:
					self.m[x][y+1]=4
			else:
				if y+2<20 and self.m[x][y+2]!=1 and fw>2:
					self.m[x][y+2]=4
				if y+1<20 and self.m[x][y+1]!=1 and fw>1:
					self.m[x][y+1]=4
		if ld>=0:
			if ld==1.5:
				if self.m[x-2][y]!=2:
					self.dust+=1
					self.m[x-2][y]=2
				if self.m[x-1][y]!=2:
					self.dust+=1
					self.m[x-1][y]=2
			elif ld==1:
				if self.m[x-1][y]!=2:
					self.dust+=1
					self.m[x-1][y]=2
				if lw>2 and x-2 >=0 and self.m[x-2][y]!=1:
					self.m[x-2][y]=4
			elif ld==0.5:
				if self.m[x-2][y]!=2:
					self.dust+=1
					self.m[x-2][y]=2
				if lw>2 and self.m[x-1][y]!=1:
					self.m[x-1][y]=4
			else:
				if x-2>=0 and self.m[x-2][y]!=1 and lw>2:
					self.m[x-2][y]=4
				if x-1>=0 and self.m[x-1][y]!=1 and lw>1:
					self.m[x-1][y]=4		
		if rd>=0:
			if rd==1.5:
				if self.m[x+2][y]!=2:
					self.dust+=1
					self.m[x+2][y]=2
				if self.m[x+1][y]!=2:
					self.dust+=1
					self.m[x+1][y]=2
			elif rd==1:
				if self.m[x+1][y]!=2:
					self.dust+=1
					self.m[x+1][y]=2	
				if rw>2 and x+2<20 and self.m[x+2][y]!=1:
					self.m[x+2][y]=4
			elif rd==0.5 :
				if self.m[x+2][y]!=2:
					self.dust+=1
					self.m[x+2][y]=2
				if rw>2 and self.m[x+1][y]!=1:
					self.m[x+1][y]=4
			else:
				if x+2<20 and self.m[x+2][y]!=1 and rw>2:
					self.m[x+2][y]=4
				if x+1<20 and self.m[x+1][y]!=1 and rw>1:
					self.m[x+1][y]=4
					
		self.m[x][y+fw]=3
		self.m[x-lw][y]=3
		self.m[x+rw][y]=3
		self.m[x][y-bw]=3
		
	elif dir == 'South':
		if fd>=0:
			if fd==1.5:
				if self.m[x][y-2]!=2:
					self.dust+=1
					self.m[x][y-2]=2
				if self.m[x][y-1]!=2:
					self.dust+=1
					self.m[x][y-1]=2
			elif fd==1:
				if self.m[x][y-1]!=2:
					self.dust+=1
					self.m[x][y-1]=2
				if fw>2 and y-2>=0 and self.m[x][y-2]!=1:
					self.m[x][y-2]=4
			elif fd==0.5:
				if self.m[x][y-2]!=2:
					self.dust+=1
					self.m[x][y-2]=2
				if fw>2 and self.m[x][y-1]!=1:
					self.m[x][y-1]=4
			else:
				if y-2>=0 and self.m[x][y-2]!=1 and fw>2:
					self.m[x][y-2]=4
				if self.m[x][y-1]!=1 and y-1>=0 and fw>1:
					self.m[x][y-1]=4
					
		if ld>=0:
			if ld==1.5:
				if self.m[x+2][y]!=2:
					self.dust+=1
					self.m[x+2][y]=2
				if self.m[x+1][y]!=2:
					self.dust+=1
					self.m[x+1][y]=2
			elif ld==1:
				if self.m[x+1][y]!=2:
					self.dust+=1
					self.m[x+1][y]=2
				if lw>2 and x+2<20 and self.m[x+2][y]!=1:
					self.m[x+2][y]=4
			elif ld==0.5 :
				if self.m[x+2][y]!=2:
					self.dust+=1
					self.m[x+2][y]=2
				if lw>2 and self.m[x+1][y]!=1:
					self.m[x+1][y]=4
			else:
				if x+2<20 and self.m[x+2][y]!=1 and lw>2:
					self.m[x+2][y]=4
				if x+1<20 and self.m[x+1][y]!=1 and lw>1:
					self.m[x+1][y]=4					
		if rd>=0:
			if rd==1.5:
				if self.m[x-2][y]!=2:
					self.dust+=1
					self.m[x-2][y]=2
				if self.m[x-1][y]!=2:
					self.dust+=1
					self.m[x-1][y]=2
			elif rd==1:
				if self.m[x-1][y]!=2:
					self.dust+=1
					self.m[x-1][y]=2
				if rw>2 and x-2>=0 and self.m[x-2][y]!=1:
					self.m[x-2][y]=4
			elif rd==0.5:
				if self.m[x-2][y]!=2:
					self.dust+=1
					self.m[x-2][y]=2
				if rw>2 and self.m[x-1][y]!=1:
					self.m[x-1][y]=4
			else:
				if x-2>=0 and self.m[x-2][y]!=1 and rw>2:
					self.m[x-2][y]=4
				if x-1>=0 and self.m[x-1][y]!=1 and rw>1:
					self.m[x-1][y]=4
					
		self.m[x][y-fw]=3
		self.m[x+lw][y]=3
		self.m[x-rw][y]=3
		self.m[x][y+bw]=3
		
	elif dir == 'East':
		if fd>=0:
			if fd==1.5:
				if self.m[x+2][y]!=2:
					self.dust+=1
					self.m[x+2][y]=2
				if self.m[x+1][y]!=2:
					self.dust+=1
					self.m[x+1][y]=2
			elif fd==1:
				if self.m[x+1][y]!=2:
					self.dust+=1
					self.m[x+1][y]=2
				if fw>2 and x+2<20 and self.m[x+2][y]!=1:
					self.m[x+2][y]=4
			elif fd==0.5:
				if self.m[x+2][y]!=2:
					self.dust+=1
					self.m[x+2][y]=2
				if fw>2 and self.m[x+1][y]!=1:
					self.m[x+1][y]=4
			else:
				if x+2<20 and self.m[x+2][y]!=1 and fw>2:
					self.m[x+2][y]=4
				if x+1<20 and self.m[x+1][y]!=1 and fw>1:
					self.m[x+1][y]=4
					
		if ld>=0:
			if ld==1.5:
				if self.m[x][y+2]!=2:
					self.dust+=1
					self.m[x][y+2]=2
				if self.m[x][y+1]!=2:
					self.dust+=1
					self.m[x][y+1]=2
			elif ld==1:
				if self.m[x][y+1]!=2:
					self.dust+=1
					self.m[x][y+1]=2
				if lw>2 and y+2<20 and self.m[x][y+2]!=1:
					self.m[x][y+2]=4
			elif ld==0.5:
				if self.m[x][y+2]!=2:
					self.dust+=1
					self.m[x][y+2]=2
				if lw>2 and self.m[x][y+1]!=1:
					self.m[x][y+1]=4
			else:
				if y+2<20 and self.m[x][y+2]!=1 and lw>2:
					self.m[x][y+2]=4
				if y+1<20 and self.m[x][y+1]!=1 and lw>1:
					self.m[x][y+1]=4
		if rd>=0:
			if rd==1.5:
				if self.m[x][y-2]!=2:
					self.dust+=1
					self.m[x][y-2]=2
				if self.m[x][y-1]!=2:
					self.dust+=1
					self.m[x][y-1]=2
			elif rd==1:
				if self.m[x][y-1]!=2:
					self.dust+=1
					self.m[x][y-1]=2
				if rw>2 and y-2>=0 and self.m[x][y-2]!=1:
					self.m[x][y-2]=4
			elif rd==0.5:
				if self.m[x][y-2]!=2:
					self.dust+=1
					self.m[x][y-2]=2
				if rw>2 and self.m[x][y-1]!=1:
					self.m[x][y-1]=4
			else:
				if y-2>=0 and self.m[x][y-2]!=1 and rw>2:
					self.m[x][y-2]=4
				if y-1>=0 and self.m[x][y-1]!=1 and rw>1:
					self.m[x][y-1]=4
					
		self.m[x+fw][y]=3
		self.m[x][y+lw]=3
		self.m[x][y-rw]=3
		self.m[x-bw][y]=3
	else:
		if fd>=0:
			if fd==1.5:
				if self.m[x-2][y]!=2:
					self.dust+=1
					self.m[x-2][y]=2
				if self.m[x-1][y]!=2:
					self.m[x-1][y]=2
					self.dust+=1
			elif fd==1:
				if self.m[x-1][y]!=2:
					self.m[x-1][y]=2
					self.dust+=1
				if fw>2 and x-2>=0 and self.m[x-2][y]!=1:
					self.m[x-2][y]=4
			elif fd==0.5:
				if self.m[x-2][y]!=2:
					self.dust+=1
					self.m[x-2][y]=2
				if fw>2 and self.m[x-1][y]!=1:
					self.m[x-1][y]=4
			else:
				if x-2>=0 and self.m[x-2][y]!=1 and fw>2:
					self.m[x-2][y]=4
				if x-1>=0 and self.m[x-1][y]!=1 and fw>1:
					self.m[x-1][y]=4
					
		if ld>=0:
			if ld==1.5:
				if self.m[x][y-2]!=2:
					self.m[x][y-2]=2
					self.dust+=1
				if self.m[x][y-1]!=2:
					self.m[x][y-1]=2
					self.dust+=1
			elif ld==1:
				if self.m[x][y-1]!=2:
					self.m[x][y-1]=2
					self.dust+=1
				if lw>2 and y-2>=0 and self.m[x][y-2]!=1:
					self.m[x][y-2]=4
			elif ld==0.5:
				if self.m[x][y-2]!=2:
					self.m[x][y-2]=2
					self.dust+=1
				if lw>2 and self.m[x][y-1]!=1:
					self.m[x][y-1]=4
			else:
				if y-2>=0 and self.m[x][y-2]!=1 and lw>2:
					self.m[x][y-2]=4
				if y-1>=0 and self.m[x][y-1]!=1 and lw>1:
					self.m[x][y-1]=4
					
		if rd>=0:
			if rd==1.5:
				if self.m[x][y+2]!=2:
					self.m[x][y+2]=2
					self.dust+=1
				if self.m[x][y+1]!=2:
					self.m[x][y+1]=2
					self.dust+=1
			elif rd==1:
				if self.m[x][y+1]!=2:
					self.m[x][y+1]=2
					self.dust+=1
				if rw>2 and y+2<20 and self.m[x][y+2]!=1:
					self.m[x][y+2]=4
			elif rd==0.5:
				if self.m[x][y+2]!=2:
					self.m[x][y+2]=2
					self.dust+=1
				if rw>2 and self.m[x][y+1]!=1:
					self.m[x][y+1]=4
			else:
				if y+2<20 and self.m[x][y+2]!=1 and rw>2:
					self.m[x][y+2]=4
				if y+1<20 and self.m[x][y+1]!=1 and rw>1:
					self.m[x][y+1]=4
					
		self.m[x-fw][y]=3
		self.m[x][y-lw]=3
		self.m[x][y+rw]=3
		self.m[x+bw][y]=3
	#updating matrix#
	
	#actions using dust sensors#	
	if fd > 1:
		action=RobotActions.FORWARD
		return action
	elif ld>1:
		action=RobotActions.TURN_AND_MOVE_LEFT
		return action
	elif rd>1:
		action=RobotActions.TURN_AND_MOVE_RIGHT
		return action
	elif fd==1:
		action=RobotActions.FORWARD
		return action
	elif ld==1:
		action=RobotActions.TURN_AND_MOVE_LEFT
		return action
	elif rd==1:
		action=RobotActions.TURN_AND_MOVE_RIGHT
		return action
	elif fd==0.5 and fw>2:
		action=RobotActions.FORWARD
		return action
	elif ld==0.5 and lw>2:
		action=RobotActions.TURN_AND_MOVE_LEFT
		return action
	elif rd==0.5 and rw>2:
		action=RobotActions.TURN_AND_MOVE_RIGHT
		return action
	elif state.dustUtility==2:
		action=RobotActions.DO_NOTHING
		return action
	elif fw<=2 and len(self.path)==0:
		if fw==2 and lw==1 and rw>1:
			if dir == 'North':
				if self.m[x+1][y]==4:
					action=RobotActions.TURN_AND_MOVE_RIGHT
					self.steps+=1
					return action
				else:
					action=RobotActions.FORWARD
					self.steps+=1
					return action
			if dir=='South':
				if self.m[x-1][y]==4:
					action=RobotActions.TURN_AND_MOVE_RIGHT
					self.steps+=1
					return action
				else:
					action=RobotActions.FORWARD
					self.steps+=1
					return action
			if dir == 'East':
				if self.m[x][y-1]==4:
					action=RobotActions.TURN_AND_MOVE_RIGHT
					self.steps+=1
					return action
				else:
					action=RobotActions.FORWARD
					self.steps+=1
					return action
			if dir == 'West':
				if self.m[x][y+1]==4:
					action=RobotActions.TURN_AND_MOVE_RIGHT
					self.steps+=1
					return action
				else:
					action=RobotActions.FORWARD
					self.steps+=1
					return action			
				
		if fw==2 and rw==1 and lw>1:
			if dir == 'North':
				if self.m[x-1][y]==4:
					action=RobotActions.TURN_AND_MOVE_LEFT
					self.steps+=1
					return action
				else:
					action=RobotActions.FORWARD
					self.steps+=1
					return action
			if dir=='South':
				if self.m[x+1][y]==4:
					action=RobotActions.TURN_AND_MOVE_LEFT
					self.steps+=1
					return action
				else:
					action=RobotActions.FORWARD
					self.steps+=1
					return action
			if dir == 'East':
				if self.m[x][y+1]==4:
					action=RobotActions.TURN_AND_MOVE_LEFT
					self.steps+=1
					return action
				else:
					action=RobotActions.FORWARD
					self.steps+=1
					return action
			if dir == 'West':
				if self.m[x][y-1]==4:
					action=RobotActions.TURN_AND_MOVE_LEFT
					self.steps+=1
					return action
				else:
					action=RobotActions.FORWARD
					self.steps+=1
					return action			
		if fw==1 and rw==1 and lw==1:
			action=RobotActions.TURN_LEFT
			self.steps+=1
			return action
		if fw==1 and lw==1 and rw>1:
			action=RobotActions.TURN_AND_MOVE_RIGHT
			self.steps+=1
			return action
		if fw==1 and rw==1 and lw>1:
			action=RobotActions.TURN_AND_MOVE_LEFT
			self.steps+=1
			return action
		if fw==1:
			if random.random() < 0.5:
				action=RobotActions.TURN_AND_MOVE_RIGHT
				self.steps+=1
				return action
			else:
				action=RobotActions.TURN_AND_MOVE_LEFT
				self.steps+=1
				return action
		if fw==2:
			if random.random() < 0.5:
				action=RobotActions.FORWARD
				self.steps+=1
				return action
			else:
				action=RobotActions.TURN_AND_MOVE_LEFT
				self.steps+=1
				return action
			
	else:
		if 1==1:
			if self.dust>=1:
				if len(self.path)==0:
					del self.path[:]
					del self.parent[:]			
					self.search(x,y,2)
					self.point=self.path[0]
					action=self.findAction(x,y,self.point[0],self.point[1],dir)
					self.steps+=1
					return action
				else:
					self.point=self.path[0]
					if x== self.point[0] and y == self.point[1]:
						del self.path[0]
						del self.parent[0]
					if len(self.path)>0:
						self.point==self.parent[0]
						if x == self.point[0] and y == self.point[1]:
							action=self.findAction(x,y,self.point[0],self.point[1],dir)
							self.steps+=1
							return action

						else:
							del self.path[:]
							del self.parent[:]
							self.search(x,y,2)
							self.point=self.path[0]
							action=self.findAction(x,y,self.point[0],self.point[1],dir)
							self.steps+=1
							return action
					else:
							del self.path[:]
							del self.parent[:]
							self.search(x,y,2)
							self.point=self.path[0]
							action=self.findAction(x,y,self.point[0],self.point[1],dir)
							self.steps+=1
							return action
			
			else:
				if len(self.path)==0:
					del self.path[:]
					del self.parent[:]
					self.search(x,y,4)
					self.point=self.path[0]
					action=self.findAction(x,y,self.point[0],self.point[1],dir)
					self.steps+=1
					return action
				else:
					self.point=self.path[0]
					if x== self.point[0] and y == self.point[1]:
						del self.path[0]
						del self.parent[0]
					if len(self.path)>0:
						self.point==self.parent[0]
						if x == self.point[0] and y == self.point[1]:
							action=self.findAction(x,y,self.point[0],self.point[1],dir)
							self.steps+=1
							return action
						else:
							del self.path[:]
							del self.parent[:]
							self.search(x,y,4)
							self.point=self.path[0]
							action=self.findAction(x,y,self.point[0],self.point[1],dir)
							self.steps+=1
							return action

					else:
						del self.path[:]
						del self.parent[:]
						self.search(x,y,4)
						self.point=self.path[0]
						action=self.findAction(x,y,self.point[0],self.point[1],dir)
						self.steps+=1
						return action
		else:
			action=RobotActions.DO_NOTHING

		#movements based on the stored data#	


