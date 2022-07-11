import pygame
import sys
import time
import random
clock=pygame.time.Clock()
pygame.init() 
width, height = 600,600
ROW,COL = 3,3
L=[]
L2=[]
LL=[]
Tabu=[]
game_over= False
temp1=0
temp2=0

screen= pygame.display.set_mode((width,height))
int1= random.randint(0, 8)
L.append(int1)
int2 = random.randint(0, 8)
while int2 in L:
	int2 = random.randint(0, 8)
L.append(int2)
int3 = random.randint(0, 8)
while int3 in L:
	int3 = random.randint(0, 8)
L.append(int3)
int4 = random.randint(0, 8)
while int4 in L:
	int4 = random.randint(0, 8)
L.append(int4)
int5 = random.randint(0, 8)
while int5 in L:
	int5 = random.randint(0, 8)
L.append(int5)
int6 = random.randint(0, 8)
while int6 in L:
	int6 = random.randint(0, 8)
L.append(int6)
int7 = random.randint(0, 8)
while int7 in L:
	int7 = random.randint(0, 8)
L.append(int7)
int8 = random.randint(0, 8)
while int8 in L:
	int8 = random.randint(0, 8)
L.append(int8)
int9 = random.randint(0, 8)
while int9 in L:
	int9 = random.randint(0, 8)
L.append(int9)

cost=0
for i in range(len(L)-1):
	if int(L[i+1])-int(L[i])!=1:
		LL.append(L[i])
		cost=cost+1

def calcost(Liste):
	cost=0 
	for i in range(len(Liste)-1):
		if int(Liste[i+1])-int(Liste[i])!=1:
			cost=cost+1
	if int(Liste[8])-int(Liste[7])!=1:
		cost=cost+1
	return cost

class board:
	def __init__(self): 
		self.board = [[],[],[]]
	def draw_squares(self,screenn):
		screen.fill((255,255,255))
		for row in range(0,ROW+1,1):
			for col in range(0,COL+1,1):
				pygame.draw.rect(screen,(0,0,0),(row*200,col*200,200,200),1)

b=board()
b.draw_squares(screen)
pygame.display.update()	

#function that solves this using Tabu search
while cost>0:
	LL=[]
	cost=calcost(L)
	for r in range(len(L)):
		if L[r]==r:
			LL.append(L[r])
	randomN1 = random.randint(0, 8)
	while randomN1 in LL: 
		randomN1 = random.randint(0, 8)
	for k in range(len(L)):
		if L[k]==randomN1:
			break
	#smaller neighbor
	randomN2=random.randint(0, 8)
	while randomN2==randomN1 or randomN2 in LL:
		randomN2=random.randint(0, 8)
	for t in range(len(L)):
		if L[t]==randomN2:
			break
	#bigger neighbor
	if len(LL)<7:
		randomN3=random.randint(0, 8)
		while randomN3==randomN1 or randomN3 in LL or randomN3==randomN2:
			randomN3=random.randint(0, 8)
		for s in range(len(L)):
			if L[s]==randomN3:
				break
	#for k-1 only, unless it's null
		if L[s] is not None:
			L[k],L[s]= L[s],L[k]
			if L in Tabu:
				L[k],L[s]= L[s],L[k]
				cost1=2000
			else:
				cost1=calcost(L)
				L[k],L[s]= L[s],L[k]
	#for k+1 onyl, unless it's null
		if L[t] is not None:
			L[k],L[t]= L[t],L[k]
			if L in Tabu:
				L[k],L[t]= L[t],L[k]
				cost2=200
			else:
				cost2=calcost(L)
				L[k],L[t]= L[t],L[k]
		if cost2<cost1 and cost2<cost:
			L[k],L[t]= L[t],L[k]
		elif cost1<cost2 and cost1<cost:
			L[k],L[s]= L[s],L[k]

		elif cost2>cost and cost1>cost:
			Tabu.append(L)
			print('Tabu',cost,Tabu)
			if cost1==min(cost1,cost2):
				L[k],L[s]= L[s],L[k]
			elif cost2==min(cost1,cost2):
				L[k],L[t]= L[t],L[k]
		else:
			cost=calcost(L)
	else:
		for m in range(len(L)):
			if L[m]!=m:
				L2.append(L[m])
		for h in range(len(L)):
			for k in range(len(L)-1,0,-1):
				if L[h] in L2 and L[k] in L2:
					L[k],L[h]=L[h],L[k]
					break
		cost=calcost(L)
	l=0
	b=board()
	b.draw_squares(screen)
	for n in range(len(L)):
		if L[n]==0:
			L[n]=''
	for iii in range(1,6,2):
		for jjj in range(1,6,2):
			font = pygame.font.SysFont(None, 40)
			img = font.render(str(L[l]), True, (255,0,0))
			#print(l)
			l=l+1
			screen.blit(img, (100*jjj, 100*iii))
			pygame.display.update()	
	for n in range(len(L)):
		if L[n]=='':
			L[n]=0
	clock.tick(7)


running = True
while running:
  	for event in pygame.event.get():
	    if event.type == pygame.QUIT:
	    	running = False
	    if running == False:
	    	pygame.quit()




	
