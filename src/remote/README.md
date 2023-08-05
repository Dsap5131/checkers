# remote

Remote directory contains the information needed to run proxies to allow 
remote connections.

# Design


![Fig remote_directory_design.png](./../../resources/UML_diagrams/remote_directory_design.png)


# Referee-Player Proxy Communications

Player - Referee communication proxies will use JSONs through JsonConverter

There will be 3 things to be send through proxies

A PlayerProxy is a proxy that allows the game to talk to the player.
A RefereeProxy is a proxy that allows the player to talk to the referee.

JSON Communication Guide

![](../../resources/swimlane_diagrams/proxy_communications.png)


# Directory 
| File or Folder | About |
| ---            | ---   |
| [playerproxy.py](./playerproxy.py) | PlayerProxy |
| [refereeproxy.py](./refereeproxy.py) | RefereeProxy |