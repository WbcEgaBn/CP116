# 3 Body Simulation in Python
This repository will hold all the code needed for the 3 body simulation. 
<br>There are 3 classes: ```Interface```, ```Simulate```, and ```Planets```.
### The ```Interface``` Class:
* This class will takes a planet's coordinate location and plot it on the screen.

### The ```Simulate``` Class:
* This class will compute the planets' new coordinates based off the planets' old data.

### The ```Planets``` Class:
* This class will store data such as location and velocity.

## To Run the Progam:
1) Load in all three files into a code editor folder.
2) Install pygame and pygame-widgets using ```pip install pygame``` and ```pip install pygame-widgets```.
3) Run ```interface.py```. A new screen should appear with a UI.

## Buttons, Toggles Switches and Sliders
The user interface has a number of different variables the user can mess with.
New planets can be placed with the mouse, or can be loaded in with the preset planet locations.
#### Start Button
Starts the simulation. New planets can be added while the simulation is running.
#### Stop Button
Pauses the current simulation. The start button may be pressed to resume.
#### Reset Button
Clears the screen, and deletes any planet data previously set.
#### Set v0 = 0
Planets can normally be held and dragged to set an initial velocity. When this setting is turned off, you will not be able to set an initial velocity.
#### Show Planet Trail
This setting allows the user to display the locations a planet has passed through.
#### Show System CM
This will show the center of mass of the system. 
#### Gravitational Constant
This slider allows the user to user to change the amount of gravity planets experience within each other.
#### Yeet Constant
The yeet constant determines at what velocity a planet should start at depending on how far a click is dragged.
#### Time Step
Time between each new calculation will change with this slider.
#### Mass
This changes the mass of the next planet placed.
#### Collison Constant
This changes the distance between two planets needed for them to collide.
#### Scalene Triangle, Trapezoid, and 3 Body Orbit
These buttons load in hardcoded initial planet data. When a button is pressed, the screen is cleared beforehand.
#### Save Orbit
This button saves the current orbit of the planets the user has placed.
#### Load Saved Orbit
The current screen will be cleared and the saved orbit will be loaded and displayed on the screen.

### Credits go to our wonderful project members :)
