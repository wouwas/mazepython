import json
import  sys
import os
import time

class game:
    def __init__(self,maze_json):
        self.update(maze_json)
        self.cells={}
    def update(self,maze_json):
        self.game_state=maze_json['game-state']
        self.pony=maze_json['pony'][0]
        self.pony_old=maze_json['pony'][0]
        self.domokun=maze_json['domokun'][0]
        self.endpoint=maze_json['end-point'][0]
        self.size=maze_json['size']
        self.maze=maze_json['data']
        self.maxlength=0
        #self.cells={}
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
               
    def printmaze(self,printvalues=0,printcells=None):
            if printcells is None:
                printcells=self.cells
            nwall='--'
            wwall='|'
            intersect='+'
            line=''
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
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
                            if  index in printcells.keys() and printvalues==1:
                              value=value+str(printcells[index])
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
        self.pony_old=self.pony
        self.pony=movetocell
    def makeMoveDomokun(self):
        charmove=self.cellpossiblemove(self.domokun)
        movecellsiter={k:v for k,v in self.cells.items() if k in charmove}
        movetocell=min(movecellsiter,key=movecellsiter.get) #choose shortest path
        self.domokun=movetocell
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
class mazeRoutes:
    ''' Class calculates shortest possible routes between cells.
    Usage  
        maze=game(maze_json)
        mazeroute=mazeRoutes(maze)
        mazeroute.makeMove(maze.pony,maze.endpoint,[4,10,34,23])
        Calculates shortest route from startpoint to endpoint.
        ForbidenCells - list doesnt' allow to include theese cells in shortest route. 
        example could be domokun monster cell.

        mazeroute.cells - contains infromation only about cells relative distance till endpoint
        mazeroute.path  - list cells that define shortest path. Filled by makeMove method.

        cells[startcell] contains value ERR  if path not is not found.
                        contains value ST    if path is found.
                        each cell in path is marked '%%'
                        each Forbiden cell is marked  with 'X'
        '''
    def __init__(self,maze):
        self.maze=maze
        self.cells={}
        self.routes=[]
    def nextCell(self,startpoint,endpoint=None,ForbidenCells=[]):
        newcellid=startpoint
        i=0
        maxlength=0
        #terminate calculationif start point reached
        while newcellid>-1 or move==endpoint:
            i=+1
            newcellid=-1
            cels=list([x for x in self.cells.keys() if self.cells[x]==maxlength])
            maxlength=maxlength+1
            #print(maxlength)
            #print(cels,maxlength)
            for possiblemove in cels:
               for move in self.maze.cellpossiblemove(possiblemove):
                   if move>-1 and move not in ForbidenCells:
                       #print ('Possible to move from ',possiblemove,'to' ,move)
                       if move not in  self.cells:
                           self.cells[move]=maxlength+0
                           newcellid=move
               #printf(move,possiblemove,i)
               yield possiblemove # return  Cell id
               
    def shortest_path(self,start_point,endpoint=None,ForbidenCells=[]):
        self.cells[start_point]=0
        self.maxlength=0
        for cellid in self.nextCell(start_point,endpoint,ForbidenCells):
            pass
    def makeMove (self,start,end,ForbidenCells=[]):
        self.shortest_path(end,start,ForbidenCells)
        self.path=[]
        movetocell=start
        if start in self.cells.keys():
            self.path.append(start)
            for i in range(0,self.cells[movetocell]):            
                charmove=self.maze.cellpossiblemove(movetocell)
                movecellsiter={k:v for k,v in self.cells.items() if k in charmove}
                movetocell=min(movecellsiter,key=movecellsiter.get) #choose shortest path
                self.path.append(movetocell)
        #self.cells.clear() #cleanup
        if start not in self.path:               
           self.cells[start]='ERR'
        else:
           self.cells[start]='ST'
        self.cells[end]='END'

        for i in self.path:
            self.cells[i]='%%'
        for i in ForbidenCells:
            self.cells[i]='X'

        
                       
        
    
                        
                  
                  
              
          
          
          
if __name__ == "__main__":           
#shortest path
    #Shortest Path
    with open('maze.json', 'r') as outfile:
        maze_json=json.load(outfile)
    maze=game(maze_json)
    maze.shortest_path(maze.endpoint)
    for i in range(0,maze.pony):
        if i%1==0:
            maze.printmaze()
        maze.makeMoveDomokun()
        maze.makeMovePony()
        if maze.cells[maze.pony]==0:
            break
    maze.printmaze()
    mazeroute=mazeRoutes(maze)
    mazeroute.makeMove(0,6)
    maze.printmaze(1,mazeroute.cells)
    time.sleep(4)
    # test 
    mazeroute2=mazeRoutes(maze)
    mazeroute2.makeMove(maze.pony,maze.endpoint,[4,10,34,23])
    maze.printmaze(1,mazeroute2.cells)
    time.sleep(4)
    # remove west walls to test activities.
    for i in range(0,len(maze.maze)-1):
        if 'west' in maze.maze[i] and i%maze.size[0]!=0:
            maze.maze[i].remove('west')
        
    mazeroute3=mazeRoutes(maze)
    mazeroute3.makeMove(maze.pony,maze.endpoint,[4,10,34,23])
    maze.printmaze(1,mazeroute3.cells)




    


