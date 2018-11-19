Names : Owen Barnett, Justin Hahn, Kate Sweeney

	Our project is a two-player boxing game. The game involves two players
fighting each other on a 1D stage. Each fighter will be equipped with health 
(that does not regenerate), energy (that does regenerate), and several fighting 
moves. Each fighting move will take energy. These moves include a punch, a kick, 
and a block. Each character can move left and right on this stage and and 
depending how close a boxer is to the other boxer attacks may hit or miss. In 
addition blocking stops your energy from regenerating and lowers damage taken 
from opponents moves. A boxer wins when he has decreased his opponent's health to
zero.

	MVC allows for the modular design of our game. It seperates out the tasks. 
The Boxer class is the model, the fxml file it the view, and the Controller class 
is the controller. This allows the boxer class to focus only on the interactions 
between the two boxers. The controller class class can focus on changing the view 
and handling user input. MVC allows for ease of modification, especially in our 
group of three. We can work on seperate pieces of the project at the same time 
while avoiding merge conflicts.

Core Classes:
	- Boxer.java
	- Controller.java
	- Main.java
	- Boxing.fxml

Program Status:
	Our game works, and has all the important features that we planned to add. 
We did not add health and energy bars, instead we just used numbers. We also 
changed some of the game mechanics so that the game is easier to play. Our controls 
are optimized for two player game play, however they are easy to change.

Credit to Assets: Street Fighter II on the SNES
