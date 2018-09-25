import requests
import json

homeurl='https://ponychallenge.trustpilot.com'
post1='/pony-challenge/maze'
data1={
  "maze-width": 15,
  "maze-height": 15,
  "maze-player-name": "Ponis",
  "difficulty": 0
}
headers={}
r=requests.post(himeurl+post1,data=data1,headers=headers)
