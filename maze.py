import json
import  sys
import os

class game:
    def __init__(self,response):
        self.game_state=maze_json['game-state']
        self.pony=maze_json['pony'][0]
        self.domokun=maze_json['domokun'][0]
        self.endpoint=maze_json['end-point'][0]
        self.size=maze_json['size']
        self.maze=maze_json['data']
        self.maxlength=0
        self.cells={}
    def shortest_path(self,start_point):
        self.cells[start_point]=0
        self.maxlength=0
        for cellid in self.nextCell(start_point):
            pass #self.cells[cellid]=self.maxlength
    def cellpossiblemove(self,id):
        possiblemoves=[]
        ''' Assumption that maze is correctly built and has outer borders no error check'''
        nomove=-1
        if id>self.size[0] and 'north' not in self.maze[id] :
            north=id-self.size[0]
        else:
            north=nomove
        if id<self.size[0]*self.size[1]-self.size[0] and'north' not in self.maze[id+self.size[0]] :
            south=id+self.size[0]
        else:
            south=nomove
        if id%self.size[0]!=0 and 'west' not in self.maze[id]  :
            west=id-1
        else:
            west=nomove
        if id+1%self.size[0]!=0 and id+1< len(self.maze) and 'west' not in  self.maze[id+1] :
            east=id+1
        else:
            east=nomove
        #print('pausable move',id,[north,east,south,west])
        return [north,east,south,west]
        
    def nextCell(self,startpoint):
        newcellid=startpoint
        i=0
        maxlength=0
        
        while newcellid>-1:
            i=+1
            newcellid=-1
            cels=list([x for x in self.cells.keys() if self.cells[x]==maxlength])
            maxlength=maxlength+1
            #print(maxlength)
            #print(cels,maxlength)
            for possiblemove in cels:
               for move in self.cellpossiblemove(possiblemove):
                   if move>-1:
                       #print ('Possible to move from ',possiblemove,'to' ,move)
                       if move not in  self.cells:
                           self.cells[move]=maxlength+0
                           newcellid=move
               #printf(move,possiblemove,i)
               yield possiblemove # return  Cell id
               
    def printmaze(self,printvalues=0):
            nwall='--'
            wwall='|'
            intersect='+'
            line=''
            for y in  range(0,self.size[1]):
                for iter in range(1,3):
                    for x in range(0,self.size[0]):
                        value=''
                        index=y*self.size[0]+x
                        
                        walls=self.maze[index]
                        if iter==1:
                          if 'north' in walls:
                              line=line+'+---'
                          else:
                              line=line+'+   '
                          if x==self.size[0]-1:
                              #last column
                              line=line+'+'
                        if  iter==2:
                            if index==self.domokun:
                              value=value+'D'
                            if index==self.pony:
                              value=value+'P'
                            if  index==self.endpoint:
                              value=value+'E'
                            if  index in self.cells.keys() and printvalues==1:
                              value=value+str(self.cells[index])
                            if len(value)>3:
                              value=value[0:3]
                            elif len(value)<3:
                              value=value+' '*(3-len(value))
                            if 'west' in walls:
                              value='|'+value
                            else:
                              value=' '+value
                            line=line+value
                            if x==self.size[0]-1:
                              #last column
                              line=line+'|'
                    print (line)
                    line=''
            print('+'+'---+'*self.size[0]) #last row 
                        
    def makeMovePony (self):
        charmove=self.cellpossiblemove(self.pony)
        #print(charmove)
        movecellsiter={k:v for k,v in self.cells.items() if k in charmove}
        movetocell=min(movecellsiter,key=movecellsiter.get) #choose shortest path
        #run away from domokun
        #check if domokun is in your path then go shortest path
        # If domokun is in your way search alternative route (recalculate shortest path interpret domokun as wall
        # if no path and domokun in a way. Just move closer
            # if domokun to close move away(runaway)
            # if run away choose path with most intersections (how) 
        self.pony=movetocell
    def makeMove (self,start,end):
        self.shortest_path(end)
        self.path=[]
        movetocell=start
        for i in range(0,maze.cells[movetocell]):            
            charmove=self.cellpossiblemove(movetocell)
            movecellsiter={k:v for k,v in self.cells.items() if k in charmove}
            movetocell=min(movecellsiter,key=movecellsiter.get) #choose shortest path
            self.path.append(movetocell)
        for i in self.path:
            self.cells[i]='%%'
        
    
    
                       
        
    
                        
                  
                  
              
          
          
          
            

with open('maze.json', 'r') as outfile:
    maze_json=json.load(outfile)
maze=game(maze_json)
#maze.shortest_path(maze.endpoint)
#for i in range(0,maze.pony):
#    if i%1==0:
#        maze.printmaze()
#    maze.makeMovePony()
#    if maze.cells[maze.pony]==0:
#        break
#maze.printmaze()
maze.makeMove(maze.pony,maze.endpoint)
maze.printmaze(1)




    


