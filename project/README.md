# Chicken Cross
#### Video Demo: https://www.youtube.com/watch?v=Vm1t79NqeuI
#### Description:
The project I created is  **Chicken Cross** using python, a frogger-style game 
where you control your character's movement with the arrow keys. The goal is to 
reach the other side of the road and touch the crown to proceed to the next level, 
while avoiding cars on your way. You have 3 extra lives at the start of the game, 
and lose one each time you are unfortunately struck by a car, one life stock will 
be removed each time from the top left of your screen. You can see what level you
are on by looking towards the top right of your screen, where you will see a
a level tracker that goes up by one every time you reach the crown, also you'll
see at the top right corner, your highest level reached will be tracked so you 
can strive to beat your personal record for each session! Of course a game 
wouldn't be as fun if it didn't seem to get harder as you progress, so with each
new level the game difficulty increases slightly meaning the car speed slowly
increases with each level beat but your character gets faster as well.


#### main.py:
The main file is where the overall class for the game is created to manage the 
games assets and behavior. Such as initializing the game and creating its
resources, starting the main loop for the game, checking for key events, updating
the screen and some others that controll functions of the game.


#### character.py:
The character file is the module where the **Character** class is created and
imported from. The **Character** class is used to manage the character such as,
Initializing the character and setting its start point on the screen, updating
the character position based on movement flags, resetting the character when a
new game is started or a new life and drawing the character at its current location.


#### cars.py:
The cars file is the module where I created instances of each car that will be
seen on the screen. I made a class for each separate car, in each class the car
image is loaded and its rect attribute is set, each car is placed in the desired
location. An update function is in each class to control the direction of the car
moves and the speed at which it moves up or down the screen.



#### settings.py:
The settings file is where the class *Settings** is created and used to store
a broader range of settings and calls from such as Some static settings like
width and height of the screen and the background image, how many lives the player
starts with and how quickly the game speeds up. There is also a function to store
settings that will be changed such as the character's speed and each car's speed
since they are moving at different speeds. And a function to increase the speeds
of the character and the cars.


#### finish.py:
The finish file is a small module I created to manage a finish area for each level. 
The class **Finish** loads in the image of the crown which is where you must reach 
to proceed to the next level and sets the position of where the crown will be. 
Also, a function to draw the crown at its position.


#### buttons.py:
The buttons file is where the class for **Button** is created and is used to build
the button for the game. The button attributes are initialized, and a prep message
function is made to turn the message into a rendered image and center text on the
button. Also, a draw button function is made to draw a blank button, and then draw
the message onto the button.


#### scoreboard.py:
The scoreboard file is where the **Scoreboard** class is made. It is used to
report scoring information and initialize scorekeeping attributes. It has
functions such as **prep_level** to turn the level into a rendered image and
position the level information, **prep_highest_level** to turn the highest level
reached into a rendered image and set its position on the screen, **check_highest_level**
used to check if there is a new high level, **show_scores** to draw the information
onto the screen and **prep_lives** to show how many extra lives the player has left.


#### game_stats.py:
The game_stats file is where the **GameStats** class is created and used to track
statistics for the game. Statistics are initialized and a function **reset_stats**
is created to initialize statistics that can change during the game.