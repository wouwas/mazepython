import requests
import json
import maze
from requests import Request, Session

class connectionPony:
    def __init__(self,height,width,ponyname,difficulty,mainurl):
        self.height=height
        self.width=width
        self.ponyname=ponyname
        self.difficulty=difficulty
        self.mazeId=None
        self.mainurl=mainurl

    def new(self):
        url='maze'    
        data={"maze-width": self.height,
        "maze-height": self.width,
        "maze-player-name": self.ponyname,
        "difficulty": self.difficulty
        }
        data_json = json.dumps(data)
        headers = {"Content-Type":"application/json","Accept": "application/json"}
        request=self.MazeRequestWrapper(reqType='POST',url=url,data_json=data_json,reqHeaders=headers)
        self.mazeId=json.loads(request.text)['maze_id']
        
    def get(self):
        url='maze/'+self.mazeId
        headers = {"Content-Type":"application/json","Accept": "application/json"}
        self.response=self.MazeRequestWrapper(reqType='GET',url=url,data_json='',reqHeaders=headers)
        self.response_json=json.loads(self.response.text)
        return self.response_json
    def move (self,direction):
        url='maze/'+self.mazeId   
        data={"direction": direction}
        data_json = json.dumps(data)
        headers = {"Content-Type":"application/json","Accept": "application/json"}
        request=self.MazeRequestWrapper(reqType='POST',url=url,data_json=data_json,reqHeaders=headers)
        return request

    def MazeRequestWrapper(self,reqType,url,reqHeaders,data_json):
        requesturl=self.mainurl+url
        if reqHeaders:
            headers=reqHeaders
        else:
            headers={"Content-Type":"application/json","Accept": "application/json"}
        s=Session()
        if reqType=='GET':
            rdef=Request('GET',requesturl,headers=headers)
        elif reqType=='POST':
            rdef=Request('POST',requesturl,data=data_json,headers=headers)
        prepped=rdef.prepare()
        self.pretty_print_POST(prepped)
        r=s.send(prepped)
        if r.status_code == requests.codes.ok:
            return r
        else:
            print(r.json)
            print(r.status_code)
            print(r.text)
            self.pretty_print_POST(prepped)
            r.raise_for_status()          
            

    def pretty_print_POST(self,req):
        """
        At this point it is completely built and ready
        to be fired; it is "prepared".

        However pay attention at the formatting used in 
        this function because it is programmed to be pretty 
        printed and may differ from the actual request.
        """
        print('{}\n{}\n{}\n\n{}'.format(
            '-----------START-----------',
            req.method + ' ' + req.url,
            '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
            req.body,
        ))
    def save(self):
        with open('maze.json', 'w') as outfile:
            json.dump(maze_json, outfile)


#maze_id={  "maze_id": "bf36a64b-b908-4ab9-b1c5-43f257d24340"}

##final_state={
##  "state": "over",
##  "state-result": "You lost. Killed by monster",
##  "hidden-url": "/eW91X2tpbGxlZF90aGVfcG9ueQ==.jpg"
##}
def MoveDirection(before,after,horizontal):
    ''' Procedufe calculates direction from before and after values and based on maze dimensions.'''
    diff=before-after
    print (str(before)+'-----'+str(after)+'---'+str(diff))
    if diff==1:
        return 'west'
    if diff==-1:
        return 'east'
    if diff==horizontal:
        return 'north'
    if diff==horizontal*-1:
        return 'south'
    print (before+'-----'+after)

if __name__ == "__main__":  
    mainurl='https://ponychallenge.trustpilot.com/pony-challenge/'
    ponyname='Pinkie Pie'
    mazeconnection=connectionPony(15,15,ponyname,2,mainurl)
    maze_id=mazeconnection.new()
    #maze_id=json.loads(NewMaze(15,15,'Pinkie Pie').text)['maze_id']
    #maze=mazeconnectio.get()
    maze_json=mazeconnection.get()
    maze=maze.game(maze_json)
    maze.shortest_path(maze.endpoint)
    for i in range(0,maze.pony):
        maze.makeMovePony()
        direction=   MoveDirection(maze.pony_old,maze.pony,maze.size[0])
        mazeconnection.move(direction) #make move send move to connection
        maze.update(mazeconnection.get())
        maze.printmaze()
        print(maze.game_state)
        if maze.cells[maze.pony]==0:
            break
        if maze.game_state['state']!='active':
            break




