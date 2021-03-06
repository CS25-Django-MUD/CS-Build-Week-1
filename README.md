# CS Build Week 1 - Django MUD

## [LINK TO THE MUD](https://cs25-mud.herokuapp.com/)

## Game Developers 
|[Michael Chrupcala](https://github.com/mchrupcala)  |  
[Steven Rollins](https://github.com/greenhornsr)        |   
[John Morrison](https://github.com/JohnMorrisonn)  |
| :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: | 
|                 [<img src="https://ca.slack-edge.com/T4JUEB3ME-UJKJRJAPJ-3af635a5f445-512" width = "200" />](https://github.com/mchrupcala)                       |                      [<img src="https://ca.slack-edge.com/T4JUEB3ME-UGHQDL8JK-da24317d310a-512" width = "200" />](https://github.com/greenhornsr)                       |                      [<img src="https://ca.slack-edge.com/T4JUEB3ME-UL5V3G7A9-002c8227b12a-512" width = "200" />](https://github.com/JohnMorrisonn)                       |       
|[<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/mchrupcala)                 |            [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/greenhornsr)             |           [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/JohnMorrisonn)                  |

### What is a MUD?
>A MUD...is a multiplayer real-time virtual world, usually text-based. MUDs combine elements of role-playing games, hack and slash, player versus player, interactive fiction, and online chat. Players can read or view descriptions of rooms, objects, other players, non-player characters, and actions performed in the virtual world. Players typically interact with each other and the world by typing commands that resemble a natural language. - Wikipedia

### How we did it

- Front-End: Michael's stuff
- Back-End: Django python app
- Deployment: Heroku

### First-step: Register/Log-in

>Make sure to register a new account with a strong password and login to access the MUD map.

### Second-step: Explore!

>Use the move buttons to traverse the map and explore the rooms and their hidden content!


### API routes


## Need to edit FE apis


[api/register](https://cs25-mud.herokuapp.com/api/register) : Register username and strong password


[api/login](https://cs25-mud.herokuapp.com/api/login) : Login page to get access to play the game


[api/init](https://cs25-mud.herokuapp.com/api/init) : Initialize the player on the map


[api/move](https://cs25-mud.herokuapp.com/api/move) : API called when clicking a move button to go to the next room


[api/adv/rooms](https://cs25-mud.herokuapp.com/api/adv/rooms) : List of all available rooms with Ids, Titles, Descriptions, and coordinates


[api/adv/players](https://cs25-mud.herokuapp.com/api/adv/players) : List of all current players and their current rooms


