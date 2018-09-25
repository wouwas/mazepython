import requests
import json
from requests import Request, Session

ponyname='Pinkie Pie'
mainurl='https://ponychallenge.trustpilot.com/pony-challenge/'
def NewMaze(height,width,ponyname="Pinkie Pie"):
    url='maze'    
    data={"maze-width": height,
    "maze-height": width,
    "maze-player-name": ponyname,
    "difficulty": 0
    }
    data_json = json.dumps(data)
    headers = {"Content-Type":"application/json","Accept": "application/json"}
    request=MazeRequestWrapper(reqType='POST',url=mainurl+url,data_json=data_json,reqHeaders=headers)
    return request
    
    
   
    
    
def getMaze(MazeId):
    url='maze/'+MazeId
    headers = {"Content-Type":"application/json","Accept": "application/json"}
    response=MazeRequestWrapper(reqType='GET',url=mainurl+url,data_json='',reqHeaders=headers)
    return response
def MazeRequestWrapper(reqType,url,reqHeaders,data_json):
    if reqHeaders:
        headers=reqHeaders
    else:
        headers={"Content-Type":"application/json","Accept": "application/json"}
    s=Session()
    if reqType=='GET':
        rdef=Request('GET',url,headers=headers)
    elif reqType=='POST':
        rdef=Request('POST',url,data=data_json,headers=headers)
    prepped=rdef.prepare()
    pretty_print_POST(prepped)
    r=s.send(prepped)
    if r.status_code == requests.codes.ok:
        return r
    else:
        print(r.json)
        print(r.status_code)
        print(r.text)
        pretty_print_POST(prepped)
        r.raise_for_status()          
        

def pretty_print_POST(req):
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

def MakeMove (MazeID,Move):
    url='POST /pony-challenge/maze/{maze-id}'

'''curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{ \ 
   "maze-width": 15, \ 
   "maze-height": 15, \ 
   "maze-player-name": "Pinkie Pie", \ 
   "difficulty": 0 \ 
 }' 'https://ponychallenge.trustpilot.com/pony-challenge/
'''
#maze_id={  "maze_id": "bf36a64b-b908-4ab9-b1c5-43f257d24340"}

final_state={
  "state": "over",
  "state-result": "You lost. Killed by monster",
  "hidden-url": "/eW91X2tpbGxlZF90aGVfcG9ueQ==.jpg"
}

maze_id=json.loads(NewMaze(15,15,'Pinkie Pie').text)['maze_id']
maze=getMaze(maze_id)
maze_json=json.loads(maze.text)
maze_json['data']
maze_json['game-state']
game-state['maze_id']
maze_json['pony']
maze_json['domokun']
maze_json['endpoint']
maze_json['size']

with open('maze.json', 'w') as outfile:
    json.dump(maze_json, outfile)
