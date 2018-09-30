import ponychallenge as conn
import maze
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

mainurl = config['CONNECTION']['mainurl'] 
height = int(config['MAZE']['height'])
width=int(config['MAZE']['width'])
ponyname=config['PONY']['ponyname']
difficulty=int(config['MAZE']['difficulty'])


mazeconnection=conn.connectionPony(height,width,ponyname,difficulty,mainurl)

maze_id=mazeconnection.new()
#maze_id=json.loads(NewMaze(15,15,'Pinkie Pie').text)['maze_id']
#maze=mazeconnectio.get()
maze_json=mazeconnection.get()
maze=maze.game(maze_json)
maze.shortest_path(maze.endpoint)
for i in range(0,maze.pony):
    maze.makeMovePony()
    direction= conn.MoveDirection(maze.pony_old,maze.pony,maze.size[0])
   
    mazeconnection.move(direction) #make move send move to connection
   
    maze.update(mazeconnection.get())
    print(direction)
    maze.printmaze()
    print(maze.game_state)
    if maze.cells[maze.pony]==0:
        break
    if maze.game_state['state']!='active':
        break

