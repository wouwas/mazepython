pip3 install requests
python3 main.py
Script solves https://ponychallenge.trustpilot.com/index.html
-Reads configuration file
-Moves pony throuht the maze by calculating shortest path between pony and exit.
-Calculates moves and transfers moves to REST-API

main.py

Script  reads in configuration file config.ini
Handles basic logic. Calls othe modules. 

ponychallenge.py
    module handles ponny challenge connections to REST-API

maze.py
    Calculates shortest path and moves based on maze.json
    Has module mazeRoutes which could be  used to calculate



Execition example:

+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
|   |           |               |                   |               |   |       |
+   +   +---+   +   +   +---+   +---+---+   +---+   +---+---+   +   +   +   +   +
|   |   |   |       |   |                   |   |               |       |   |   |
+   +   +   +---+---+   +---+---+---+---+---+   +---+---+   +---+---+---+   +   +
|   |       |       |               |       |               |       |       |   |
+   +---+---+   +   +   +---+---+   +   +   +---+---+---+   +   +   +   +---+   +
|               |   |   |           |   |               |   |   |       |   |   |
+---+---+---+---+   +---+   +---+---+   +---+---+---+   +   +   +---+---+   +   +
|       |       |       |   |       |           |       |   |   |           |   |
+   +   +   +   +---+   +   +   +   +---+---+   +   +   +---+   +---+---+   +   +
|   |       |       |   |       |               |   |   |                   |   |
+   +---+---+---+   +   +   +---+---+   +---+---+   +   +   +---+---+---+---+   +
|       |       |       |   |       |       |       |   |   |   |               |
+---+   +---+   +---+---+---+   +   +---+---+   +   +---+   +   +   +---+---+   +
|       |           |           |               |   |       |   |       |       |
+   +---+   +---+   +   +   +---+---+---+---+   +---+   +---+   +---+   +---+---+
|       |       |       |   |               |   |       |           |           |
+---+   +   +   +---+---+---+   +---+---+   +   +   +---+   +---+   +---+---+   +
|   |   |   |   |           |   |       |   |   |       |   |               |   |
+   +   +   +   +   +---+   +   +   +---+   +   +---+   +---+   +---+   +---+   +
|   |   |   |   |       |       |   |       |       |       |   |   |   |       |
+   +   +---+   +---+   +---+---+   +   +---+---+---+---+   +   +   +   +   +   +
|   |       |       |   |   |       |   |               |       |       |   |   |
+   +---+   +   +---+   +   +   +   +   +   +---+   +---+---+   +---+---+   +---+
|       |   |           |       |   |       |   |               |       |       |
+   +   +   +   +---+---+   +---+   +---+---+   +---+---+---+---+   +   +---+   +
|   |       |   |               |               |                D  |   |       |
+   +---+---+   +   +---+---+---+---+   +---+   +   +---+---+---+---+   +   +   +
|   |   |       |       |               |       |   |               |       |   |
+   +   +   +---+   +---+   +---+---+---+---+   +   +   +---+---+   +---+---+   +
|   |           |   |       |               |   |               |       |       |
+   +---+---+   +---+   +   +   +---+---+   +---+---+---+---+---+   +   +   +---+
|       |   |           |   |       |   |           |           |   |   |       |
+---+   +   +---+   +---+---+---+   +   +---+---+   +   +---+   +---+   +---+---+
|       |           |           |   |           |   |   |           |           |
+   +---+---+---+---+   +---+   +   +   +   +---+   +   +---+---+   +   +---+   +
|   |           |       |       |   |P  |   |       |       |   |   |   |       |
+   +---+   +   +   +---+   +---+   +   +   +   +---+---+   +   +   +---+   +   +
|           |       |               |E  |                   |               |   |
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
{'state': 'active', 'state-result': 'Move accepted'}
369-----389----20
-----------START-----------
POST https://ponychallenge.trustpilot.com/pony-challenge/maze/2aa832b8-347d-4ef9-bf96-1109ca831ffb
Content-Type: application/json
Accept: application/json
Content-Length: 22

{"direction": "south"}
-----------START-----------
GET https://ponychallenge.trustpilot.com/pony-challenge/maze/2aa832b8-347d-4ef9-bf96-1109ca831ffb
Content-Type: application/json
Accept: application/json

None
south

